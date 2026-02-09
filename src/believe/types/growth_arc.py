# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["GrowthArc"]


class GrowthArc(BaseModel):
    """Character development arc."""

    breakthrough: str
    """Key breakthrough moment"""

    challenge: str
    """Main challenge faced"""

    ending_point: str
    """Where the character ends up"""

    season: int
    """Season number"""

    starting_point: str
    """Where the character starts emotionally"""
