''' schema for parsing shot attempt rows from raw data '''
from marshmallow import fields, Schema, pre_dump


class ShotAttempt(Schema):
    game_pk = fields.Str()
    goalie_id = fields.Integer()
    shooter_id = fields.Integer()
    shooter_team_id = fields.Integer(attribute="team.id")
    location_x = fields.Integer(attribute="coordinates.x")
    location_y = fields.Integer(attribute="coordinates.y")
    shot_type = fields.Str(attribute="result.secondaryType")
    description = fields.Str(attribute="result.description")
    event_index = fields.Integer(attribute="about.eventIdx")
    event_id = fields.Integer(attribute="about.eventId")
    period = fields.Integer(attribute="about.period")
    period_time_remaining = fields.Str(attribute="about.periodTimeRemaining")
    timestamp = fields.DateTime(attribute="about.dateTime")
    home_score = fields.Integer(attribute="about.goals.home")
    away_score = fields.Integer(attribute="about.goals.away")

    @pre_dump
    def predump_data(self, data, **kwargs):
        """ performs predump transforms on data; gets shooter and goalie; formats fields """
        data["game_pk"] = self.context["game_pk"]

        # parse out shooter and goalie from players list
        for player in data.get("players", []):
            if player["playerType"] in ("Shooter", "Scorer"):
                data["shooter_id"] = player["player"]["id"]
            elif player["playerType"] == "Goalie":
                data["goalie_id"] = player["player"]["id"]

        # format fields
        if "secondaryType" in data.get("result", {}):
            data["result"]["secondaryType"] = data["result"]["secondaryType"].lower().replace(' ', '_')

        return data
