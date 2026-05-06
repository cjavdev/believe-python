# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MatchStreamLiveParams"]


class MatchStreamLiveParams(TypedDict, total=False):
    away_team: str
    """Away team name"""

    excitement_level: int
    """How eventful the match should be (1=boring, 10=chaos)"""

    home_team: str
    """Home team name"""

    speed: float
    """Simulation speed multiplier (1.0 = real-time)"""
