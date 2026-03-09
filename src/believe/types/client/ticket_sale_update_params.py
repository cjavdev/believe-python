# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["TicketSaleUpdateParams"]


class TicketSaleUpdateParams(TypedDict, total=False):
    buyer_email: Optional[str]

    buyer_name: Optional[str]

    coupon_code: Optional[str]

    currency: Optional[str]

    discount: Optional[str]

    match_id: Optional[str]

    purchase_method: Optional[Literal["online", "box_office", "will_call", "phone"]]
    """How the ticket was purchased."""

    quantity: Optional[int]

    subtotal: Optional[str]

    tax: Optional[str]

    total: Optional[str]

    unit_price: Optional[str]
