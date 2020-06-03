''' sql alchemy model for goal table '''
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import MEDIUMINT, INTEGER, TINYINT, SMALLINT, VARCHAR, DATETIME
from models.sqla_utils import BASE


class Goal(BASE):
    __tablename__ = 'goal'

    game_pk = Column(VARCHAR(10), primary_key=True)
    event_index = Column(SMALLINT, primary_key=True)
    event_id = Column(MEDIUMINT)
    goalie_id = Column(INTEGER(10))
    shooter_id = Column(INTEGER(10))
    shooter_team_id = Column(INTEGER(3))
    goal_scorer_id = Column(INTEGER(10))
    first_assist_id = Column(INTEGER(10))
    second_assist_id = Column(INTEGER(10))
    location_x = Column(TINYINT(3))
    location_y = Column(TINYINT(3))
    shot_type = Column(VARCHAR(15))
    description = Column(VARCHAR(150))
    period = Column(TINYINT(1))
    period_time_remaining = Column(VARCHAR(5))
    home_score = Column(TINYINT(3))
    away_score = Column(TINYINT(3))
    scoring_team_strength = Column(VARCHAR(15))
    is_empty_net = Column(TINYINT(1))
    is_game_winning_goal = Column(TINYINT(1))
    timestamp = Column(DATETIME)
