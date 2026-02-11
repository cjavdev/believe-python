# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .character_role import CharacterRole

__all__ = ["CharacterListParams"]


class CharacterListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return (max: 100)"""

    min_optimism: Optional[int]
    """Minimum optimism score"""

    role: Optional[CharacterRole]
    """Filter by role"""

    skip: int
    """Number of items to skip (offset)"""

    team_id: Optional[str]
    """Filter by team ID"""
