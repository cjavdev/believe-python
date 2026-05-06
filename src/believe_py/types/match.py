# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .match_type import MatchType
from .match_result import MatchResult
from .turning_point import TurningPoint

__all__ = ["Match"]


class Match(BaseModel):
    """Full match model with ID."""

    id: str
    """Unique identifier"""

    away_team_id: str
    """Away team ID"""

    date: datetime
    """Match date and time"""

    home_team_id: str
    """Home team ID"""

    match_type: MatchType
    """Type of match"""

    attendance: Optional[int] = None
    """Match attendance"""

    away_score: Optional[int] = None
    """Away team score"""

    episode_id: Optional[str] = None
    """Episode ID where this match is featured"""

    home_score: Optional[int] = None
    """Home team score"""

    lesson_learned: Optional[str] = None
    """The life lesson learned from this match"""

    possession_percentage: Optional[float] = None
    """Home team possession percentage"""

    result: Optional[MatchResult] = None
    """Match result from home team perspective"""

    ted_halftime_speech: Optional[str] = None
    """Ted's inspirational halftime speech"""

    ticket_revenue_gbp: Optional[str] = None
    """Total ticket revenue in GBP"""

    turning_points: Optional[List[TurningPoint]] = None
    """Key moments that changed the match"""

    weather_temp_celsius: Optional[float] = None
    """Temperature at kickoff in Celsius"""
