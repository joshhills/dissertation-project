"""
:author: Josh Hills

Microservice to scrape store page information from Steam API.
Uses 'competing consumers' design pattern.
"""

import config
import urllib
import json
from shared import messaging
from shared import database
from shared.model import ApplicationStore

msg = messaging.RabbitMQMessaging(host='messaging')
db = database.Couchbase(host=config.database['host'])
store_bucket = db.get_connection('store')
job_bucket = db.get_connection('job')


def begin_scraping(channel, method, properties, body):
    """
    Begin scraping a product in response to an object
    being added to the work queue for this microservice.

    :param body: The contents of the message.
    """

    print "Received message {0}".format(body)

    # Convert body into object in memory for ease-of-use.

    product_id = body

    # Make request for information.
    request_url = config.api_url.format(product_id)
    data = json.loads(urllib.urlopen(request_url).read())

    data = data[product_id]["data"]

    application_store = ApplicationStore(data)

    db.store_application_store(application_store, store_bucket)

    # Log that work has finished.
    js = db.get_job_state(product_id)
    js.store_finished = True
    db.store_job_state(js, job_bucket)


def register_subscribers():
    """
    Listen to the message queue.
    """

    print "Registering subscribers"

    msg.add_subscriber(
        config.messaging['queues']['work_store'],
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
