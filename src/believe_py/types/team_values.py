# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["TeamValues"]


class TeamValues(BaseModel):
    """Core values that define a team's culture."""

    primary_value: str
    """The team's primary guiding value"""

    secondary_values: List[str]
    """Supporting values"""

    team_motto: str
    """Team's motivational motto"""
