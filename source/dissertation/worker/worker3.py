# Grunt task worker to initiate specific bespoke tasks.
from __future__ import division

import shared.database
import json
import ast

db = shared.database.Couchbase(host="couchbase://128.199.62.177")

product_ids_results = db.run_query('select product_id from job', 'job')

overall_results = []

for row1 in product_ids_results:

    product_id = row1['product_id']

    print "Working on " + product_id

    error = True

    while error:
        try:
            total_reviews_positive = -1
            total_reviews = -1

            results = db.run_query(
                'select count(*) as cnt from `review` where product_id="' + str(product_id) + '" and voted_up = true',
                'job')

            for row in results:
                total_reviews_positive = row['cnt']

            results = db.run_query(
                'select count(*) as cnt from `review` where product_id="' + str(product_id) + '"',
                'job')

            for row in results:
                total_reviews = row['cnt']

            true_user_score = round((total_reviews_positive / total_reviews) * 100, 0)

            overall_results.append({
                'product_id': product_id,
                'true_user_score': true_user_score
            })

            error = False
        except Exception, e:
            print "Timed out on {0}, trying again.".format(product_id)

print "Finally"
print overall_results
print len(overall_results)