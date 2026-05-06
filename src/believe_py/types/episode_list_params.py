# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["EpisodeListParams"]


class EpisodeListParams(TypedDict, total=False):
    character_focus: Optional[str]
    """Filter by character focus (character ID)"""

    limit: int
    """Maximum number of items to return (max: 100)"""

    season: Optional[int]
    """Filter by season"""

    skip: int
    """Number of items to skip (offset)"""
