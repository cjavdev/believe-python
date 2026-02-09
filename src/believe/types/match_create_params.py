# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .match_type import MatchType
from .match_result import MatchResult
from .turning_point_param import TurningPointParam

__all__ = ["MatchCreateParams"]


class MatchCreateParams(TypedDict, total=False):
    away_team_id: Required[str]
    """Away team ID"""

    date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Match date and time"""

    home_team_id: Required[str]
    """Home team ID"""

    match_type: Required[MatchType]
    """Type of match"""

    attendance: Optional[int]
    """Match attendance"""

    away_score: int
    """Away team score"""

    episode_id: Optional[str]
    """Episode ID where this match is featured"""

    home_score: int
    """Home team score"""

    lesson_learned: Optional[str]
    """The life lesson learned from this match"""

    possession_percentage: Optional[float]
    """Home team possession percentage"""

    result: MatchResult
    """Match result from home team perspective"""

    ted_halftime_speech: Optional[str]
    """Ted's inspirational halftime speech"""

    ticket_revenue_gbp: Union[float, str, None]
    """Total ticket revenue in GBP"""

    turning_points: Iterable[TurningPointParam]
    """Key moments that changed the match"""

    weather_temp_celsius: Optional[float]
    """Temperature at kickoff in Celsius"""
