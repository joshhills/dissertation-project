"""
:author: Josh Hills

Microservice to scrape reviews from Steam API.
Uses 'competing consumers' design pattern.
"""

import config
from shared import messaging

msg = messaging.RabbitMQMessaging()


def begin_scraping(channel, method, properties, body):
    """
    Begin scraping a product in response to an object
    being added to the work queue for this microservice.

    :param channel:
    :param method:
    :param properties:
    :param body:
    """

    # Convert body into object in memory for ease-of-use.
    print "Received message {0}".format(body);


def register_subscribers():
    """
    Listen to the message queue.
    """

    msg.add_subscriber(
        config.message_queue['queues']['work_review'],
        begin_scraping
    )


def main():
    """
    Run the microservice.
    """
    try:
        msg.start_consuming()
    except KeyboardInterrupt:
        msg.stop_consuming()

if __name__ == '__main__':
    main()
