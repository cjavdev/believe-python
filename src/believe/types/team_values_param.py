# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["TeamValuesParam"]


class TeamValuesParam(TypedDict, total=False):
    """Core values that define a team's culture."""

    primary_value: Required[str]
    """The team's primary guiding value"""

    secondary_values: Required[SequenceNotStr[str]]
    """Supporting values"""

    team_motto: Required[str]
    """Team's motivational motto"""
