# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EpisodeCreateParams"]


class EpisodeCreateParams(TypedDict, total=False):
    air_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Original air date"""

    character_focus: Required[SequenceNotStr[str]]
    """Characters with significant development"""

    director: Required[str]
    """Episode director"""

    episode_number: Required[int]
    """Episode number within season"""

    main_theme: Required[str]
    """Central theme of the episode"""

    runtime_minutes: Required[int]
    """Episode runtime in minutes"""

    season: Required[int]
    """Season number"""

    synopsis: Required[str]
    """Brief plot synopsis"""

    ted_wisdom: Required[str]
    """Key piece of Ted wisdom from the episode"""

    title: Required[str]
    """Episode title"""

    writer: Required[str]
    """Episode writer(s)"""

    biscuits_with_boss_moment: Optional[str]
    """Notable biscuits with the boss scene"""

    memorable_moments: SequenceNotStr[str]
    """Standout moments from the episode"""

    us_viewers_millions: Optional[float]
    """US viewership in millions"""

    viewer_rating: Optional[float]
    """Viewer rating out of 10"""
