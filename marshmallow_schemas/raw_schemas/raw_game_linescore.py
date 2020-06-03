''' raw linescore schema '''
from marshmallow import Schema, fields
from marshmallow_schemas.schema_utils import Team

# -------------- PERIODS --------------

class RawLinescorePeriodTeam(Schema):
    goals = fields.Integer()
    shotsOnGoal = fields.Integer()
    rinkSide = fields.Str()


class RawLinescorePeriod(Schema):
    periodType = fields.Str()
    startTime = fields.DateTime()
    endTime = fields.DateTime()
    num = fields.Integer()
    ordinalNum = fields.Str()
    home = fields.Nested(RawLinescorePeriodTeam)
    away = fields.Nested(RawLinescorePeriodTeam)


# -------------- SHOOTOUT INFO --------------

class RawLinescoreShootoutInfoTeam(Schema):
    scores = fields.Integer()
    attempts = fields.Integer()


class RawLinescoreShootoutInfo(Schema):
    away = fields.Nested(RawLinescoreShootoutInfoTeam)
    home = fields.Nested(RawLinescoreShootoutInfoTeam)
    startTime = fields.DateTime()


# -------------- TEAMS --------------

class RawLinescoreTeam(Schema):
    team = fields.Nested(Team)
    goals = fields.Integer()
    shotsOnGoal = fields.Integer()
    goaliePulled = fields.Boolean()
    numSkaters = fields.Integer()
    powerPlay = fields.Boolean()


class RawLinescoreTeams(Schema):
    home = fields.Nested(RawLinescoreTeam)
    away = fields.Nested(RawLinescoreTeam)


# -------------- INTERMISSION INFO --------------

class RawLinescoreIntermissionInfo(Schema):
    inIntermission = fields.Boolean()
    intermissionTimeRemaining = fields.Integer()
    intermissionTimeElapsed = fields.Integer()
    isIntermission = fields.Boolean()


# -------------- POWER PLAY INFO --------------

class RawLinescorePowerPlayInfo(Schema):
    situationTimeRemaining = fields.Integer()
    situationTimeElapsed = fields.Integer()
    inSituation = fields.Boolean()


# -------------- LINESCORE --------------

class RawLinescore(Schema):
    currentPeriod = fields.Integer()
    currentPeriodOrdinal = fields.Str()
    currentPeriodTimeRemaining = fields.Str()
    periods = fields.List(fields.Nested(RawLinescorePeriod))
    shootoutInfo = fields.Nested(RawLinescoreShootoutInfo)
    teams = fields.Nested(RawLinescoreTeams)
    powerPlayStrength = fields.Str()
    hasShootout = fields.Boolean()
    intermissionInfo = fields.Nested(RawLinescoreIntermissionInfo)
    powerPlayInfo = fields.Nested(RawLinescorePowerPlayInfo)
