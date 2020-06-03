''' raw boxscore schema '''
from marshmallow import Schema, fields, pre_load
from marshmallow_schemas.schema_utils import Person, Team, Position


#############
# Officials #
#############

class RawOfficial(Schema):
    official = fields.Nested(Person)
    officialType = fields.Str()


#########
# Teams #
#########

# -------------- TEAM STATS --------------

class RawBoxscoreTeamSkaterStats(Schema):
    goals = fields.Integer()
    pim = fields.Integer()
    shots = fields.Integer()
    powerPlayPercentage = fields.Float()
    powerPlayGoals = fields.Integer()
    powerPlayOpportunities = fields.Integer()
    faceOffWinPercentage = fields.Float()
    blocked = fields.Integer()
    takeaways = fields.Integer()
    giveaways = fields.Integer()
    hits = fields.Integer()


class RawBoxscoreTeamStats(Schema):
    teamSkaterStats = fields.Nested(RawBoxscoreTeamSkaterStats)


# -------------- PLAYERS --------------

class RawBoxscorePlayerSkaterStats(Schema):
    timeOnIce = fields.Str()
    assists = fields.Integer()
    goals = fields.Integer()
    shots = fields.Integer()
    hits = fields.Integer()
    powerPlayGoals = fields.Integer()
    powerPlayAssists = fields.Integer()
    penaltyMinutes = fields.Integer()
    faceOffWins = fields.Integer()
    faceoffTaken = fields.Integer()
    faceOffPct = fields.Float()
    takeaways = fields.Integer()
    giveaways = fields.Integer()
    shortHandedGoals = fields.Integer()
    shortHandedAssists = fields.Integer()
    blocked = fields.Integer()
    plusMinus = fields.Integer()
    evenTimeOnIce = fields.Str()
    powerPlayTimeOnIce = fields.Str()
    shortHandedTimeOnIce = fields.Str()



class RawBoxscorePlayerGoalieStats(Schema):
    timeOnIce = fields.Str()
    assists = fields.Integer()
    goals = fields.Integer()
    pim = fields.Integer()
    shots = fields.Integer()
    saves = fields.Integer()
    powerPlaySaves = fields.Integer()
    shortHandedSaves = fields.Integer()
    evenSaves = fields.Integer()
    shortHandedShotsAgainst = fields.Integer()
    evenShotsAgainst = fields.Integer()
    powerPlayShotsAgainst = fields.Integer()
    decision = fields.Str()
    savePercentage = fields.Float()
    powerPlaySavePercentage = fields.Float()
    evenStrengthSavePercentage = fields.Float()
    shortHandedSavePercentage = fields.Float()


class RawBoxscorePlayerStats(Schema):
    skaterStats = fields.Nested(RawBoxscorePlayerSkaterStats)
    goalieStats = fields.Nested(RawBoxscorePlayerGoalieStats)


class RawBoxscorePlayerPerson(Schema):
    id = fields.Integer()
    fullName = fields.Str()
    name = fields.Str()
    link = fields.Str()
    shootsCatches = fields.Str()
    rosterStatus = fields.Str()


class RawBoxscorePlayer(Schema):
    person = fields.Nested(RawBoxscorePlayerPerson)
    jerseyNumber = fields.Integer()
    position = fields.Nested(Position)
    stats = fields.Nested(RawBoxscorePlayerStats)


# -------------- ON ICE PLUS --------------

class RawOnIcePlus(Schema):
    playerId = fields.Integer()
    shiftDuration = fields.Integer()
    stamina = fields.Integer()


# -------------- COACH --------------

class RawBoxscoreCoachPerson(Schema):
    fullName = fields.Str()
    link = fields.Str()


class RawBoxscoreCoach(Schema):
    person = fields.Nested(RawBoxscoreCoachPerson)
    position = fields.Nested(Position)


# -------------- OVERALL TEAM --------------

class RawBoxscoreTeam(Schema):
    team = fields.Nested(Team)
    teamStats = fields.Nested(RawBoxscoreTeamStats)
    players = fields.Nested(RawBoxscorePlayer, many=True)
    goalies = fields.List(fields.Integer)
    skaters = fields.List(fields.Integer)
    onIce = fields.List(fields.Integer)
    onIcePlus = fields.Nested(RawOnIcePlus, many=True)
    scratches = fields.List(fields.Integer)
    penaltyBox = fields.List(fields.Integer)
    coaches = fields.Nested(RawBoxscoreCoach, many=True)

    @pre_load
    def preload_players(self, data, **kwargs):
        data["players"] = [x for x in data["players"].values()]
        return data


class RawBoxscoreTeams(Schema):
    home = fields.Nested(RawBoxscoreTeam)
    away = fields.Nested(RawBoxscoreTeam)


class RawBoxscore(Schema):
    officials = fields.Nested(RawOfficial, many=True)
    teams = fields.Nested(RawBoxscoreTeams)
