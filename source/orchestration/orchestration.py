"""
:author: Josh Hills

Define the public entryway to the
microservice architecture.
"""

import flask
import shared.messaging
import shared.database

# Global fields
app = flask.Flask(__name__)
messaging = shared.messaging.RabbitMQMessaging()
database = shared.database.Couchbase()

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
    500 if request fails.
    """

    # Add to queue for review microservice.
    messaging.publish_message("review_queue", product_id)

    # Add to queue for store microservice.


    # Add to queue for update microservice.

    # Store in database.

    # Return response
    response_str = "Product {0} added to work queue for scraping".format(product_id)
    return flask.Response(
        response=response_str, status=200, mimetype="text/html"
    )


# Run the service
if __name__ == "__main__":
    app.run()
