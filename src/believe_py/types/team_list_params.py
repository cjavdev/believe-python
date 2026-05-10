# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .league import League

__all__ = ["TeamListParams"]


class TeamListParams(TypedDict, total=False):
    league: Optional[League]
    """Filter by league"""

    limit: int
    """Maximum number of items to return (max: 100)"""

    min_culture_score: Optional[int]
    """Minimum culture score"""

    skip: int
    """Number of items to skip (offset)"""
