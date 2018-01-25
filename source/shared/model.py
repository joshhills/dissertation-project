"""
:author: Josh Hills

Model loosely defined transactions.
"""

import json

# Define custom fields.
FIELD_PRODUCT_ID = "product_id"
FIELD_FINISHED = "finished"

# Define the constant field strings used to manipulate REST API JSON.
FIELD_QUERY_SUMMARY = 'query_summary'
FIELD_NUM_REVIEWS = 'num_reviews'
FIELD_REVIEWS = 'reviews'

FIELD_RECOMMENDATION_ID = 'recommendationid'
FIELD_LANGUAGE = 'language'
FIELD_REVIEW = 'review'
FIELD_DATE_CREATED = 'timestamp_created'
FIELD_VOTED_UP = 'voted_up'
FIELD_VOTES_UP = 'votes_up'
FIELD_VOTES_FUNNY = 'votes_funny'
FIELD_RECEIVED_FOR_FREE = 'received_for_free'
FIELD_WRITTEN_DURING_EARLY_ACCESS = 'written_during_early_access'

FIELD_AUTHOR = 'author'
FIELD_AUTHOR_ID = 'steamid'
FIELD_AUTHOR_NUM_GAMES_OWNED = 'num_games_owned'
FIELD_AUTHOR_NUM_REVIEWS = 'num_reviews'
FIELD_AUTHOR_TOTAL_PLAYTIME = 'playtime_forever'
FIELD_AUTHOR_LAST_PLAYED = 'last_played'


# Define a loose interface for objects consumed RESTfully.
class JSONAPIResource:
    def from_json(self, blob):
        """Convert object from JSON or dictionary."""
        raise NotImplementedError("Class %s doesn't implement from_json()" % self.__class__.__name__)

    def to_json(self):
        """Convert object to JSON encoded string."""
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __str__(self):
        return self.to_json()


class JobState(JSONAPIResource):
    def __init__(self, blob=None, product_id=-1, finished=False):
        if blob is None:
            self.product_id = product_id
            self.finished = finished
        else:
            self.from_json(blob)

    def from_json(self, blob):
        # Convert JSON encoded string into dictionary.
        blob = json.loads(blob)

        self.product_id = blob[FIELD_PRODUCT_ID]
        self.finished = blob[FIELD_FINISHED]

        return self


# Class to store review information in-memory.
class ApplicationReview(JSONAPIResource):
    # Constructor equivalent.
    def __init__(self, blob=None):
        # Store the decoded JSON dictionary internally for posterity.
        # self.blob = blob

        if blob is None:
            # Review meta.
            self.recommendation_id = None
            self.language = None
            self.review_length = None
            self.date_created = None
            self.voted_up = None
            self.votes_up = None
            self.votes_funny = None
            self.received_for_free = None
            self.written_during_early_access = None

            # Author meta (flattened here).
            self.author_id = None
            self.author_num_games_owned = None
            self.author_num_reviews = None
            self.author_total_playtime = None
            self.author_last_played = None
        else:
            self.from_json(blob)

    def from_json(self, blob):
        # Review meta.
        self.recommendation_id = blob[FIELD_RECOMMENDATION_ID]
        self.language = blob[FIELD_LANGUAGE]
        self.review_length = len(blob[FIELD_REVIEW])
        self.date_created = blob[FIELD_DATE_CREATED]
        self.voted_up = blob[FIELD_VOTED_UP]
        self.votes_up = blob[FIELD_VOTES_UP]
        self.votes_funny = blob[FIELD_VOTES_FUNNY]
        self.received_for_free = blob[FIELD_RECEIVED_FOR_FREE]
        self.written_during_early_access = blob[FIELD_WRITTEN_DURING_EARLY_ACCESS]

        # Author meta (flattened here).
        self.author_id = blob[FIELD_AUTHOR][FIELD_AUTHOR_ID]
        self.author_num_games_owned = blob[FIELD_AUTHOR][FIELD_AUTHOR_NUM_GAMES_OWNED]
        self.author_num_reviews = blob[FIELD_AUTHOR][FIELD_AUTHOR_NUM_REVIEWS]
        self.author_total_playtime = blob[FIELD_AUTHOR][FIELD_AUTHOR_TOTAL_PLAYTIME]
        self.author_last_played = blob[FIELD_AUTHOR][FIELD_AUTHOR_LAST_PLAYED]

        return self