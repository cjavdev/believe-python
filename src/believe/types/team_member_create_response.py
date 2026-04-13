# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .player import Player

from .coach import Coach

from .medical_staff import MedicalStaff

from .equipment_manager import EquipmentManager

from .._utils import PropertyInfo

from typing_extensions import Annotated, TypeAliasType, TypeAlias

__all__ = ["TeamMemberCreateResponse"]

TeamMemberCreateResponse: TypeAlias = Annotated[Union[Player, Coach, MedicalStaff, EquipmentManager], PropertyInfo(discriminator="member_type")]