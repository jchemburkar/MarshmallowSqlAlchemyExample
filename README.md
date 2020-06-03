# SQLAlchemy and Marshmallow Example

## Overview

This module scrapes the publicly available NHL Api for game data given a specific day. The code is meant to demonstrate how to form an ETL process using Marshmallow for data validation and SQLAlchemy for database operations.

## Setup

To set up, run the following commands. Start by cloning this repo:

`git clone https://github.com/jchemburkar/MarshmallowSqlAlchemyExample`

Then, `cd` into the directory containing the cloned repo. From there, set up a virtual env:

`virtualenv .env; . .env/bin/activate`

This should create and activate your virtualenv. You should see `(.env)` at the left of your terminal command line. Now, we want to install relevant packages:

`pip install -r requirements.txt` 

Now our environment should be all set up to run the uploader!

## How to run

To run, call the following;

`PYTHONPATH=<path to repo> python upload_example.py --date <date>`

* PYTHONPATH: path to repo. Include the repo folder (`MarshmallowSqlAlchemyExample`)
* date: date of games to be uploaded. Takes YYYY-MM-DD format; e.g. `2019-02-07`

## Workflow

The general structure of the uploader is as follows:

1. data is extracted from a raw api endpoint. data is recieved in a json format
2. data is passed through a set of "raw" marshmallow schemas. These specify exactly how we expact the incoming data to look; any unexpected fields, or fields that are null/have an incorrrect datatype will throw an error. This step validates the incoming data during extraction
3. data is transformed with the help of "parsed" marshmallow schemas. this enables us to deserialize and transform the raw data into the format we wish to store in the database. we often leverage certain features of these marshmallow schemas (context, pre/post dumps) to enrich the data in the process.
4. data is loaded into the databse through sqlalchemy. in addition to helping specify and create our table structure, sqlalchemy helps us enforce relationships between different tables.

In order to see out these steps, the module is structured as follows:

* upload_example.py: main file combining all pieces of the uploader
* extract.py: contains functions for pulling raw data from api
* transform.py: contains functions for parsing through raw data, and transforming that into db-formatted rows
* load.py: contains functions using SQLAlchemy to manage database operations
* marshamllow_schemas/

	* raw_schemas: contains schemas that model the structure of a raw api response
	* parsed_schemas: contain schemas that perform deserialization of raw data into db format
	* schema_utils.py: helper schemas used in different places

* models: contains files for SQLAlchemy models (one table per file)
* utils.py: utility functions for extracting and logging
* requirements.txt: contains packages needed in environment for this module to work

## Data Overview

The rough structure of the raw data is as follows:
```
	{
		copyright: (str),
		gamePk: (int),
		link: (str),
		metadata: {...},
		game: {
			game: {game metadata},
			datetime: {game time data},
			status: {info on game completion},
			teams: {
				home: {info on home team},
				away: {info on away team}
			},
			players: [list of player dictionaries],
			venue: {info on venue}
		},
		liveData: {
			plays: {
				allPlays: [all events (shots, goals, etc) throughout game],
				scoringPlays: [indices in allPlays with goals],
				penaltyPlays: [indices in allPlays with penalties],
				playsByPeriod: {divies up plays into dictionaries by what period they happened in},
				currentPlay: {play node of most recent play if game is live, else the last play}
			},
			linescore: {period summaries on goals, shots, etc},
			boxscore: {overall stats for players, teams, etc.},
			decisions: {winner, loser, 1/2/3 star}
		}
	}
```

We are parsing this into the following tables:

| TABLE        | Stores                                                            |
|--------------|-------------------------------------------------------------------|
| shot_attempt | a row for every shot attempt, containing shooter, location, etc   |
| goal         | a row for every goal, with similar information to what is in shot |

There are plenty of other things that can be parsed from this data (penalties, faceoffs, winners/losers, boxscores, linescores) but I wanted to keep this example limited in scope.