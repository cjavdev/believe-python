# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .registered_webhook import RegisteredWebhook

__all__ = ["WebhookListResponse"]

WebhookListResponse: TypeAlias = List[RegisteredWebhook]
