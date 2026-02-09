# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TurningPoint"]


class TurningPoint(BaseModel):
    """A pivotal moment in a match."""

    description: str
    """What happened"""

    emotional_impact: str
    """How this affected the team emotionally"""

    minute: int
    """Minute of the match"""

    character_involved: Optional[str] = None
    """Character ID who was central to this moment"""
