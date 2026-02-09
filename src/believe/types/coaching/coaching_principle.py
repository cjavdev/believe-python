# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CoachingPrinciple"]


class CoachingPrinciple(BaseModel):
    """A Ted Lasso coaching principle."""

    id: str
    """Principle identifier"""

    application: str
    """How to apply this principle"""

    example_from_show: str
    """Example from the show"""

    explanation: str
    """What this principle means"""

    principle: str
    """The coaching principle"""

    ted_quote: str
    """Related Ted quote"""
