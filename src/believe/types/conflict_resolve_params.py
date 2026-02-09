# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ConflictResolveParams"]


class ConflictResolveParams(TypedDict, total=False):
    conflict_type: Required[
        Literal["interpersonal", "team_dynamics", "leadership", "ego", "miscommunication", "competition"]
    ]
    """Type of conflict"""

    description: Required[str]
    """Describe the conflict"""

    parties_involved: Required[SequenceNotStr[str]]
    """Who is involved in the conflict"""

    attempts_made: Optional[SequenceNotStr[str]]
    """What you've already tried"""
