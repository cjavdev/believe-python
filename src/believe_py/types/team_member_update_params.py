# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .position import Position
from .coach_specialty import CoachSpecialty
from .medical_specialty import MedicalSpecialty

__all__ = [
    "TeamMemberUpdateParams",
    "Updates",
    "UpdatesPlayerUpdate",
    "UpdatesCoachUpdate",
    "UpdatesMedicalStaffUpdate",
    "UpdatesEquipmentManagerUpdate",
]


class TeamMemberUpdateParams(TypedDict, total=False):
    updates: Required[Updates]
    """Update model for players."""


class UpdatesPlayerUpdate(TypedDict, total=False):
    """Update model for players."""

    assists: Optional[int]

    goals_scored: Optional[int]

    is_captain: Optional[bool]

    jersey_number: Optional[int]

    position: Optional[Position]
    """Football positions for players."""

    team_id: Optional[str]

    years_with_team: Optional[int]


class UpdatesCoachUpdate(TypedDict, total=False):
    """Update model for coaches."""

    certifications: Optional[SequenceNotStr[str]]

    specialty: Optional[CoachSpecialty]
    """Coaching specialties."""

    team_id: Optional[str]

    win_rate: Optional[float]

    years_with_team: Optional[int]


class UpdatesMedicalStaffUpdate(TypedDict, total=False):
    """Update model for medical staff."""

    license_number: Optional[str]

    qualifications: Optional[SequenceNotStr[str]]

    specialty: Optional[MedicalSpecialty]
    """Medical staff specialties."""

    team_id: Optional[str]

    years_with_team: Optional[int]


class UpdatesEquipmentManagerUpdate(TypedDict, total=False):
    """Update model for equipment managers."""

    is_head_kitman: Optional[bool]

    responsibilities: Optional[SequenceNotStr[str]]

    team_id: Optional[str]

    years_with_team: Optional[int]


Updates: TypeAlias = Union[
    UpdatesPlayerUpdate, UpdatesCoachUpdate, UpdatesMedicalStaffUpdate, UpdatesEquipmentManagerUpdate
]
