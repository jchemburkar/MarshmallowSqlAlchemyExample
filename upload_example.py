""" upload file for nhl game data """
import argparse
from utils import get_logger
from extract import extract_game_ids_for_date, extract_game
from transform import transform_game
from load import create_tables, load_data

logger = get_logger()


def get_args():
    ''' parses any command line arguments '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', default=None, help='Day to get games from in YYYY-MM-DD format')
    return parser.parse_args()


def main():
    ''' main function 
    This puts the pieces of the ETL all together:
    extract -- reads raw data from api endpoints, and passes through raw schemas for validation
    transform -- uses parsed schemas to deserialize data into desired format for DB
    load -- uses sqlalchemy models + session to safely merge the data into the database
    '''
    args = get_args()
    if not args.date:
        logger.error('Must pass date for parsing')
        return

    # extract -- start by extracting all game_ids; then extract each game one by one
    results = {"shot_attempt": [], "goal": []}
    game_ids = extract_game_ids_for_date(args.date)
    logger.info('Receieved %s game_ids to load', len(game_ids))
    for game_id in game_ids:
        logger.info('Extracting: %s', game_id)
        raw_game = extract_game(game_id)

        # transform -- for each game we get, turn it into parsed shot and goal rows
        parsed_data = transform_game(raw_game)
        results["shot_attempt"].extend(parsed_data["shot_attempt"])
        results["goal"].extend(parsed_data["goal"])

    # load -- once all games have been iterated through, create sqlalchemy models out of the rows and insert
    create_tables()
    load_data(results)


if __name__ == '__main__':
    main()