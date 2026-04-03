# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from ..._types import FileTypes

__all__ = ["LogoUploadParams"]

class LogoUploadParams(TypedDict, total=False):
    file: Required[FileTypes]
    """Logo image file"""