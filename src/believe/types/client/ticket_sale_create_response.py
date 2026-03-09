# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TicketSaleCreateResponse"]


class TicketSaleCreateResponse(BaseModel):
    """Full ticket sale model with ID."""

    id: str
    """Unique identifier"""

    buyer_name: str
    """Name of the ticket buyer"""

    currency: str
    """Currency code (GBP, USD, or EUR)"""

    discount: str
    """Discount amount applied from coupon"""

    match_id: str
    """ID of the match"""

    purchase_method: Literal["online", "box_office", "will_call", "phone"]
    """How the ticket was purchased"""

    quantity: int
    """Number of tickets purchased"""

    subtotal: str
    """Subtotal before discount and tax (unit_price \\** quantity)"""

    tax: str
    """Tax amount (20% UK VAT on discounted subtotal)"""

    total: str
    """Final total (subtotal - discount + tax)"""

    unit_price: str
    """Price per ticket (decimal string)"""

    buyer_email: Optional[str] = None
    """Email of the ticket buyer"""

    coupon_code: Optional[str] = None
    """Coupon code applied, if any"""
