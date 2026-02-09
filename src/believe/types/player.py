# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .position import Position

__all__ = ["Player"]


class Player(BaseModel):
    """Full player model with ID."""

    id: str
    """Unique identifier for this team membership"""

    character_id: str
    """ID of the character (references /characters/{id})"""

    jersey_number: int
    """Jersey/shirt number"""

    position: Position
    """Playing position on the field"""

    team_id: str
    """ID of the team they belong to"""

    years_with_team: int
    """Number of years with the current team"""

    assists: Optional[int] = None
    """Total assists for the team"""

    goals_scored: Optional[int] = None
    """Total goals scored for the team"""

    is_captain: Optional[bool] = None
    """Whether this player is team captain"""

    member_type: Optional[Literal["player"]] = None
    """Discriminator field indicating this is a player"""
