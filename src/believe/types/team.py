# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .league import League
from .._models import BaseModel
from .team_values import TeamValues
from .geo_location import GeoLocation

__all__ = ["Team"]


class Team(BaseModel):
    """Full team model with ID."""

    id: str
    """Unique identifier"""

    culture_score: int
    """Team culture/morale score (0-100)"""

    founded_year: int
    """Year the club was founded"""

    league: League
    """Current league"""

    name: str
    """Team name"""

    stadium: str
    """Home stadium name"""

    values: TeamValues
    """Team's core values"""

    annual_budget_gbp: Optional[str] = None
    """Annual budget in GBP"""

    average_attendance: Optional[float] = None
    """Average match attendance"""

    contact_email: Optional[str] = None
    """Team contact email"""

    is_active: Optional[bool] = None
    """Whether the team is currently active"""

    nickname: Optional[str] = None
    """Team nickname"""

    primary_color: Optional[str] = None
    """Primary team color (hex)"""

    rival_teams: Optional[List[str]] = None
    """List of rival team IDs"""

    secondary_color: Optional[str] = None
    """Secondary team color (hex)"""

    stadium_location: Optional[GeoLocation] = None
    """Geographic coordinates for a location."""

    website: Optional[str] = None
    """Official team website"""

    win_percentage: Optional[float] = None
    """Season win percentage"""
