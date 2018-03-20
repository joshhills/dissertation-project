# Grunt task worker to initiate specific bespoke tasks.
from __future__ import division

import shared.database

db = shared.database.Couchbase(host="couchbase://128.199.62.177")

# product_ids_results = db.run_query('select product_id from job', 'job')

product_ids_results = ["437550"]

overall_results = []

for row1 in product_ids_results:

    product_id = row1

    print "Working on " + product_id

    error = True
    results = []
    while error:
        try:
            update_count = -1
            present_user_score = -1
            start_user_score = -1
            review_count = -1
            review_midpoint_time = -1

            # Get date of first review
            date_first_review = -1

            results = db.run_query(
                'select date_created from `review` where product_id="' + str(product_id) + '" order by date_created asc limit 1', 'job')

            for row in results:
                date_first_review = row['date_created']

            # Get date of last update
            date_last_review = -1

            results = db.run_query(
                'select date_created from `review` where product_id="' + str(product_id) + '" order by date_created desc limit 1', 'job')

            for row in results:
                date_last_review = row['date_created']

            review_midpoint_time = int(date_first_review + ((date_last_review - date_first_review) / 2))

            # Build user score at midpoint.
            results = db.run_query(
                'select voted_up from `review` where product_id="' + str(product_id) + '" and date_created < ' + str(review_midpoint_time), 'job')

            num_voted_up2 = 0
            num_voted_down2 = 0
            for row in results:
                if row['voted_up']:
                    num_voted_up2 += 1
                else:
                    num_voted_down2 += 1

            score_at_midpoint = (num_voted_up2 / (num_voted_up2 + num_voted_down2)) * 100

            results = db.run_query(
                'select count(*) as cnt from `review` where product_id="' + str(product_id) + '"', 'job')

            for row in results:
                review_count = row['cnt']

            results = db.run_query(
                'select count(*) as cnt from `update` where product_id = "' + str(product_id) + '"', 'job')

            for row in results:
                update_count = row['cnt']

            results = db.run_query(
                'select user_score from `store` where product_id = "' + str(product_id) + '"', 'job')

            for row in results:
                present_user_score = row['user_score']

            # I need to get the date of the first update after 20 reviews.
            # So get the date of the 20th review
            results = db.run_query(
                'select date_created as twentieth_review_time from `review` where product_id = "' + str(
                    product_id) + '" order by date_created asc limit 1 offset 20 - 1', 'job')

            twentieth_review_time = -1
            for row in results:
                twentieth_review_time = row['twentieth_review_time']

            # So I need to get the date of the first update after that point
            results = db.run_query(
                'select date_created from `update` where product_id = "' + str(
                    product_id) + '" and date_created > ' + str(twentieth_review_time) + ' order by date_created asc limit 1', 'job')

            first_meaningful_update_date = -1
            for row in results:
                first_meaningful_update_date = row['date_created']

            # Finally, get all reviews before that point in time.
            results = db.run_query(
                'select voted_up from `review` where product_id = "' + str(
                    product_id) + '" and date_created < ' + str(first_meaningful_update_date), 'job')

            num_voted_up = 0
            num_voted_down = 0
            for row in results:
                if row['voted_up']:
                    num_voted_up += 1
                else:
                    num_voted_down += 1

            total_reviews_before_first_meaningful_update = num_voted_down + num_voted_up

            start_user_score = (num_voted_up / (num_voted_up + num_voted_down)) * 100

            result = {
                'start_user_score': int(start_user_score),
                'present_user_score': present_user_score,
                'update_count': update_count,
                'review_count': review_count,
                'total_reviews_before_first_meaningful_update': total_reviews_before_first_meaningful_update,
                'twentieth_review_time': twentieth_review_time,
                'review_midpoint_time': review_midpoint_time,
                'score_at_midpoint': int(score_at_midpoint)
            }

            print(result)

            overall_results.append(result)

            error = False
        except Exception, e:
            print "Timed out on {0}, trying again.".format(product_id)

print "Finally"
print overall_results
