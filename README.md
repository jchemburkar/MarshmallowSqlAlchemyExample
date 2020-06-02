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

`ENV=<env> PYTHONPATH=<path to repo> python upload_example.py --date <date>`
	* ENV: takes in `local` or `docker`. Local will upload to local mysql db while docker while insert into local docker db
	* PYTHONPATH: path to repo. Include the repo folder (`MarshmallowSqlAlchemyExample`)
	* date: date of games to be uploaded. Takes YYYY-MM-DD format; e.g. `2019-02-07`

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