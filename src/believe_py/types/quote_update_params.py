# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from .quote_theme import QuoteTheme
from .quote_moment import QuoteMoment

__all__ = ["QuoteUpdateParams"]


class QuoteUpdateParams(TypedDict, total=False):
    character_id: Optional[str]

    context: Optional[str]

    episode_id: Optional[str]

    is_funny: Optional[bool]

    is_inspirational: Optional[bool]

    moment_type: Optional[QuoteMoment]
    """Types of moments when quotes occur."""

    popularity_score: Optional[float]

    secondary_themes: Optional[List[QuoteTheme]]

    text: Optional[str]

    theme: Optional[QuoteTheme]
    """Themes that quotes can be categorized under."""

    times_shared: Optional[int]
