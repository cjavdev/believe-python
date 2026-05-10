# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["TeamMemberListParams"]


class TeamMemberListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return (max: 100)"""

    member_type: Optional[Literal["player", "coach", "medical_staff", "equipment_manager"]]
    """Filter by member type"""

    skip: int
    """Number of items to skip (offset)"""

    team_id: Optional[str]
    """Filter by team ID"""
