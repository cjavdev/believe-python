# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ConflictResolveResponse"]


class ConflictResolveResponse(BaseModel):
    """Conflict resolution response."""

    barbecue_sauce_wisdom: str
    """A folksy metaphor to remember"""

    diagnosis: str
    """Understanding the root cause"""

    diamond_dogs_advice: str
    """Advice from the Diamond Dogs support group"""

    potential_outcome: str
    """What resolution could look like"""

    steps_to_resolution: List[str]
    """Concrete steps to resolve the conflict"""

    ted_approach: str
    """How Ted would handle this"""
