''' utils and common Marshmallow Schemas '''
from marshmallow import Schema, fields

class Info(Schema):
    ''' generic info field; useful when, e.g., a team dict is nested in a field '''
    link = fields.Str()
    id = fields.Integer()
    name = fields.Str()


class Person(Schema):
    ''' generic person schema; useful for players, officials, etc. '''
    fullName = fields.Str()
    id = fields.Integer()
    link = fields.Str()


class Position(Schema):
    ''' generic positoin schema; useful for players, coaches, etc. '''
    abbreviation = fields.Str()
    code = fields.Str()
    name = fields.Str()
    type = fields.Str()


class Team(Schema):
    ''' generic team schema; useful in multiple places such as boxscore '''
    abbreviation = fields.Str()
    id = fields.Integer()
    link = fields.Str()
    name = fields.Str()
    triCode = fields.Str()
