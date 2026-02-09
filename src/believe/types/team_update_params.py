# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypedDict

from .league import League
from .._types import SequenceNotStr
from .team_values_param import TeamValuesParam
from .geo_location_param import GeoLocationParam

__all__ = ["TeamUpdateParams"]


class TeamUpdateParams(TypedDict, total=False):
    annual_budget_gbp: Union[float, str, None]

    average_attendance: Optional[float]

    contact_email: Optional[str]

    culture_score: Optional[int]

    founded_year: Optional[int]

    is_active: Optional[bool]

    league: Optional[League]
    """Football leagues."""

    name: Optional[str]

    nickname: Optional[str]

    primary_color: Optional[str]

    rival_teams: Optional[SequenceNotStr[str]]

    secondary_color: Optional[str]

    stadium: Optional[str]

    stadium_location: Optional[GeoLocationParam]
    """Geographic coordinates for a location."""

    values: Optional[TeamValuesParam]
    """Core values that define a team's culture."""

    website: Optional[str]

    win_percentage: Optional[float]
