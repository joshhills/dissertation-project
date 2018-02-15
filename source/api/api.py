"""
:author: Josh Hills

Define the public entryway to the
microservice architecture.

Documentation auto-generated at '/api'.
No need for CRUD, simple RESTful tasks.
"""

import config
import json
from flask import Flask, request
from flask_restplus import Api, Resource
from shared import database
from shared import messaging
from shared.model import JobState

# Global fields
app = Flask(__name__)
msg = messaging.RabbitMQMessaging()
db = database.Couchbase()
job_bucket = db.get_connection('job')

# Define API
api = Api(
    app,
    version=config.app['version'],
    title=config.app['title'],
    description=config.app['description'],
    doc=config.app['documentation_url']
)

# TODO: Split into a child package.
ons = api.namespace(
    name='Orchestration',
    description='The public entryway to the microservice architecture.',
    path='/orchestration'
)


@ons.route('/scrape/<string:product_id>', endpoint='scrape')
@api.param('product_id', 'The unique id of the product on Steam.')
@api.param('update_feedname', 'Optional feed_name to filter news items as product updates.')
class ScrapeProduct(Resource):

    @api.response(200, 'Added to work queue.')
    @api.response(202, 'Already added to work queue.')
    def get(self, product_id):
        """
        Add product to work queues to scrape its information.
        """

        # Get extra arguments.
        update_feedname = request.args.get('update_feedname')
        if update_feedname is None:
            update_feedname = -1

        # Check if job has already been queued
        job_state = db.get_job_state(product_id)

        if job_state is not None:
            response_str = "Product {0} already processing.".format(product_id)
            return response_str, 202

        # Store in database
        job_state = JobState(product_id=product_id)
        db.store_job_state(job_state, job_bucket)

        # Add to queue for review microservice
        # msg.publish_message(config.messaging['queues']['work_review'], product_id)

        # Add to queue for store microservice
        msg.publish_message(config.messaging['queues']['work_store'], product_id)

        # Add to queue for update microservice
        # msg.publish_message(config.messaging['queues']['work_update'], json.dumps(
        #     {
        #         'product_id': product_id,
        #         'update_feedname': update_feedname
        #     }
        # ))

        # Return response
        response_str = "Product {0} added to work queue for scraping".format(product_id)
        return response_str, 200


# TODO: Provoke individual jobs.

# Run the service
if __name__ == '__main__':
    app.run(
        debug=config.app['debug'],
        port=int(config.app['port'])
    )
