"""
:author: Josh Hills

Encapsulate messaging interactions
to facilitate uncoupled microservice
communication.
"""

import pika

class Messaging:
    """
    Define an interface that is both a consumer
    and a publisher to a message queue.
    """

    def start_consuming(self):
        """
        Being publishing/consuming.
        """
        raise NotImplementedError("Class %s doesn't implement start_consuming()" % self.__class__.__name__)

    def stop_consuming(self):
        """
        Stop publishing/consuming.
        """
        raise NotImplementedError("Class %s doesn't implement stop_consuming()" % self.__class__.__name__)

    def publish_message(self, queue, body):
        """
        Publish a message to a queue.

        :param queue:
        The name of the queue as a string.

        :param body:
        The contents of the message
        """
        raise NotImplementedError("Class %s doesn't implement publish_message()" % self.__class__.__name__)

    def add_subscriber(self, queue, callback):
        """
        Register interest in a message queue.
        :return:
        """
        raise NotImplementedError("Class %s doesn't implement add_subscriber()" % self.__class__.__name__)


class RabbitMQMessaging(Messaging):
    def __init__(self, host='localhost'):
        # Define connection parameters.
        self.connection = pika.SelectConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()

    def start_consuming(self):
        self.connection.ioloop.start()

    def stop_consuming(self):
        self.connection.ioloop.stop()

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

    def add_subscriber(self, queue, callback):
        self.channel.basic_consume(
            callback,
            queue=queue,
            no_ack=True
        )
