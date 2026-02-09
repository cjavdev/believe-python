# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PepTalkRetrieveResponse", "Chunk"]


class Chunk(BaseModel):
    """A chunk of a streaming pep talk from Ted."""

    chunk_id: int
    """Chunk sequence number"""

    is_final: bool
    """Is this the final chunk"""

    text: str
    """The text of this chunk"""

    emotional_beat: Optional[str] = None
    """
    The emotional purpose of this chunk (e.g., greeting, acknowledgment, wisdom,
    affirmation, encouragement)
    """


class PepTalkRetrieveResponse(BaseModel):
    """A complete pep talk response."""

    chunks: List[Chunk]
    """Individual chunks of the pep talk"""

    text: str
    """The full pep talk text"""
