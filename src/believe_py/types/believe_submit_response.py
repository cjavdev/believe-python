# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BelieveSubmitResponse"]


class BelieveSubmitResponse(BaseModel):
    """Response from the Believe Engine."""

    action_suggestion: str
    """Suggested action to take"""

    believe_score: int
    """Your current believe-o-meter score"""

    goldfish_wisdom: str
    """A reminder to have a goldfish memory when needed"""

    relevant_quote: str
    """A relevant Ted Lasso quote"""

    ted_response: str
    """Ted's motivational response"""
