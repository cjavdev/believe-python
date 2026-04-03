# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .teams.file_upload import FileUpload

from typing_extensions import TypeAliasType, TypeAlias

__all__ = ["TeamListLogosResponse"]

TeamListLogosResponse: TypeAlias = List[FileUpload]