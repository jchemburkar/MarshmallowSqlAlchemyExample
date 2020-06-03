''' sql alchemy model for shot_attempt table '''
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import MEDIUMINT, TINYINT, SMALLINT, VARCHAR, DATETIME, INTEGER
from models.sqla_utils import BASE


class ShotAttempt(BASE):
    __tablename__ = 'shot_attempt'

    game_pk = Column(VARCHAR(10), primary_key=True)
    event_index = Column(SMALLINT, primary_key=True)
    event_id = Column(MEDIUMINT)
    goalie_id = Column(INTEGER(10))
    shooter_id = Column(INTEGER(10))
    shooter_team_id = Column(TINYINT(3))
    location_x = Column(TINYINT(3))
    location_y = Column(TINYINT(3))
    shot_type = Column(VARCHAR(15))
    description = Column(VARCHAR(150))
    period = Column(TINYINT(1))
    period_time_remaining = Column(VARCHAR(5))
    home_score = Column(TINYINT(3))
    away_score = Column(TINYINT(3))
    timestamp = Column(DATETIME)
