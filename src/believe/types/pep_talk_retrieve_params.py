# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PepTalkRetrieveParams"]


class PepTalkRetrieveParams(TypedDict, total=False):
    stream: bool
    """If true, returns SSE stream instead of full response"""
