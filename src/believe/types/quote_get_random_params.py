# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .quote_theme import QuoteTheme

__all__ = ["QuoteGetRandomParams"]


class QuoteGetRandomParams(TypedDict, total=False):
    character_id: Optional[str]
    """Filter by character"""

    inspirational: Optional[bool]
    """Filter inspirational quotes"""

    theme: Optional[QuoteTheme]
    """Themes that quotes can be categorized under."""
