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

msg = messaging.RabbitMQMessaging(host='messaging')
db = database.Couchbase(host=config.database['host'])
job_bucket = db.get_connection('job')
review_bucket = db.get_connection('review')

def is_desired_application_review(application_review):
    """
    Some reviews may be irrelevant based
    on aspects of the context of their decision.

    Make a decision as to whether or not
    a review should be kept.

    :param ApplicationReview application_review: The review in question.

    :return:
    True if the review should be stored.
    """
    return True


def begin_scraping(channel, method, properties, body):
    """
    Begin scraping a product in response to an object
    being added to the work queue for this microservice.

    :param body: The contents of the message.
    """

    print "Received message {0}".format(body)

    # Convert body into object in memory for ease-of-use.
    product_id = body

    # Control iteration over API.
    reviews_per_page = 20
    page_offset = 0

    # Get the number of items present in response data.
    while True:
        # Make a request for the necessary information.
        request_url = config.api_url.format(product_id, reviews_per_page * page_offset)
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
            if is_desired_application_review(application_review):
                # Store it in the database.
                db.store_application_review(application_review, review_bucket)

        page_offset += 1

    # Log that work has finished.
    js = db.get_job_state(product_id)
    js.review_finished = True
    db.store_job_state(js, job_bucket)


def register_subscribers():
    """
    Listen to the message queue.
    """

    print "Registering subscribers"

    msg.add_subscriber(
        config.messaging['queues']['work_review'],
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
