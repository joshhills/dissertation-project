"""
:author: Josh Hills

Model loosely defined transactions.
"""

FIELD_PRODUCT_ID = "product_id"
FIELD_FINISHED = "finished"


class JobState:
    def __init__(self, blob=None, product_id=-1, finished=False):
        if blob is None:
            self.product_id = product_id
            self.finished = finished
        else:
            self.from_json(blob)

    def from_json(self, blob):
        self.product_id = blob[FIELD_PRODUCT_ID]
        self.finished = blob[FIELD_FINISHED]

        return self

    def to_json(self):
        return {
            FIELD_PRODUCT_ID: self.product_id,
            FIELD_FINISHED: self.finished
        }