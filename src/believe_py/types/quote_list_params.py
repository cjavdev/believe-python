# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .quote_theme import QuoteTheme
from .quote_moment import QuoteMoment

__all__ = ["QuoteListParams"]


class QuoteListParams(TypedDict, total=False):
    character_id: Optional[str]
    """Filter by character"""

    funny: Optional[bool]
    """Filter funny quotes"""

    inspirational: Optional[bool]
    """Filter inspirational quotes"""

    limit: int
    """Maximum number of items to return (max: 100)"""

    moment_type: Optional[QuoteMoment]
    """Filter by moment type"""

    skip: int
    """Number of items to skip (offset)"""

    theme: Optional[QuoteTheme]
    """Filter by theme"""
