''' raw plays schema '''
from marshmallow import Schema, fields
from marshmallow_schemas.schema_utils import Person, Team, Position

# -------------- ALL PLAYS --------------

class RawPlayPlayer(Schema):
    playerType = fields.Str()
    player = fields.Nested(Person)
    seasonTotal = fields.Integer()


class RawPlayResultStrength(Schema):
    code = fields.Str()
    name = fields.Str()


class RawPlayResult(Schema):
    emptyNet = fields.Boolean()
    event = fields.Str()
    eventCode = fields.Str()
    eventTypeId = fields.Str()
    description = fields.Str()
    gameWinningGoal = fields.Boolean()
    penaltyMinutes = fields.Integer()
    penaltySeverity = fields.Str()
    secondaryType = fields.Str()
    strength = fields.Nested(RawPlayResultStrength)


class RawPlayAboutGoals(Schema):
    home = fields.Integer()
    away = fields.Integer()


class RawPlayAbout(Schema):
    eventIdx = fields.Integer()
    eventId = fields.Integer()
    period = fields.Integer()
    periodType = fields.Str()
    ordinalNum = fields.Str()
    periodTime = fields.Str()
    periodTimeRemaining = fields.Str()
    dateTime = fields.DateTime()
    goals = fields.Nested(RawPlayAboutGoals)


class RawPlayCoordinates(Schema):
    x = fields.Integer()
    y = fields.Integer()


class RawPlay(Schema):
    players = fields.List(fields.Nested(RawPlayPlayer))
    result = fields.Nested(RawPlayResult)
    about = fields.Nested(RawPlayAbout)
    coordinates = fields.Nested(RawPlayCoordinates)
    team = fields.Nested(Team)


# -------------- PLAYS BY PERIOD --------------

class RawPlaysByPeriod(Schema):
    startIndex = fields.Integer()
    plays = fields.List(fields.Integer)
    endIndex = fields.Integer()


# -------------- CURRENT PLAY --------------

class RawPlays(Schema):
    allPlays = fields.List(fields.Nested(RawPlay))
    scoringPlays = fields.List(fields.Integer)
    penaltyPlays = fields.List(fields.Integer)
    playsByPeriod = fields.List(fields.Nested(RawPlaysByPeriod))
    currentPlay = fields.Nested(RawPlay)
