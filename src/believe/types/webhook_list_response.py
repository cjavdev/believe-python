# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .registered_webhook import RegisteredWebhook

from typing_extensions import TypeAliasType, TypeAlias

__all__ = ["WebhookListResponse"]

WebhookListResponse: TypeAlias = List[RegisteredWebhook]