# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .position import Position

__all__ = ["TeamMemberListPlayersParams"]


class TeamMemberListPlayersParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return (max: 100)"""

    position: Optional[Position]
    """Football positions for players."""

    skip: int
    """Number of items to skip (offset)"""

    team_id: Optional[str]
    """Filter by team ID"""
