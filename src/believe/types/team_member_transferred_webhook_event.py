# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TeamMemberTransferredWebhookEvent", "Data"]


class Data(BaseModel):
    """Data payload for a team member transfer event."""

    character_id: str
    """ID of the character (links to /characters)"""

    character_name: str
    """Name of the character"""

    member_type: Literal["player", "coach", "medical_staff", "equipment_manager"]
    """Type of team member"""

    team_id: str
    """ID of the team involved"""

    team_member_id: str
    """ID of the team member"""

    team_name: str
    """Name of the team involved"""

    ted_reaction: str
    """Ted's reaction to the transfer"""

    transfer_type: Literal["joined", "departed"]
    """Whether the member joined or departed"""

    previous_team_id: Optional[str] = None
    """Previous team ID (for joins from another team)"""

    previous_team_name: Optional[str] = None
    """Previous team name (for joins from another team)"""

    transfer_fee_gbp: Optional[str] = None
    """Transfer fee in GBP (for players)"""

    years_with_previous_team: Optional[int] = None
    """Years spent with previous team"""


class TeamMemberTransferredWebhookEvent(BaseModel):
    """
    Webhook event sent when a team member (player, coach, staff) transfers between teams.
    """

    created_at: datetime
    """When the event was created"""

    data: Data
    """Data payload for a team member transfer event."""

    event_id: str
    """Unique identifier for this event"""

    event_type: Literal["team_member.transferred"]
    """The type of webhook event"""
