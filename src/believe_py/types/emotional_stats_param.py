# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EmotionalStatsParam"]


class EmotionalStatsParam(TypedDict, total=False):
    """Emotional intelligence statistics for a character."""

    curiosity: Required[int]
    """Level of curiosity over judgment (0-100)"""

    empathy: Required[int]
    """Capacity for empathy (0-100)"""

    optimism: Required[int]
    """Level of optimism (0-100)"""

    resilience: Required[int]
    """Bounce-back ability (0-100)"""

    vulnerability: Required[int]
    """Willingness to be vulnerable (0-100)"""
