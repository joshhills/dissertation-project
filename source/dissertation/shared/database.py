"""
:author: Josh Hills

Encapsulate interactions with a database.
"""

from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
from couchbase.exceptions import NotFoundError
from couchbase.n1ql import N1QLQuery
from couchbase import FMT_UTF8
from model import JobState


class Database:
    def store_job_state(self, job_state, where):
        """
        Log that scraping for a product has begun.

        :param job_state:
        A JobState object representative of the work.
        """

        raise NotImplementedError("Class %s doesn't implement store_job_state()" % self.__class__.__name__)

    def store_application_review(self, application_review, where):
        """
        Store a review for an application.

        :param shared.model.ApplicationReview application_review:
        The review that has been parsed and tested.
        """
        raise NotImplementedError("Class %s doesn't implement store_application_review()" % self.__class__.__name__)

    def store_application_update(self, application_update, where):
        """
        Store an update for an application.

        :param shared.model.ApplicationUpdate application_update:
        The update that has been parsed and tested.
        """
        raise NotImplementedError("Class %s doesn't implement store_application_update()" % self.__class__.__name__)

    def store_application_store(self, application_store, where):
        """
        Store store-page information for an application.

        :param shared.model.ApplicationStore application_store:
        The update that has been parsed and tested.
        """
        raise NotImplementedError("Class %s doesn't implement store_application_store()" % self.__class__.__name__)

    def store_application_usage(self, application_usage, where):
        """
        Store forever-daily CCU for an application.

        :param shared.model.ApplicationUsage application_usage:
        The update that has been parsed and tested.
        """
        raise NotImplementedError("Class %s doesn't implement store_application_usage()" % self.__class__.__name__)

    def get_job_state(self, product_id):
        """
        Get the state of a job for a specific product.

        :param product_id:
        The unique identifier for the product to serve as key.

        :return:
        A JobState object representative of the work, or None if it does not exist.
        """
        raise NotImplementedError("Class %s doesn't implement get_job_state()" % self.__class__.__name__)

    def run_query(self, query, name):
        """
        Run a generic query without interfacing
        with specific library methods as a catch-all.

        :param query: The query string to execute.
        :param name: The name of the database table/cluster to perform the query on.

        :return:
        The response from the database.
        """
        raise NotImplementedError("Class %s doesn't implement run_query()" % self.__class__.__name__)

    def get_connection(self, database_name):
        """
        Open a connection with an aspect of the data base
        (representation dependent).

        :param database_name: The unique identifier of the cluster.
        :return: A connection to a data store.
        """
        raise NotImplementedError("Class %s doesn't implement get_connection()" % self.__class__.__name__)


class Couchbase(Database):
    def __init__(self, username='root', password='administrator', host='couchbase://localhost'):
        # Define connection parameters.
        authenticator = PasswordAuthenticator(username, password)

        self.cluster = Cluster(host)
        self.cluster.authenticate(authenticator=authenticator)
        self.last_active_bucket = None

    def store_job_state(self, job_state, where):
        # Access the correct cluster.
        where.upsert(
            key=job_state.product_id,
            value=job_state.to_json(),
            format=FMT_UTF8
        )

    def get_job_state(self, product_id):
        # Access the correct cluster.
        self.last_active_bucket = self.cluster.open_bucket('job')

        try:
            response = self.last_active_bucket.get(product_id)
            return JobState(response.value)
        except NotFoundError:
            return None

    def store_application_review(self, application_review, where):
        # Access the correct cluster.
        where.upsert(
            key=application_review.recommendation_id,
            value=application_review.to_json(),
            format=FMT_UTF8
        )

    def store_application_update(self, application_update, where):
        # Access the correct cluster.
        where.upsert(
            key=application_update.update_id,
            value=application_update.to_json(),
            format=FMT_UTF8
        )

    def store_application_store(self, application_store, where):
        # Access the correct cluster.
        where.upsert(
            key=application_store.product_id,
            value=application_store.to_json(),
            format=FMT_UTF8
        )

    def store_application_usage(self, application_usage, where):
        # Access the correct cluster.
        where.upsert(
            key=application_usage.product_id,
            value=application_usage.to_json(),
            format=FMT_UTF8
        )

    def run_query(self, query, name):
        self.last_active_bucket = self.cluster.open_bucket(name)
        self.last_active_bucket.n1ql_timeout = 900.0
        q = N1QLQuery(query)
        results = self.last_active_bucket.n1ql_query(q)
        return results

    def get_connection(self, cluster_id):
        self.last_active_bucket = self.cluster.open_bucket(cluster_id)
        return self.last_active_bucket
