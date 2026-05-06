# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PressSimulateParams"]


class PressSimulateParams(TypedDict, total=False):
    question: Required[str]
    """The press question to answer"""

    hostile: bool
    """Is this a hostile question from Trent Crimm?"""

    topic: Optional[str]
    """Topic category"""
