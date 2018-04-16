# Grunt task worker to initiate specific bespoke tasks.
from __future__ import division

import shared.database
import json
import ast
import numpy

db = shared.database.Couchbase(host="couchbase://128.199.62.177")

product_ids_results = db.run_query('select product_id from job', 'job')

overall_results = []

for row1 in product_ids_results:

    product_id = row1['product_id']

    print "Working on " + product_id

    error = True

    while error:
        try:
            ccu_values = []
            mean_ccu = -1
            median_ccu = -1
            stddev_ccu = -1
            max_ccu = -1
            min_ccu = -1
            start_ccu = -1
            end_ccu = -1
            mean_first_half = -1
            mean_second_half = -1
            num_days = -1

            results = db.run_query(
                'select `values` from `usage` where product_id="' + str(product_id) + '"',
                'job')

            for row in results:
                ccu_values = ast.literal_eval(row['values'])

            # Sanitize it.
            for i in range(len(ccu_values)):
                if ccu_values[i] is None:
                    ccu_values[i] = 0

            mean_ccu = numpy.mean(ccu_values)
            median_ccu = numpy.median(ccu_values)
            stddev_ccu = numpy.std(ccu_values)
            max_ccu = numpy.amax(ccu_values)
            min_ccu = numpy.amin(ccu_values)
            start_ccu = ccu_values[0]
            end_ccu = ccu_values[len(ccu_values) - 1]
            num_days = len(ccu_values)

            mean_first_half = numpy.mean(ccu_values[:len(ccu_values)//2])
            mean_second_half = numpy.mean(ccu_values[len(ccu_values) // 2:])

            overall_results.append({
                'product_id': product_id,
                'mean_ccu': mean_ccu,
                'median_ccu': median_ccu,
                'stddev_ccu': stddev_ccu,
                'max_ccu': max_ccu,
                'min_ccu': min_ccu,
                'mean_first_half': mean_first_half,
                'mean_second_half': mean_second_half,
                'start_ccu': start_ccu,
                'end_ccu': end_ccu,
                'num_days': num_days
            })

            error = False
        except Exception, e:
            print "Timed out on {0}, trying again.".format(product_id)

print "Finally"
print overall_results
print len(overall_results)