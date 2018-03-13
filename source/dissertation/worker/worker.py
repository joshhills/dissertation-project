# Grunt task worker to initiate specific bespoke tasks.

import shared.database

db = shared.database.Couchbase(host="couchbase://127.0.0.1")

product_ids_results = db.run_query('select product_id from job', 'job')

playtime_and_upvotes = []

for row1 in product_ids_results:
    product_id = row1['product_id']

    print "Working on " + product_id

    error = True
    results = []
    while error:
        try:
            results = db.run_query('select raw max([t.distinct_average_votes_up, {t.distinct_average_votes_up, t.author_total_playtime}])[1] from (select author_total_playtime, avg(distinct votes_up) as distinct_average_votes_up from review where product_id = "' + str(product_id) + '" group by author_total_playtime) t', 'job')

            for row in results:
                results_object = {
                    'author_total_playtime': row['author_total_playtime'],
                    'distinct_average_votes_up': row['distinct_average_votes_up']
                }

            print results_object
            print '=-=-=-=-=-=-=-=-=-=-=-='

            playtime_and_upvotes.append(results_object)

            error = False
        except Exception, e:
            print "Timed out on {0}, trying again.".format(product_id)

print "Finally"
print playtime_and_upvotes
