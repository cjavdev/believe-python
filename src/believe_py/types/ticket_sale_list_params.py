# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .purchase_method import PurchaseMethod

__all__ = ["TicketSaleListParams"]


class TicketSaleListParams(TypedDict, total=False):
    coupon_code: Optional[str]
    """Filter by coupon code (use 'none' for sales without coupons)"""

    currency: Optional[str]
    """Filter by currency (GBP, USD, EUR)"""

    limit: int
    """Maximum number of items to return (max: 100)"""

    match_id: Optional[str]
    """Filter by match ID"""

    purchase_method: Optional[PurchaseMethod]
    """Filter by purchase method"""

    skip: int
    """Number of items to skip (offset)"""
