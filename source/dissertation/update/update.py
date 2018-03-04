"""
:author: Josh Hills

Microservice to scrape news updates from Steam API.
Uses 'competing consumers' design pattern.
"""

import config
import urllib
import json
from shared import messaging
from shared import database
from shared.model import ApplicationUpdate

msg = messaging.RabbitMQMessaging(host=config.messaging['host'])
db = database.Couchbase(host=config.database['host'])
update_bucket = db.get_connection('update')
job_bucket = db.get_connection('job')


def is_desired_application_update(application_update, update_feedname):
    """
    Some reviews may be irrelevant based
    on aspects of the context of their decision.

    Make a decision as to whether or not
    a review should be kept.

    :param ApplicationReview application_review: The review in question.

    :return:
    True if the review should be stored.
    """
    if update_feedname != -1:
        return application_update.feed_name == update_feedname
    else:
        return True


def begin_scraping(channel, method, properties, body):
    """
    Begin scraping a product in response to an object
    being added to the work queue for this microservice.

    :param body: The contents of the message.
    """

    print "Received message {0}".format(body)

    # Convert body into object in memory for ease-of-use.
    body = json.loads(body)

    product_id = body['product_id']
    update_feedname = body['update_feedname']

    try:
        # Make initial request to get the number of updates posted.
        request_url = config.api_url.format(product_id, -1)
        data = json.loads(urllib.urlopen(request_url).read())
        update_count = int(data['appnews']['count'])

        # Make request for information.
        request_url = config.api_url.format(product_id, update_count)
        data = json.loads(urllib.urlopen(request_url).read())

        for i in range(update_count):
            update = ApplicationUpdate(product_id, data['appnews']['newsitems']['newsitem'][i])

            # Make a decision as to whether to keep it.
            if is_desired_application_update(update, update_feedname):
                # Store it in the database.
                db.store_application_update(update, update_bucket)

        # Log that work has finished.
        js = db.get_job_state(product_id)
        js.update_finished = True
        db.store_job_state(js, job_bucket)
    except Exception, e:
        print "Failed to retrieve update information for product {0}".format(product_id)


def register_subscribers():
    """
    Listen to the message queue.
    """

    print "Registering subscribers"

    msg.add_subscriber(
        config.messaging['queues']['work_update'],
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
