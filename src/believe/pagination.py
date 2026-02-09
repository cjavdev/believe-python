# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncSkipLimitPage", "AsyncSkipLimitPage"]

_T = TypeVar("_T")


class SyncSkipLimitPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    total: Optional[int] = None
    skip: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        skip = self.skip
        if skip is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = skip + length

        total = self.total
        if total is None:
            return None

        if current_count < total:
            return PageInfo(params={"skip": current_count})

        return None


class AsyncSkipLimitPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    total: Optional[int] = None
    skip: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        skip = self.skip
        if skip is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = skip + length

        total = self.total
        if total is None:
            return None

        if current_count < total:
            return PageInfo(params={"skip": current_count})

        return None
