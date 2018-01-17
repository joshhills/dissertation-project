"""
:author: Josh Hills

Encapsulate interactions with a database.
"""

from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator


class Database:
    def store_job_state(self, product_id):
        """
        Log that scraping for a product has begun.

        :param product_id:
        """
        raise NotImplementedError("Class %s doesn't implement from_json()" % self.__class__.__name__)


class Couchbase(Database):
    def __init__(self):
        # Define connection parameters.
        authenticator = PasswordAuthenticator('root', 'administrator')

        self.cluster = Cluster('couchbase://localhost')
        self.cluster.authenticate(authenticator=authenticator)

    def store_job_state(self, product_id):
        cluster = self.cluster.open_bucket('job')

        # Learn how to do things with this.
        return

