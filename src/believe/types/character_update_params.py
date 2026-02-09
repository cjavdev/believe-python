# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .character_role import CharacterRole
from .growth_arc_param import GrowthArcParam
from .emotional_stats_param import EmotionalStatsParam

__all__ = ["CharacterUpdateParams"]


class CharacterUpdateParams(TypedDict, total=False):
    background: Optional[str]

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    email: Optional[str]

    emotional_stats: Optional[EmotionalStatsParam]
    """Emotional intelligence statistics for a character."""

    growth_arcs: Optional[Iterable[GrowthArcParam]]

    height_meters: Optional[float]

    name: Optional[str]

    personality_traits: Optional[SequenceNotStr[str]]

    profile_image_url: Optional[str]

    role: Optional[CharacterRole]
    """Roles characters can have."""

    salary_gbp: Union[float, str, None]

    signature_quotes: Optional[SequenceNotStr[str]]

    team_id: Optional[str]
