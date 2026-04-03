# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

__all__ = ["PressSimulateResponse"]

class PressSimulateResponse(BaseModel):
    """Ted's press conference response."""
    actual_wisdom: str
    """The actual wisdom beneath the humor"""

    follow_up_dodge: str
    """How Ted would dodge a follow-up"""

    reporter_reaction: str
    """How reporters would react"""

    response: str
    """Ted's press conference answer"""

    deflection_humor: Optional[str] = None
    """Humorous deflection if appropriate"""