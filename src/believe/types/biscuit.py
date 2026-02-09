# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Biscuit"]


class Biscuit(BaseModel):
    """A biscuit from Ted."""

    id: str
    """Biscuit identifier"""

    message: str
    """Message that comes with the biscuit"""

    pairs_well_with: str
    """What this biscuit pairs well with"""

    ted_note: str
    """A handwritten note from Ted"""

    type: Literal["classic", "shortbread", "chocolate_chip", "oatmeal_raisin"]
    """Type of biscuit"""

    warmth_level: int
    """How warm and fresh (1-10)"""
