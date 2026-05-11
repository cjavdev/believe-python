# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .medical_staff import MedicalStaff
from .equipment_manager import EquipmentManager

__all__ = ["TeamMemberListStaffResponse"]

TeamMemberListStaffResponse: TypeAlias = Union[MedicalStaff, EquipmentManager]
