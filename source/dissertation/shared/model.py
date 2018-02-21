"""
:author: Josh Hills

Model loosely defined transactions.
"""

import json

# Define custom fields.
FIELD_PRODUCT_ID = "product_id"
FIELD_REVIEW_FINISHED = "review_finished"
FIELD_STORE_FINISHED = "store_finished"
FIELD_UPDATE_FINISHED = "update_finished"

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

FIELD_UPDATE_ID = 'gid'
FIELD_FEED_NAME = 'feedname'
FIELD_DATE = 'date'

FIELD_STEAM_APP_ID = 'steam_appid'
FIELD_APP_ID = 'appid'
FIELD_NAME = 'name'
FIELD_IS_FREE = 'is_free'
FIELD_METACRITIC_SCORE = 'metacritic'
FIELD_SCORE = 'score'
FIELD_GENRES = 'genres'
FIELD_DESCRIPTION = 'description'
FIELD_RELEASE_DATE = 'release_date'

FIELD_USER_SCORE = 'userscore'
FIELD_OWNERS = 'owners'
FIELD_PLAYERS_FOREVER = 'players_forever'
FIELD_PLAYERS_AVERAGE_FOREVER = 'average_forever'
FIELD_PLAYERS_MEDIAN_FOREVER = 'median_forever'
FIELD_SCORE_RANK = 'score_rank'
FIELD_PRICE = 'price'


# Define a loose interface for objects consumed RESTfully.
class JSONAPIResource:
    def from_json(self, blob):
        """Convert object from JSON or dictionary."""
        raise NotImplementedError("Class %s doesn't implement from_json()" % self.__class__.__name__)

    def to_json(self):
        """Convert object to JSON encoded string."""
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4, ensure_ascii=False)

    def __str__(self):
        return self.to_json()


class JobState(JSONAPIResource):
    def __init__(self, blob=None, product_id=-1, review_finished=False, store_finished=False, update_finished=False):
        if blob is None:
            self.product_id = product_id
            self.review_finished = review_finished
            self.store_finished = store_finished
            self.update_finished = update_finished
        else:
            self.from_json(blob)

    def from_json(self, blob):
        # Convert JSON encoded string into a dictionary.
        if isinstance(blob, basestring):
            blob = json.loads(blob)

        self.product_id = blob.get(FIELD_PRODUCT_ID, "-1")
        self.review_finished = blob.get(FIELD_REVIEW_FINISHED, "-1")
        self.store_finished = blob.get(FIELD_STORE_FINISHED, "-1")
        self.update_finished = blob.get(FIELD_UPDATE_FINISHED, "-1")

        return self


# Class to store review information in-memory.
class ApplicationReview(JSONAPIResource):
    # Constructor equivalent.
    def __init__(self, product_id = -1, blob=None):
        # Store the decoded JSON dictionary internally for posterity.
        # self.blob = blob
        self.product_id = product_id

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
        # Convert JSON encoded string into a dictionary.
        if isinstance(blob, basestring):
            blob = json.loads(blob)

        # Review meta.
        self.recommendation_id = blob.get(FIELD_RECOMMENDATION_ID, "-1")
        self.language = blob.get(FIELD_LANGUAGE, "-1")
        self.review_length = len(blob.get(FIELD_REVIEW, "-1"))
        self.date_created = blob.get(FIELD_DATE_CREATED, "-1")
        self.voted_up = blob.get(FIELD_VOTED_UP, "-1")
        self.votes_up = blob.get(FIELD_VOTES_UP, "-1")
        self.votes_funny = blob.get(FIELD_VOTES_FUNNY, "-1")
        self.received_for_free = blob.get(FIELD_RECEIVED_FOR_FREE, "-1")
        self.written_during_early_access = blob.get(FIELD_WRITTEN_DURING_EARLY_ACCESS, "-1")

        # Author meta (flattened here).
        self.author_id = blob.get(FIELD_AUTHOR, {}).get(FIELD_AUTHOR_ID, "-1")
        self.author_num_games_owned = blob.get(FIELD_AUTHOR, {}).get(FIELD_AUTHOR_NUM_GAMES_OWNED, "-1")
        self.author_num_reviews = blob.get(FIELD_AUTHOR, {}).get(FIELD_AUTHOR_NUM_REVIEWS, "-1")
        self.author_total_playtime = blob.get(FIELD_AUTHOR, {}).get(FIELD_AUTHOR_TOTAL_PLAYTIME, "-1")
        self.author_last_played = blob.get(FIELD_AUTHOR, {}).get(FIELD_AUTHOR_LAST_PLAYED, "-1")

        return self


# Class to store update information in memory.
class ApplicationUpdate(JSONAPIResource):
    # Constructor equivalent.
    def __init__(self, blob=None):
        # Store the decoded JSON dictionary internally for posterity.
        # self.blob = blob

        if blob is None:
            self.product_id = None
            self.update_id = None
            self.feed_name = None
            self.date_created = None
        else:
            self.from_json(blob)

    def from_json(self, blob):
        # Convert JSON encoded string into a dictionary.
        if isinstance(blob, basestring):
            blob = json.loads(blob)

        # Update meta.
        self.product_id = blob.get(FIELD_APP_ID, "-1")
        self.update_id = blob.get(FIELD_UPDATE_ID, "-1")
        self.feed_name = blob.get(FIELD_FEED_NAME, "-1")
        self.date_created = blob.get(FIELD_DATE, "-1")

        return self


# Class to store store information in memory.
class ApplicationStore(JSONAPIResource):
    # Constructor equivalent.
    def __init__(self, blob_1=None, blob_2=None):
        # Store the decoded JSON dictionary internally for posterity.
        # self.blob = blob

        if blob_1 is None or blob_2 is None:
            self.product_id = None
            self.name = None
            self.is_free = None
            self.metacritic_score = None
            self.genres = []
            self.date_released = None

            self.user_score = None
            self.owners = None
            self.players_forever = None
            self.players_average_forever = None
            self.players_median_forever = None
            self.score_rank = None
            self.price = None
        else:
            self.from_json(blob_1, blob_2)

    def from_json(self, blob_1, blob_2):
        # Convert JSON encoded string into a dictionary.
        if isinstance(blob_1, basestring):
            blob_1 = json.loads(blob_1)

        if isinstance(blob_2, basestring):
            blob_2 = json.loads(blob_2)

        self.product_id = str(blob_1.get(FIELD_STEAM_APP_ID, "-1"))
        self.name = blob_1.get(FIELD_NAME, "-1")
        self.is_free = blob_1.get(FIELD_IS_FREE, "-1")
        self.metacritic_score = blob_1.get(FIELD_METACRITIC_SCORE, {}).get(FIELD_SCORE, "-1")

        self.genres = []
        for genre in blob_1[FIELD_GENRES]:
            self.genres.append(genre.get(FIELD_DESCRIPTION, "-1"))

        self.date_released = blob_1.get(FIELD_RELEASE_DATE, {}).get(FIELD_DATE, "-1")

        self.user_score = blob_2.get(FIELD_USER_SCORE, "-1")
        self.owners = blob_2.get(FIELD_OWNERS, "-1")
        self.players_forever = blob_2.get(FIELD_PLAYERS_FOREVER, "-1")
        self.players_average_forever = blob_2.get(FIELD_PLAYERS_AVERAGE_FOREVER, "-1")
        self.players_median_forever = blob_2.get(FIELD_PLAYERS_MEDIAN_FOREVER, "-1")
        self.score_rank = blob_2.get(FIELD_SCORE_RANK, "-1")
        self.price = blob_2.get(FIELD_PRICE, "-1")

        return self
