# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TicketSaleCreateParams"]


class TicketSaleCreateParams(TypedDict, total=False):
    buyer_name: Required[str]
    """Name of the ticket buyer"""

    currency: Required[str]
    """Currency code (GBP, USD, or EUR)"""

    discount: Required[str]
    """Discount amount applied from coupon"""

    match_id: Required[str]
    """ID of the match"""

    purchase_method: Required[Literal["online", "box_office", "will_call", "phone"]]
    """How the ticket was purchased"""

    quantity: Required[int]
    """Number of tickets purchased"""

    subtotal: Required[str]
    """Subtotal before discount and tax (unit_price \\** quantity)"""

    tax: Required[str]
    """Tax amount (20% UK VAT on discounted subtotal)"""

    total: Required[str]
    """Final total (subtotal - discount + tax)"""

    unit_price: Required[str]
    """Price per ticket (decimal string)"""

    buyer_email: Optional[str]
    """Email of the ticket buyer"""

    coupon_code: Optional[str]
    """Coupon code applied, if any"""
