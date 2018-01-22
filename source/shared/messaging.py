"""
:author: Josh Hills

Encapsulate interactions with a message queue.
"""

import pika

# Define an interface
class Messaging:
    def publish_message(self, queue, body):
        """
        Publish a message to a queue.

        :param queue:
        The name of the queue as a string.

        :param body:
        The contents of the message
        """
        raise NotImplementedError("Class %s doesn't implement from_json()" % self.__class__.__name__)


class RabbitMQMessaging(Messaging):
    def __init__(self, host='localhost'):
        # Define connection parameters.
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()

    def publish_message(self, queue, body):
        # Assert the queue's existence
        self.channel.queue_declare(queue=queue, durable=True)

        # Publish the message
        self.channel.basic_publish(
            exchange="",
            routing_key=queue,
            body=body,
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
