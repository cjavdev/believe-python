# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GeoLocationParam"]


class GeoLocationParam(TypedDict, total=False):
    """Geographic coordinates for a location."""

    latitude: Required[float]
    """Latitude in degrees"""

    longitude: Required[float]
    """Longitude in degrees"""
