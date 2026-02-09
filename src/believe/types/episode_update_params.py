# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EpisodeUpdateParams"]


class EpisodeUpdateParams(TypedDict, total=False):
    air_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    biscuits_with_boss_moment: Optional[str]

    character_focus: Optional[SequenceNotStr[str]]

    director: Optional[str]

    episode_number: Optional[int]

    main_theme: Optional[str]

    memorable_moments: Optional[SequenceNotStr[str]]

    runtime_minutes: Optional[int]

    season: Optional[int]

    synopsis: Optional[str]

    ted_wisdom: Optional[str]

    title: Optional[str]

    us_viewers_millions: Optional[float]

    viewer_rating: Optional[float]

    writer: Optional[str]
