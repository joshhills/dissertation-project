# Grunt task worker to initiate specific bespoke tasks.

from couchbase.n1ql import N1QLQuery

import urllib
import time
import shared.database
import cfscrape

sleep_time = 5

scraper = cfscrape.create_scraper()
db = shared.database.Couchbase(host="couchbase://128.199.62.177")

bucket = db.cluster.open_bucket('job')
q = N1QLQuery('select * from job where review_finished = true and store_finished = true and update_finished = true and usage_finished is missing')
results = bucket.n1ql_query(q)

for row in results:
    product_id = row['job']['product_id']

    request_url = "http://128.199.62.177:8888/orchestration/scrape/usage/{0}".format(product_id)

    print "Making request to: '{0}'".format(request_url)

    urllib.urlopen(request_url)

    print "Sleeping for {0} seconds...".format(sleep_time)
    time.sleep(sleep_time)
