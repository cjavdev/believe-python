# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .quote import Quote
from .._models import BaseModel

__all__ = ["PaginatedResponseQuote"]


class PaginatedResponseQuote(BaseModel):
    data: List[Quote]

    has_more: bool
    """Whether there are more items after this page."""

    limit: int

    page: int
    """Current page number (1-indexed, for display purposes)."""

    pages: int
    """Total number of pages."""

    skip: int

    total: int
