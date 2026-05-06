# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ReframeTransformNegativeThoughtsParams"]


class ReframeTransformNegativeThoughtsParams(TypedDict, total=False):
    negative_thought: Required[str]
    """The negative thought to reframe"""

    recurring: bool
    """Is this a recurring thought?"""
