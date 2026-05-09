# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .character_role import CharacterRole
from .growth_arc_param import GrowthArcParam
from .emotional_stats_param import EmotionalStatsParam

__all__ = ["CharacterCreateParams"]


class CharacterCreateParams(TypedDict, total=False):
    background: Required[str]
    """Character background and history"""

    emotional_stats: Required[EmotionalStatsParam]
    """Emotional intelligence stats"""

    name: Required[str]
    """Character's full name"""

    personality_traits: Required[SequenceNotStr[str]]
    """Key personality traits"""

    role: Required[CharacterRole]
    """Character's role"""

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Character's date of birth"""

    email: Optional[str]
    """Character's email address"""

    growth_arcs: Iterable[GrowthArcParam]
    """Character development across seasons"""

    height_meters: Optional[float]
    """Height in meters"""

    profile_image_url: Optional[str]
    """URL to character's profile image"""

    salary_gbp: Union[float, str, None]
    """Annual salary in GBP"""

    signature_quotes: SequenceNotStr[str]
    """Memorable quotes from this character"""

    team_id: Optional[str]
    """ID of the team they belong to"""
