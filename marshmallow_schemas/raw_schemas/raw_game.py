''' overall raw game schema '''
from marshmallow import Schema, fields
from marshmallow_schemas.raw_schemas.raw_game_boxscore import RawBoxscore
from marshmallow_schemas.raw_schemas.raw_game_decisions import RawDecisions
from marshmallow_schemas.raw_schemas.raw_game_game import RawGameGame
from marshmallow_schemas.raw_schemas.raw_game_linescore import RawLinescore
from marshmallow_schemas.raw_schemas.raw_game_plays import RawPlays


class RawMetaData(Schema):
    timeStamp = fields.Str()
    wait = fields.Integer()


class RawLiveData(Schema):
    plays = fields.Nested(RawPlays)
    linescore = fields.Nested(RawLinescore)
    boxscore = fields.Nested(RawBoxscore)
    decisions = fields.Nested(RawDecisions)
    shotPressure = fields.Dict()


class RawGame(Schema):
    gamePk = fields.Integer()
    copyright = fields.Str()
    link = fields.Str()
    metaData = fields.Nested(RawMetaData)
    gameData = fields.Nested(RawGameGame)
    liveData = fields.Nested(RawLiveData)
