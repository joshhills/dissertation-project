# Grunt task worker to initiate specific bespoke tasks.

import shared.database

db = shared.database.Couchbase(host="couchbase://128.199.62.177")

product_ids_results = db.run_query('select product_id from job', 'job')

overall_results = []

for row1 in product_ids_results:

    product_id = row1['product_id']

    print "Working on " + product_id

    error = True
    results = []
    while error:
        try:
            results = db.run_query('select raw max([votes_up, {product_id, votes_up, voted_up}])[1] from review where product_id = "' + str(product_id) + '"', 'job')

            for row in results:
                results_object = {
                    'product_id': row['product_id'],
                    'votes_up': row['votes_up'],
                    'voted_up': row['voted_up']
                }

            print results_object
            print '=-=-=-=-=-=-=-=-=-=-=-='

            overall_results.append(results_object)

            error = False
        except Exception, e:
            print "Timed out on {0}, trying again.".format(product_id)

print "Finally"
print overall_results
