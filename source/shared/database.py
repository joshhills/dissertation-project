"""
:author: Josh Hills

Encapsulate interactions with a database.
"""

from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
from couchbase.exceptions import NotFoundError
from model import JobState

class Database:
    def store_job_state(self, job_state):
        """
        Log that scraping for a product has begun.

        :param job_state:
        A JobState object representative of the work.

        :param finished:
        Boolean dictating whether the job has been finished.
        """
        raise NotImplementedError("Class %s doesn't implement store_job_state()" % self.__class__.__name__)

    def get_job_state(self, product_id):
        """
        Get the state of a job for a specific product.

        :param product_id:
        The unique identifier for the product to serve as key.

        :return:
        A JobState object representative of the work, or None if it does not exist.
        """
        raise NotImplementedError("Class %s doesn't implement get_job_state()" % self.__class__.__name__)


class Couchbase(Database):
    def __init__(self):
        # Define connection parameters.
        authenticator = PasswordAuthenticator('root', 'administrator')

        self.cluster = Cluster('couchbase://localhost')
        self.cluster.authenticate(authenticator=authenticator)

    def store_job_state(self, job_state):
        cluster = self.cluster.open_bucket('job')

        cluster.upsert(
            key=job_state.product_id,
            value=job_state.to_json()
        )

    def get_job_state(self, product_id):
        cluster = self.cluster.open_bucket('job')

        try:
            response = cluster.get(product_id)
            return JobState(response.value)
        except NotFoundError:
            return None
