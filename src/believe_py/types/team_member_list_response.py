# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .coach import Coach
from .player import Player
from .._utils import PropertyInfo
from .medical_staff import MedicalStaff
from .equipment_manager import EquipmentManager

__all__ = ["TeamMemberListResponse"]

TeamMemberListResponse: TypeAlias = Annotated[
    Union[Player, Coach, MedicalStaff, EquipmentManager], PropertyInfo(discriminator="member_type")
]
