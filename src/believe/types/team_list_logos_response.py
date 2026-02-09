# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .teams.file_upload import FileUpload

__all__ = ["TeamListLogosResponse"]

TeamListLogosResponse: TypeAlias = List[FileUpload]
