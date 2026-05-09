# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .coach_specialty import CoachSpecialty

__all__ = ["Coach"]


class Coach(BaseModel):
    """Full coach model with ID."""

    id: str
    """Unique identifier for this team membership"""

    character_id: str
    """ID of the character (references /characters/{id})"""

    specialty: CoachSpecialty
    """Coaching specialty/role"""

    team_id: str
    """ID of the team they belong to"""

    years_with_team: int
    """Number of years with the current team"""

    certifications: Optional[List[str]] = None
    """Coaching certifications and licenses"""

    member_type: Optional[Literal["coach"]] = None
    """Discriminator field indicating this is a coach"""

    win_rate: Optional[float] = None
    """Career win rate (0.0 to 1.0)"""
