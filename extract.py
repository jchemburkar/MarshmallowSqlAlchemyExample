''' main upload file for schedule '''
from utils import get_json_from_url, get_logger
from marshmallow_schemas.raw_schemas.raw_game import RawGame

logger = get_logger()
GAME_ENDPOINT = "https://statsapi.web.nhl.com/api/v1/game/%s/feed/live"
SCHEDULE_ENDPOINT = "https://statsapi.web.nhl.com/api/v1/schedule"


def extract_game_ids_for_date(date):
    '''
    extracts game ids from schedule, that then get passed to the game endpoint for
    extracting individual games
    :param date: date to be queried
    :return: list of nhl game ids for that date
    '''
    # pull raw schedule info from endpoint
    logger.info('Getting schedule info for %s' % date)
    url = SCHEDULE_ENDPOINT + '?startDate=%s&endDate=%s' % (date, date)
    data = get_json_from_url(url)

    # iterate through the schedule data to get the game ids for every game
    game_ids = []
    for date in data.get("dates", []):
        for game in date.get("games", []):
            game_ids.append(game["gamePk"])

    return game_ids


def extract_game(game_id):
    '''
    extracts game data from endpoint given a game id
    :return: dict representing game data
    '''
    url = GAME_ENDPOINT % game_id
    data = get_json_from_url(url)

    # NOTE: here, we can use the 'raw' marshmallow schemas to validate the data being returned from an endpoint
    # this can help us catch if any new fields are added, or if a field has unexpected values (null, incorrect datatype, etc)
    extracted_data = RawGame().load(data)
    return extracted_data
