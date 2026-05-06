# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EquipmentManager"]


class EquipmentManager(BaseModel):
    """Full equipment manager model with ID."""

    id: str
    """Unique identifier for this team membership"""

    character_id: str
    """ID of the character (references /characters/{id})"""

    team_id: str
    """ID of the team they belong to"""

    years_with_team: int
    """Number of years with the current team"""

    is_head_kitman: Optional[bool] = None
    """Whether this is the head equipment manager"""

    member_type: Optional[Literal["equipment_manager"]] = None
    """Discriminator field indicating this is an equipment manager"""

    responsibilities: Optional[List[str]] = None
    """List of responsibilities"""
