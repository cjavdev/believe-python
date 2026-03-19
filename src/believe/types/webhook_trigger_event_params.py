# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "WebhookTriggerEventParams",
    "Payload",
    "PayloadMatchCompletedPayload",
    "PayloadMatchCompletedPayloadData",
    "PayloadTeamMemberTransferredPayload",
    "PayloadTeamMemberTransferredPayloadData",
]


class WebhookTriggerEventParams(TypedDict, total=False):
    event_type: Required[Literal["match.completed", "team_member.transferred"]]
    """The type of event to trigger"""

    payload: Optional[Payload]
    """Optional event payload. If not provided, a sample payload will be generated."""


class PayloadMatchCompletedPayloadData(TypedDict, total=False):
    """Event data"""

    away_score: Required[int]
    """Final away team score"""

    away_team_id: Required[str]
    """Away team ID"""

    completed_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """When the match completed"""

    home_score: Required[int]
    """Final home team score"""

    home_team_id: Required[str]
    """Home team ID"""

    match_id: Required[str]
    """Unique match identifier"""

    match_type: Required[Literal["league", "cup", "friendly", "playoff", "final"]]
    """Type of match"""

    result: Required[Literal["home_win", "away_win", "draw"]]
    """Match result from home team perspective"""

    ted_post_match_quote: Required[str]
    """Ted's post-match wisdom"""

    lesson_learned: Optional[str]
    """Ted's lesson from the match"""

    man_of_the_match: Optional[str]
    """Player of the match (if awarded)"""


class PayloadMatchCompletedPayload(TypedDict, total=False):
    """Payload for match.completed event."""

    data: Required[PayloadMatchCompletedPayloadData]
    """Event data"""

    event_type: Literal["match.completed"]
    """The type of webhook event"""


class PayloadTeamMemberTransferredPayloadData(TypedDict, total=False):
    """Event data"""

    character_id: Required[str]
    """ID of the character (links to /characters)"""

    character_name: Required[str]
    """Name of the character"""

    member_type: Required[Literal["player", "coach", "medical_staff", "equipment_manager"]]
    """Type of team member"""

    team_id: Required[str]
    """ID of the team involved"""

    team_member_id: Required[str]
    """ID of the team member"""

    team_name: Required[str]
    """Name of the team involved"""

    ted_reaction: Required[str]
    """Ted's reaction to the transfer"""

    transfer_type: Required[Literal["joined", "departed"]]
    """Whether the member joined or departed"""

    previous_team_id: Optional[str]
    """Previous team ID (for joins from another team)"""

    previous_team_name: Optional[str]
    """Previous team name (for joins from another team)"""

    transfer_fee_gbp: Optional[str]
    """Transfer fee in GBP (for players)"""

    years_with_previous_team: Optional[int]
    """Years spent with previous team"""


class PayloadTeamMemberTransferredPayload(TypedDict, total=False):
    """Payload for team_member.transferred event."""

    data: Required[PayloadTeamMemberTransferredPayloadData]
    """Event data"""

    event_type: Literal["team_member.transferred"]
    """The type of webhook event"""


Payload: TypeAlias = Union[PayloadMatchCompletedPayload, PayloadTeamMemberTransferredPayload]
