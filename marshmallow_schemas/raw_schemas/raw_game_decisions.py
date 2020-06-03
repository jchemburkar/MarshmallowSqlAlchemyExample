''' raw decisions schema '''
from marshmallow import Schema, fields
from marshmallow_schemas.schema_utils import Person


class RawDecisions(Schema):
    winner = fields.Nested(Person)
    loser = fields.Nested(Person)
    firstStar = fields.Nested(Person)
    secondStar = fields.Nested(Person)
    thirdStar = fields.Nested(Person)
