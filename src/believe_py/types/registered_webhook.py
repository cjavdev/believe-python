# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RegisteredWebhook"]


class RegisteredWebhook(BaseModel):
    """A registered webhook endpoint."""

    id: str
    """Unique webhook identifier"""

    created_at: datetime
    """When the webhook was registered"""

    event_types: List[Literal["match.completed", "team_member.transferred"]]
    """List of event types this webhook is subscribed to"""

    secret: str
    """The secret key for verifying webhook signatures (base64 encoded)"""

    url: str
    """The URL to send webhook events to"""

    description: Optional[str] = None
    """Optional description for this webhook"""
