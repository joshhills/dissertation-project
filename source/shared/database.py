"""
:author: Josh Hills

Encapsulate interactions with a database.
"""

from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
from couchbase.exceptions import NotFoundError
from couchbase import FMT_UTF8
from model import JobState


class Database:
    def store_job_state(self, job_state):
        """
        Log that scraping for a product has begun.

        :param job_state:
        A JobState object representative of the work.
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

    def store_application_review(self, application_review):
        """
        Store a review for an application.

        :param application_review:
        The ApplicationReview that has been parsed and tested.
        """

class Couchbase(Database):
    def __init__(self, username='root', password='administrator', host='couchbase://localhost'):
        # Define connection parameters.
        authenticator = PasswordAuthenticator(username, password)

        self.cluster = Cluster(host)
        self.cluster.authenticate(authenticator=authenticator)

    def store_job_state(self, job_state):
        # Access the correct cluster.
        # TODO: Create cluster if not created.
        cluster = self.cluster.open_bucket('job')

        cluster.upsert(
            key=job_state.product_id,
            value=job_state.to_json(),
            format=FMT_UTF8
        )

    def get_job_state(self, product_id):
        # Access the correct cluster.
        # TODO: Create cluster if not created.
        cluster = self.cluster.open_bucket('job')

        try:
            response = cluster.get(product_id)
            return JobState(response.value)
        except NotFoundError:
            return None

    def store_application_review(self, application_review):
        # Access the correct cluster.
        # TODO: Create cluster if not created.
        cluster = self.cluster.open_bucket('review')

        cluster.upsert(
            key=application_review.recommendation_id,
            value=application_review.to_json(),
            format=FMT_UTF8
        )
