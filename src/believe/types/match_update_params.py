# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .match_type import MatchType
from .match_result import MatchResult
from .turning_point_param import TurningPointParam

__all__ = ["MatchUpdateParams"]


class MatchUpdateParams(TypedDict, total=False):
    attendance: Optional[int]

    away_score: Optional[int]

    away_team_id: Optional[str]

    date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    episode_id: Optional[str]

    home_score: Optional[int]

    home_team_id: Optional[str]

    lesson_learned: Optional[str]

    match_type: Optional[MatchType]
    """Types of matches."""

    possession_percentage: Optional[float]

    result: Optional[MatchResult]
    """Match result types."""

    ted_halftime_speech: Optional[str]

    ticket_revenue_gbp: Union[float, str, None]

    turning_points: Optional[Iterable[TurningPointParam]]

    weather_temp_celsius: Optional[float]
