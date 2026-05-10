# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .match_completed_webhook_event import MatchCompletedWebhookEvent
from .team_member_transferred_webhook_event import TeamMemberTransferredWebhookEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Union[MatchCompletedWebhookEvent, TeamMemberTransferredWebhookEvent]
