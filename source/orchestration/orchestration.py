"""
:author: Josh Hills

Define the public entryway to the
microservice architecture.
"""

import config
import flask
from shared import database
from shared import messaging
from shared.model import JobState

# Global fields
app = flask.Flask(__name__)
msg = messaging.RabbitMQMessaging()
db = database.Couchbase()


# API
@app.route("/scrape/product/<product_id>")
def scrape_product(product_id):
    """
    Send messages to work queues of
    microservices related to scraping
    information about a specific product.

    :param product_id:
    The unique identifier for the product.

    :return:
    200 if request succeeds.
    202 if the job is already processing.
    500 if request fails.
    """

    # Check if job has already been queued
    job_state = db.get_job_state(product_id)

    if job_state is not None:
        response_str = "Product {0} already processing.".format(product_id)
        return flask.Response(
            response=response_str, status=202, mimetype="text/html"
        )

    # Store in database
    job_state = JobState(product_id=product_id)
    db.store_job_state(job_state)

    # Add to queue for review microservice
    msg.publish_message(config.message_queue['queues']['work_review'], product_id)

    # Add to queue for store microservice
    # msg.publish_message(config.message_queue['queues']['work_store'], product_id)

    # Add to queue for update microservice
    # msg.publish_message(config.message_queue['queues']['work_update'], product_id)

    # Return response
    response_str = "Product {0} added to work queue for scraping".format(product_id)
    return flask.Response(
        response=response_str, status=200, mimetype="text/html"
    )


# Run the service
if __name__ == "__main__":
    app.run()
