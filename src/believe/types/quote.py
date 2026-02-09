# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .quote_theme import QuoteTheme
from .quote_moment import QuoteMoment

__all__ = ["Quote"]


class Quote(BaseModel):
    """Full quote model with ID."""

    id: str
    """Unique identifier"""

    character_id: str
    """ID of the character who said it"""

    context: str
    """Context in which the quote was said"""

    moment_type: QuoteMoment
    """Type of moment when the quote was said"""

    text: str
    """The quote text"""

    theme: QuoteTheme
    """Primary theme of the quote"""

    episode_id: Optional[str] = None
    """Episode where the quote appears"""

    is_funny: Optional[bool] = None
    """Whether this quote is humorous"""

    is_inspirational: Optional[bool] = None
    """Whether this quote is inspirational"""

    popularity_score: Optional[float] = None
    """Popularity/virality score (0-100)"""

    secondary_themes: Optional[List[QuoteTheme]] = None
    """Additional themes"""

    times_shared: Optional[int] = None
    """Number of times shared on social media"""
