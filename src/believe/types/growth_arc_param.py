# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GrowthArcParam"]


class GrowthArcParam(TypedDict, total=False):
    """Character development arc."""

    breakthrough: Required[str]
    """Key breakthrough moment"""

    challenge: Required[str]
    """Main challenge faced"""

    ending_point: Required[str]
    """Where the character ends up"""

    season: Required[int]
    """Season number"""

    starting_point: Required[str]
    """Where the character starts emotionally"""
