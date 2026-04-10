# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

__all__ = ["FileUpload"]

class FileUpload(BaseModel):
    """Response model for file uploads."""
    checksum_sha256: str

    content_type: str

    file_id: str

    filename: str

    size_bytes: int

    uploaded_at: datetime