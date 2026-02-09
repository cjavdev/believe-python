# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypedDict

from .league import League
from .._types import SequenceNotStr
from .team_values_param import TeamValuesParam
from .geo_location_param import GeoLocationParam

__all__ = ["TeamCreateParams"]


class TeamCreateParams(TypedDict, total=False):
    culture_score: Required[int]
    """Team culture/morale score (0-100)"""

    founded_year: Required[int]
    """Year the club was founded"""

    league: Required[League]
    """Current league"""

    name: Required[str]
    """Team name"""

    stadium: Required[str]
    """Home stadium name"""

    values: Required[TeamValuesParam]
    """Team's core values"""

    annual_budget_gbp: Union[float, str, None]
    """Annual budget in GBP"""

    average_attendance: Optional[float]
    """Average match attendance"""

    contact_email: Optional[str]
    """Team contact email"""

    is_active: bool
    """Whether the team is currently active"""

    nickname: Optional[str]
    """Team nickname"""

    primary_color: Optional[str]
    """Primary team color (hex)"""

    rival_teams: SequenceNotStr[str]
    """List of rival team IDs"""

    secondary_color: Optional[str]
    """Secondary team color (hex)"""

    stadium_location: Optional[GeoLocationParam]
    """Geographic coordinates for a location."""

    website: Optional[str]
    """Official team website"""

    win_percentage: Optional[float]
    """Season win percentage"""
