"""
:author: Josh Hills

Microservice to scrape reviews from Steam API.
Uses 'competing consumers' design pattern.
"""

import config
import urllib
import json
from shared import messaging
from shared import database
from shared.model import ApplicationReview
import shared.model

msg = messaging.RabbitMQMessaging()
db = database.Couchbase()

def is_desired_application_review():
    return True

def begin_scraping(channel, method, properties, body):
    """
    Begin scraping a product in response to an object
    being added to the work queue for this microservice.

    :param channel:
    :param method:
    :param properties:
    :param body:
    """

    print "Received message {0}".format(body)

    # Convert body into object in memory for ease-of-use.
    product_id = body

    # Control iteration over API.
    REVIEWS_PER_PAGE = 20
    i = 1

    # Get the number of items present in response data.
    while True:
        # Make a request for the necessary information.
        request_url = config.api_url.format(product_id, 0)
        data = json.loads(urllib.urlopen(request_url).read())

        num_reviews = int(data[shared.model.FIELD_QUERY_SUMMARY][shared.model.FIELD_NUM_REVIEWS])

        # Check for end of reviews.
        if num_reviews == 0:
            break

        # Iterate over reviews.
        for i in range(num_reviews):
            # Create object representation.
            application_review = ApplicationReview(data[shared.model.FIELD_REVIEWS][i])

            # Make a decision as to whether to keep it.
            if is_desired_application_review():
                # Store it in the database.
                db.store_application_review(application_review)

        i += 1

def register_subscribers():
    """
    Listen to the message queue.
    """

    print "Registering subscribers"

    msg.add_subscriber(
        config.message_queue['queues']['work_review'],
        begin_scraping
    )


def main():
    """
    Run the microservice.
    """
    print "Starting review microservice"

    register_subscribers()

    try:
        msg.start_consuming()
    except KeyboardInterrupt:
        msg.stop_consuming()


if __name__ == '__main__':
    main()
