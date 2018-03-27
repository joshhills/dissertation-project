# Grunt task worker to initiate specific bespoke tasks.
from __future__ import division

import shared.database
import json
import ast

db = shared.database.Couchbase(host="couchbase://128.199.62.177")

# product_ids_results = db.run_query('select product_id from job', 'job')

product_ids_results = ["356510"]

overall_results = []

for row1 in product_ids_results:

    product_id = row1

    print "Working on " + product_id

    error = True

    review_range_start = -1
    review_range_end = -1

    update_range_start = -1
    update_range_end = -1

    ccu_range_start = -1
    ccu_range_end = -1

    while error:
        # try:
        results = db.run_query(
            'select date_created, voted_up from `review` where product_id="' + str(product_id) + '" order by date_created asc', 'job')

        first = True

        day = {
          'day_start_time': -1,
          'total_reviews_voted_up': 0,
          'total_reviews_voted_down': 0,
          'total_reviews': 0,
          'total_updates': 0,
          'peak_ccu': 0
        }

        day_start_time = -1
        day_end_time = -1

        for row in results:
            date_created = row['date_created']
            voted_up = row['voted_up']

            day_start_time = date_created - (date_created % 86400)
            day_end_time = day_start_time + 86400

            # If this is a new day, push the old one.
            if day_start_time > day['day_start_time']:
                if not first:
                    day['total_reviews'] = day['total_reviews_voted_down'] + day['total_reviews_voted_up']
                    overall_results.append(day)
                else:
                    review_range_start = day_start_time
                    first = False

                day = {
                    'day_start_time': day_start_time,
                    'total_reviews_voted_up': 0,
                    'total_reviews_voted_down': 0,
                    'total_reviews': 0,
                    'total_updates': 0,
                    'peak_ccu': 0
                }

            if voted_up:
                day['total_reviews_voted_up'] += 1
            else:
                day['total_reviews_voted_down'] += 1

        # Push the last day.
        day['total_reviews'] = day['total_reviews_voted_down'] + day['total_reviews_voted_up']
        review_range_end = day['day_start_time']
        overall_results.append(day)

        overall_results.sort(key=lambda x: x['day_start_time'])
        print("After sequencing reviews:")
        print(overall_results)

        # Now do updates.
        results2 = db.run_query(
          'select date_created from `update` where product_id="' + str(
            product_id) + '" order by date_created asc', 'job')

        first_update = True
        update_date_created = -1
        day_start_time = -1
        # For every update.
        for row2 in results2:
            # Compute the start day.
            update_date_created = row2['date_created']
            day_start_time = update_date_created - (update_date_created % 86400)

            if first_update:
                update_range_start = day_start_time
                first_update = False

            found = False
            for item in overall_results:
                if item['day_start_time'] == day_start_time:
                    found = True
                    item['total_updates'] += 1

            if not found:
                overall_results.append({
                    'day_start_time': day_start_time,
                    'total_reviews_voted_up': 0,
                    'total_reviews_voted_down': 0,
                    'total_reviews': 0,
                    'total_updates': 1,
                    'peak_ccu': 0
                })
        update_range_end = day_start_time

        overall_results.sort(key=lambda x: x['day_start_time'])
        print("After sequencing updates:")
        print(overall_results)

        # For every CCU.
        results3 = db.run_query(
          'select `start`, `values` from `usage` where product_id="' + str(
            product_id) + '"', 'job')

        for row3 in results3:
            day_start_time = int(row3['start']) - (int(row3['start']) % 86400)

            # Convert values to array.
            values = ast.literal_eval(row3['values'])
            print('=-=-= ' + str(len(values)))
            ccu_range_start = day_start_time
            ccu_range_end = day_start_time + (len(values) - 1) * 86400

            for i in range(len(values)):
                temp_start_time = day_start_time + (86400 * i)

                found = False
                for item in overall_results:
                    if item['day_start_time'] == temp_start_time:
                        found = True
                        item['peak_ccu'] = values[i]

                if not found:
                    overall_results.append({
                      'day_start_time': temp_start_time,
                      'total_reviews_voted_up': 0,
                      'total_reviews_voted_down': 0,
                      'total_reviews': 0,
                      'total_updates': 0,
                      'peak_ccu': values[i]
                    })

        overall_results.sort(key=lambda x: x['day_start_time'])
        print("After sequencing ccu:")
        print(overall_results)
        print(len(overall_results))

        error = False
        # except Exception, e:
        #     print "Timed out on {0}, trying again.".format(product_id)

        print("review_range_start: " + str(review_range_start))
        print("review_range_end: " + str(review_range_end))

        print("update_range_start: " + str(update_range_start))
        print("update_range_end: " + str(update_range_end))

        print("ccu_range_start: " + str(ccu_range_start))
        print("ccu_range_end: " + str(ccu_range_end))

        latest_start = review_range_start
        if ccu_range_start > latest_start:
            latest_start = ccu_range_start

        earliest_end = review_range_end
        if ccu_range_end < earliest_end:
            earliest_end = ccu_range_end

        print("The smallest range is " + str(latest_start) + " to " + str(earliest_end))

        # temp_overall_results = [x for x in overall_results if x['day_start_time'] >= latest_start and x['day_start_time'] <= earliest_end]
        # overall_results = temp_overall_results

        print(int((overall_results[len(overall_results) - 1]['day_start_time'] - overall_results[0]['day_start_time']) / 86400))

        # Finally, fill in missing days.
        for j in range(int((overall_results[len(overall_results) - 1]['day_start_time'] - overall_results[0]['day_start_time']) / 86400)):
            # Check if it exists already as a day.
            dst = overall_results[0]['day_start_time'] + (j * 86400)
            f = False
            for k in overall_results:
                if k['day_start_time'] == dst:
                    f = True
            if not f:
                overall_results.append({
                    'day_start_time': dst,
                    'total_reviews_voted_up': 0,
                    'total_reviews_voted_down': 0,
                    'total_reviews': 0,
                    'total_updates': 0,
                    'peak_ccu': 0
                })

        overall_results.sort(key=lambda x: x['day_start_time'])
        print("After adding missing days:")
        print(overall_results)

# Sweep over results and compute accumulative user score.
total_positive = 0
total_negative = 0
for item in overall_results:
    total_positive += item['total_reviews_voted_up']
    total_negative += item['total_reviews_voted_down']
    user_score_snapshot = 0
    if total_positive == 0 and total_negative == 0:
        user_score_snapshot = 0
    elif total_positive == 0 and total_negative != 0:
        user_score_snapshot = 0
    elif total_positive != 0 and total_negative == 0:
        user_score_snapshot = 100
    else:
        user_score_snapshot = int(round((total_positive / (total_positive + total_negative)) * 100, 0))

    item['user_score_snapshot'] = user_score_snapshot

print "Finally"
overall_results.sort(key=lambda x: x['day_start_time'])
print overall_results
print len(overall_results)