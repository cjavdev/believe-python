# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .principles import (
    PrinciplesResource,
    AsyncPrinciplesResource,
    PrinciplesResourceWithRawResponse,
    AsyncPrinciplesResourceWithRawResponse,
    PrinciplesResourceWithStreamingResponse,
    AsyncPrinciplesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CoachingResource", "AsyncCoachingResource"]


class CoachingResource(SyncAPIResource):
    @cached_property
    def principles(self) -> PrinciplesResource:
        return PrinciplesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CoachingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/believe-python#accessing-raw-response-data-eg-headers
        """
        return CoachingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CoachingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/believe-python#with_streaming_response
        """
        return CoachingResourceWithStreamingResponse(self)


class AsyncCoachingResource(AsyncAPIResource):
    @cached_property
    def principles(self) -> AsyncPrinciplesResource:
        return AsyncPrinciplesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCoachingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCoachingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCoachingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/believe-python#with_streaming_response
        """
        return AsyncCoachingResourceWithStreamingResponse(self)


class CoachingResourceWithRawResponse:
    def __init__(self, coaching: CoachingResource) -> None:
        self._coaching = coaching

    @cached_property
    def principles(self) -> PrinciplesResourceWithRawResponse:
        return PrinciplesResourceWithRawResponse(self._coaching.principles)


class AsyncCoachingResourceWithRawResponse:
    def __init__(self, coaching: AsyncCoachingResource) -> None:
        self._coaching = coaching

    @cached_property
    def principles(self) -> AsyncPrinciplesResourceWithRawResponse:
        return AsyncPrinciplesResourceWithRawResponse(self._coaching.principles)


class CoachingResourceWithStreamingResponse:
    def __init__(self, coaching: CoachingResource) -> None:
        self._coaching = coaching

    @cached_property
    def principles(self) -> PrinciplesResourceWithStreamingResponse:
        return PrinciplesResourceWithStreamingResponse(self._coaching.principles)


class AsyncCoachingResourceWithStreamingResponse:
    def __init__(self, coaching: AsyncCoachingResource) -> None:
        self._coaching = coaching

    @cached_property
    def principles(self) -> AsyncPrinciplesResourceWithStreamingResponse:
        return AsyncPrinciplesResourceWithStreamingResponse(self._coaching.principles)
