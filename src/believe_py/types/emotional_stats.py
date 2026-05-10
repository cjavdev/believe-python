# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["EmotionalStats"]


class EmotionalStats(BaseModel):
    """Emotional intelligence statistics for a character."""

    curiosity: int
    """Level of curiosity over judgment (0-100)"""

    empathy: int
    """Capacity for empathy (0-100)"""

    optimism: int
    """Level of optimism (0-100)"""

    resilience: int
    """Bounce-back ability (0-100)"""

    vulnerability: int
    """Willingness to be vulnerable (0-100)"""
