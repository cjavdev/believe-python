# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .position import Position
from .coach_specialty import CoachSpecialty
from .medical_specialty import MedicalSpecialty

__all__ = [
    "TeamMemberCreateParams",
    "Member",
    "MemberPlayerBase",
    "MemberCoachBase",
    "MemberMedicalStaffBase",
    "MemberEquipmentManagerBase",
]


class TeamMemberCreateParams(TypedDict, total=False):
    member: Required[Member]
    """A football player on the team."""


class MemberPlayerBase(TypedDict, total=False):
    """A football player on the team."""

    character_id: Required[str]
    """ID of the character (references /characters/{id})"""

    jersey_number: Required[int]
    """Jersey/shirt number"""

    position: Required[Position]
    """Playing position on the field"""

    team_id: Required[str]
    """ID of the team they belong to"""

    years_with_team: Required[int]
    """Number of years with the current team"""

    assists: int
    """Total assists for the team"""

    goals_scored: int
    """Total goals scored for the team"""

    is_captain: bool
    """Whether this player is team captain"""

    member_type: Literal["player"]
    """Discriminator field indicating this is a player"""


class MemberCoachBase(TypedDict, total=False):
    """A coach or coaching staff member."""

    character_id: Required[str]
    """ID of the character (references /characters/{id})"""

    specialty: Required[CoachSpecialty]
    """Coaching specialty/role"""

    team_id: Required[str]
    """ID of the team they belong to"""

    years_with_team: Required[int]
    """Number of years with the current team"""

    certifications: SequenceNotStr[str]
    """Coaching certifications and licenses"""

    member_type: Literal["coach"]
    """Discriminator field indicating this is a coach"""

    win_rate: Optional[float]
    """Career win rate (0.0 to 1.0)"""


class MemberMedicalStaffBase(TypedDict, total=False):
    """Medical and wellness staff member."""

    character_id: Required[str]
    """ID of the character (references /characters/{id})"""

    specialty: Required[MedicalSpecialty]
    """Medical specialty"""

    team_id: Required[str]
    """ID of the team they belong to"""

    years_with_team: Required[int]
    """Number of years with the current team"""

    license_number: Optional[str]
    """Professional license number"""

    member_type: Literal["medical_staff"]
    """Discriminator field indicating this is medical staff"""

    qualifications: SequenceNotStr[str]
    """Medical qualifications and degrees"""


class MemberEquipmentManagerBase(TypedDict, total=False):
    """Equipment and kit management staff."""

    character_id: Required[str]
    """ID of the character (references /characters/{id})"""

    team_id: Required[str]
    """ID of the team they belong to"""

    years_with_team: Required[int]
    """Number of years with the current team"""

    is_head_kitman: bool
    """Whether this is the head equipment manager"""

    member_type: Literal["equipment_manager"]
    """Discriminator field indicating this is an equipment manager"""

    responsibilities: SequenceNotStr[str]
    """List of responsibilities"""


Member: TypeAlias = Union[MemberPlayerBase, MemberCoachBase, MemberMedicalStaffBase, MemberEquipmentManagerBase]
