# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from typing import Optional, Union, Iterable

from datetime import date

from .._utils import PropertyInfo

from .emotional_stats_param import EmotionalStatsParam

from .growth_arc_param import GrowthArcParam

from .._types import SequenceNotStr

from .character_role import CharacterRole

__all__ = ["CharacterUpdateParams"]

class CharacterUpdateParams(TypedDict, total=False):
    background: Optional[str]

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format = "iso8601")]

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