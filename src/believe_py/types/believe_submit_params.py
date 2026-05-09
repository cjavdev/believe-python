# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BelieveSubmitParams"]


class BelieveSubmitParams(TypedDict, total=False):
    situation: Required[str]
    """Describe your situation"""

    situation_type: Required[
        Literal[
            "work_challenge",
            "personal_setback",
            "team_conflict",
            "self_doubt",
            "big_decision",
            "failure",
            "new_beginning",
            "relationship",
        ]
    ]
    """Type of situation"""

    context: Optional[str]
    """Additional context"""

    intensity: int
    """How intense is the response needed (1=gentle, 10=full Ted)"""
