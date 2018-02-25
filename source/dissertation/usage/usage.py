"""
:author: Josh Hills

Microservice to scrape forever-daily CCU information from
SteamDB API.
Uses 'competing consumers' design pattern.
"""

import config
import cfscrape
import json
from shared import messaging
from shared import database
from shared.model import ApplicationUsage

msg = messaging.RabbitMQMessaging(host=config.messaging['host'])
db = database.Couchbase(host=config.database['host'])
usage_bucket = db.get_connection('usage')
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

    try:
        # Make request for information.
        scraper = cfscrape.create_scraper()
        data = json.loads(scraper.get(config.api_url.format(product_id)).content)['data']

        application_usage = ApplicationUsage(product_id, data)

        db.store_application_usage(application_usage, usage_bucket)

        # Log that work has finished.
        js = db.get_job_state(product_id)
        js.usage_finished = True
        db.store_job_state(js, job_bucket)
    except Exception, e:
        print "Failed to retrieve usage information for product {0}".format(product_id)


def register_subscribers():
    """
    Listen to the message queue.
    """

    print "Registering subscribers"

    msg.add_subscriber(
        config.messaging['queues']['work_usage'],
        begin_scraping
    )


def main():
    """
    Run the microservice.
    """
    print "Starting usage microservice"

    register_subscribers()

    try:
        msg.start_consuming()
    except KeyboardInterrupt:
        msg.stop_consuming()


if __name__ == '__main__':
    main()
