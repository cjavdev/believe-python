# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ReframeTransformNegativeThoughtsResponse"]


class ReframeTransformNegativeThoughtsResponse(BaseModel):
    """Reframed perspective response."""

    daily_affirmation: str
    """A daily affirmation to practice"""

    original_thought: str
    """The original negative thought"""

    reframed_thought: str
    """The thought reframed positively"""

    ted_perspective: str
    """Ted's take on this thought"""

    dr_sharon_insight: Optional[str] = None
    """Dr. Sharon's therapeutic insight"""
