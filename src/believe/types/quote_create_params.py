# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .quote_theme import QuoteTheme
from .quote_moment import QuoteMoment

__all__ = ["QuoteCreateParams"]


class QuoteCreateParams(TypedDict, total=False):
    character_id: Required[str]
    """ID of the character who said it"""

    context: Required[str]
    """Context in which the quote was said"""

    moment_type: Required[QuoteMoment]
    """Type of moment when the quote was said"""

    text: Required[str]
    """The quote text"""

    theme: Required[QuoteTheme]
    """Primary theme of the quote"""

    episode_id: Optional[str]
    """Episode where the quote appears"""

    is_funny: bool
    """Whether this quote is humorous"""

    is_inspirational: bool
    """Whether this quote is inspirational"""

    popularity_score: Optional[float]
    """Popularity/virality score (0-100)"""

    secondary_themes: List[QuoteTheme]
    """Additional themes"""

    times_shared: Optional[int]
    """Number of times shared on social media"""
