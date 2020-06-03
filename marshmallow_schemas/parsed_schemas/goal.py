''' schema for parsing goal rows from raw data '''
from marshmallow import fields, Schema, pre_dump
from marshmallow_schemas.parsed_schemas.shot_attempt import ShotAttempt


class Goal(ShotAttempt):
    goal_scorer_id = fields.Integer()
    first_assist_id = fields.Integer(default=None)
    second_assist_id = fields.Integer(default=None)
    scoring_team_strength = fields.Str(attribute="result.strength.name")
    is_empty_net = fields.Boolean(attribute="result.emptyNet")
    is_game_winning_goal = fields.Boolean(attribute="result.gameWinningGoal")

    @pre_dump
    def predump_goal(self, data, **kwargs):
        """ parse out assist information and format the strenght of the goal """
        data["goal_scorer_id"] = data["players"][0]["player"]["id"]
        if len(data["players"]) > 2 and data["players"][1]["playerType"] == "Assist":
            data["first_assist_id"] = data["players"][1]["player"]["id"]

        if len(data["players"]) > 3 and data["players"][2]["playerType"] == "Assist":
            data["second_assist_id"] = data["players"][2]["player"]["id"]

        if "strength" in data["result"]:
            data["result"]["strength"]["name"] = data["result"]["strength"]["name"].lower().replace(' ', '_')

        return data
