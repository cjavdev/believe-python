# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    url: Required[str]
    """The URL to send webhook events to"""

    description: Optional[str]
    """Optional description for this webhook"""

    event_types: Optional[List[Literal["match.completed", "team_member.transferred"]]]
    """List of event types to subscribe to. If not provided, subscribes to all events."""
