# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .coach_specialty import CoachSpecialty

__all__ = ["TeamMemberListCoachesParams"]


class TeamMemberListCoachesParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return (max: 100)"""

    skip: int
    """Number of items to skip (offset)"""

    specialty: Optional[CoachSpecialty]
    """Filter by specialty"""

    team_id: Optional[str]
    """Filter by team ID"""
