# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .._models import BaseModel
from .growth_arc import GrowthArc
from .character_role import CharacterRole
from .emotional_stats import EmotionalStats

__all__ = ["Character"]


class Character(BaseModel):
    """Full character model with ID."""

    id: str
    """Unique identifier"""

    background: str
    """Character background and history"""

    emotional_stats: EmotionalStats
    """Emotional intelligence stats"""

    name: str
    """Character's full name"""

    personality_traits: List[str]
    """Key personality traits"""

    role: CharacterRole
    """Character's role"""

    date_of_birth: Optional[date] = None
    """Character's date of birth"""

    email: Optional[str] = None
    """Character's email address"""

    growth_arcs: Optional[List[GrowthArc]] = None
    """Character development across seasons"""

    height_meters: Optional[float] = None
    """Height in meters"""

    profile_image_url: Optional[str] = None
    """URL to character's profile image"""

    salary_gbp: Optional[str] = None
    """Annual salary in GBP"""

    signature_quotes: Optional[List[str]] = None
    """Memorable quotes from this character"""

    team_id: Optional[str] = None
    """ID of the team they belong to"""
