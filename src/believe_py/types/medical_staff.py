# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .medical_specialty import MedicalSpecialty

__all__ = ["MedicalStaff"]


class MedicalStaff(BaseModel):
    """Full medical staff model with ID."""

    id: str
    """Unique identifier for this team membership"""

    character_id: str
    """ID of the character (references /characters/{id})"""

    specialty: MedicalSpecialty
    """Medical specialty"""

    team_id: str
    """ID of the team they belong to"""

    years_with_team: int
    """Number of years with the current team"""

    license_number: Optional[str] = None
    """Professional license number"""

    member_type: Optional[Literal["medical_staff"]] = None
    """Discriminator field indicating this is medical staff"""

    qualifications: Optional[List[str]] = None
    """Medical qualifications and degrees"""
