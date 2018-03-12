# Grunt task worker to initiate specific bespoke tasks.

import shared.database

db = shared.database.Couchbase(host="couchbase://128.199.62.177")

product_ids_results = db.run_query('select product_id from job', 'job')

free_review_counts = []

for row1 in product_ids_results:
    product_id = row1['product_id']

    print "Working on " + product_id

    total_reviews = -1
    total_positive = -1
    total_free_reviews = -1
    total_free_positive = -1

    total_free_reviews_results = db.run_query(
        'select count(*) as cnt from review where product_id = "{0}" and received_for_free = true'.format(product_id),
        'job'
    )

    for row2 in total_free_reviews_results:
        total_free_reviews = int(row2['cnt'])

    if total_free_reviews < 1:
        print "Product " + product_id + " has no free reviews"
        continue

    total_reviews_results = db.run_query(
        'select count(*) as cnt from review where product_id = "{0}"'.format(product_id),
        'job'
    )

    for row2 in total_reviews_results:
        total_reviews = row2['cnt']

    total_positive_reviews_results = db.run_query(
        'select count(*) as cnt from review where product_id = "{0}" and voted_up = true'.format(product_id),
        'job'
    )

    for row2 in total_positive_reviews_results:
        total_positive = row2['cnt']

    total_free_positive_results = db.run_query(
        'select count(*) as cnt from review where product_id = "{0}" and voted_up = true and received_for_free = true'.format(product_id),
        'job'
    )

    for row2 in total_free_positive_results:
        total_free_positive = row2['cnt']

    # Finally, build object...
    results_object = {
        "product_id": product_id,
        "total_reviews": total_reviews,
        "total_reviews_positive": total_positive,
        "total_reviews_negative": total_reviews - total_positive,
        "total_reviews_purchased": total_reviews - total_free_reviews,
        "total_reviews_purchased_positive": total_positive - total_free_positive,
        "total_reviews_purchased_negative": (total_reviews - total_free_reviews) - (total_positive - total_free_positive),
        "total_reviews_free": total_free_reviews,
        "total_reviews_free_positive": total_free_positive,
        "total_reviews_free_negative": total_free_reviews - total_free_positive
    }

    print results_object
    print '=-=-=-=-=-=-=-=-=-=-=-='

    free_review_counts.append(results_object)

print "Finally"
print free_review_counts
