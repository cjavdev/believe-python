# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .registered_webhook import RegisteredWebhook

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(BaseModel):
    """Response after registering a webhook."""

    webhook: RegisteredWebhook
    """The registered webhook details"""

    message: Optional[str] = None
    """Status message"""

    ted_says: Optional[str] = None
    """Ted's reaction"""
