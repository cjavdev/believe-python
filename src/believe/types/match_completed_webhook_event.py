# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MatchCompletedWebhookEvent", "Data"]


class Data(BaseModel):
    """Data payload for a match completed event."""

    away_score: int
    """Final away team score"""

    away_team_id: str
    """Away team ID"""

    completed_at: datetime
    """When the match completed"""

    home_score: int
    """Final home team score"""

    home_team_id: str
    """Home team ID"""

    match_id: str
    """Unique match identifier"""

    match_type: Literal["league", "cup", "friendly", "playoff", "final"]
    """Type of match"""

    result: Literal["home_win", "away_win", "draw"]
    """Match result from home team perspective"""

    ted_post_match_quote: str
    """Ted's post-match wisdom"""

    lesson_learned: Optional[str] = None
    """Ted's lesson from the match"""

    man_of_the_match: Optional[str] = None
    """Player of the match (if awarded)"""


class MatchCompletedWebhookEvent(BaseModel):
    """Webhook event sent when a match completes."""

    created_at: datetime
    """When the event was created"""

    data: Data
    """Data payload for a match completed event."""

    event_id: str
    """Unique identifier for this event"""

    event_type: Literal["match.completed"]
    """The type of webhook event"""
