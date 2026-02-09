# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["GeoLocation"]


class GeoLocation(BaseModel):
    """Geographic coordinates for a location."""

    latitude: float
    """Latitude in degrees"""

    longitude: float
    """Longitude in degrees"""
