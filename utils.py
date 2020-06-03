''' utilities used for extracting data '''
import json
import requests
import logging


def get_json_from_url(url):
    ''' given url, make request and return json '''
    response = requests.get(url, timeout=60)
    return json.loads(response.text)


def get_logger(filepath='logger'):
    ''' util for getting logger '''
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(filepath)
    return logger
