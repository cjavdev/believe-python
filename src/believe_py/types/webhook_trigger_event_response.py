# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebhookTriggerEventResponse", "Delivery"]


class Delivery(BaseModel):
    """Result of delivering a webhook to a single endpoint."""

    success: bool
    """Whether delivery was successful"""

    url: str
    """URL the webhook was sent to"""

    webhook_id: str
    """ID of the webhook"""

    error: Optional[str] = None
    """Error message if delivery failed"""

    status_code: Optional[int] = None
    """HTTP status code from the endpoint"""


class WebhookTriggerEventResponse(BaseModel):
    """Response after triggering webhook events."""

    deliveries: List[Delivery]
    """Results of webhook deliveries"""

    event_id: str
    """Unique event identifier"""

    event_type: Literal["match.completed", "team_member.transferred"]
    """The type of event triggered"""

    successful_deliveries: int
    """Number of successful deliveries"""

    ted_says: str
    """Ted's reaction"""

    total_webhooks: int
    """Total number of webhooks that received this event"""
