# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TurningPointParam"]


class TurningPointParam(TypedDict, total=False):
    """A pivotal moment in a match."""

    description: Required[str]
    """What happened"""

    emotional_impact: Required[str]
    """How this affected the team emotionally"""

    minute: Required[int]
    """Minute of the match"""

    character_involved: Optional[str]
    """Character ID who was central to this moment"""
