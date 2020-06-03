''' contains transform for transforming an nhl game response '''
from marshmallow_schemas.parsed_schemas.goal import Goal
from marshmallow_schemas.parsed_schemas.shot_attempt import ShotAttempt

def transform_plays(play_events, rows, context):
    '''
    transforms the play in allPlays
    :param play_events: dictionary representing raw game dump
    :param rows: dictionary of table name to rows
    :param context: context specific to game
    :return: None
    '''
    for play in play_events:
        # parse out the event type and dump into appropriate schema
        # NOTE: here, we are using the "parsed" schemas to deserialize the raw data into the format we wish to store
        # the data in
        event = play["result"]["event"]
        if event in ["Goal"]:
            goal = Goal(context=context).dump(play)
            rows["goal"].append(goal)

        if event in ["Shot", "Missed Shot", "BlockedShot", "Goal"]:
            shot_attempt = ShotAttempt(context=context).dump(play)
            rows["shot_attempt"].append(shot_attempt)


def transform_game(raw_game):
    '''
    transforms rows out of raw game object
    :param data: raw game object
    :return: rows, a dictionary mapping table name to rows
    '''
    rows = {table: [] for table in ['shot_attempt', 'goal']}
    context = {"game_pk": raw_game["gamePk"], "teams": raw_game["liveData"]["boxscore"]["teams"]}  # use the context to store general data for parse
    transform_plays(raw_game["liveData"]["plays"]["allPlays"], rows, context)
    return rows
