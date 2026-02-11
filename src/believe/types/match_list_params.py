# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .match_type import MatchType
from .match_result import MatchResult

__all__ = ["MatchListParams"]


class MatchListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return (max: 100)"""

    match_type: Optional[MatchType]
    """Filter by match type"""

    result: Optional[MatchResult]
    """Filter by result"""

    skip: int
    """Number of items to skip (offset)"""

    team_id: Optional[str]
    """Filter by team (home or away)"""
