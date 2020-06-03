''' raw game schema '''
from marshmallow import Schema, fields, pre_load
from marshmallow_schemas.schema_utils import Info, Person, Team, Position


# -------------- SCHEDULE --------------

class RawScheduleGameStatus(Schema):
    abstractGameState = fields.Str()
    codedGameState = fields.Integer()
    detailedState = fields.Str()
    statusCode = fields.Integer()
    startTimeTBD = fields.Boolean()


# -------------- TEAM --------------

class RawTeamDivision(Schema):
    nameShort = fields.Str()
    abbreviation = fields.Str()
    link = fields.Str()
    id = fields.Integer()
    name = fields.Str()


class RawTeamVenueTimezone(Schema):
    tz = fields.Str()
    id = fields.Str()
    offset = fields.Integer()


class RawTeamVenue(Schema):
    city = fields.Str()
    id = fields.Integer()
    link = fields.Str()
    name = fields.Str()
    timeZone = fields.Nested(RawTeamVenueTimezone)


# -------------- GAME --------------

class RawGameGameGame(Schema):
    pk = fields.Integer()
    season = fields.Integer()
    type = fields.Str()


# -------------- DATETIME --------------

class RawGameDatetime(Schema):
    dateTime = fields.DateTime()
    endDateTime = fields.DateTime()


# -------------- TEAMS --------------

class RawGameFranchise(Schema):
    franchiseId = fields.Integer()
    teamName = fields.Str()
    link = fields.Str()


class RawGameTeam(Schema):
    id = fields.Integer()
    name = fields.Str()
    link = fields.Str()
    venue = fields.Nested(RawTeamVenue)
    abbreviation = fields.Str()
    triCode = fields.Str()
    teamName = fields.Str()
    locationName = fields.Str()
    firstYearOfPlay = fields.Integer()
    division = fields.Nested(RawTeamDivision)
    conference = fields.Nested(Info)
    franchise = fields.Nested(RawGameFranchise)
    shortName = fields.Str()
    officialSiteUrl = fields.Str()
    franchiseId = fields.Integer()
    active = fields.Boolean()


class RawGameTeams(Schema):
    home = fields.Nested(RawGameTeam)
    away = fields.Nested(RawGameTeam)


# -------------- PLAYERS --------------

class RawGamePlayer(Schema):
    id = fields.Integer()
    fullName = fields.Str()
    link = fields.Str()
    firstName = fields.Str()
    lastName = fields.Str()
    primaryNumber = fields.Integer()
    birthDate = fields.Date()
    currentAge = fields.Integer()
    birthCity = fields.Str()
    birthStateProvince = fields.Str()
    birthCountry = fields.Str()
    nationality = fields.Str()
    height = fields.Str()
    weight = fields.Integer()
    active = fields.Boolean()
    alternateCaptain = fields.Boolean()
    captain = fields.Boolean()
    rookie = fields.Boolean()
    shootsCatches = fields.Str()
    rosterStatus = fields.Str()
    currentTeam = fields.Nested(Team)
    primaryPosition = fields.Nested(Position)


# -------------- GAME --------------

class RawGameGame(Schema):
    game = fields.Nested(RawGameGameGame)
    datetime = fields.Nested(RawGameDatetime)
    status = fields.Nested(RawScheduleGameStatus)
    teams = fields.Nested(RawGameTeams)
    players = fields.Nested(RawGamePlayer, many=True)
    venue = fields.Nested(Info)

    @pre_load
    def preload_players(self, data, **kwargs):
        data["players"] = [x for x in data["players"].values()]
        return data
