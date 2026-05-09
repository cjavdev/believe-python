# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .._models import BaseModel

__all__ = ["Episode"]


class Episode(BaseModel):
    """Full episode model with ID."""

    id: str
    """Unique identifier (format: s##e##)"""

    air_date: date
    """Original air date"""

    character_focus: List[str]
    """Characters with significant development"""

    director: str
    """Episode director"""

    episode_number: int
    """Episode number within season"""

    main_theme: str
    """Central theme of the episode"""

    runtime_minutes: int
    """Episode runtime in minutes"""

    season: int
    """Season number"""

    synopsis: str
    """Brief plot synopsis"""

    ted_wisdom: str
    """Key piece of Ted wisdom from the episode"""

    title: str
    """Episode title"""

    writer: str
    """Episode writer(s)"""

    biscuits_with_boss_moment: Optional[str] = None
    """Notable biscuits with the boss scene"""

    memorable_moments: Optional[List[str]] = None
    """Standout moments from the episode"""

    us_viewers_millions: Optional[float] = None
    """US viewership in millions"""

    viewer_rating: Optional[float] = None
    """Viewer rating out of 10"""
