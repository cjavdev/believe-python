# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ..types import (
    QuoteTheme,
    QuoteMoment,
    quote_list_params,
    quote_create_params,
    quote_update_params,
    quote_get_random_params,
    quote_list_by_theme_params,
    quote_list_by_character_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncSkipLimitPage, AsyncSkipLimitPage
from ..types.quote import Quote
from .._base_client import AsyncPaginator, make_request_options
from ..types.quote_theme import QuoteTheme
from ..types.quote_moment import QuoteMoment

__all__ = ["QuotesResource", "AsyncQuotesResource"]


class QuotesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QuotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/believe-python#accessing-raw-response-data-eg-headers
        """
        return QuotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/believe-python#with_streaming_response
        """
        return QuotesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        character_id: str,
        context: str,
        moment_type: QuoteMoment,
        text: str,
        theme: QuoteTheme,
        episode_id: Optional[str] | Omit = omit,
        is_funny: bool | Omit = omit,
        is_inspirational: bool | Omit = omit,
        popularity_score: Optional[float] | Omit = omit,
        secondary_themes: List[QuoteTheme] | Omit = omit,
        times_shared: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Quote:
        """
        Add a new memorable quote to the collection.

        Args:
          character_id: ID of the character who said it

          context: Context in which the quote was said

          moment_type: Type of moment when the quote was said

          text: The quote text

          theme: Primary theme of the quote

          episode_id: Episode where the quote appears

          is_funny: Whether this quote is humorous

          is_inspirational: Whether this quote is inspirational

          popularity_score: Popularity/virality score (0-100)

          secondary_themes: Additional themes

          times_shared: Number of times shared on social media

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/quotes",
            body=maybe_transform(
                {
                    "character_id": character_id,
                    "context": context,
                    "moment_type": moment_type,
                    "text": text,
                    "theme": theme,
                    "episode_id": episode_id,
                    "is_funny": is_funny,
                    "is_inspirational": is_inspirational,
                    "popularity_score": popularity_score,
                    "secondary_themes": secondary_themes,
                    "times_shared": times_shared,
                },
                quote_create_params.QuoteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Quote,
        )

    def retrieve(
        self,
        quote_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Quote:
        """
        Retrieve a specific quote by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not quote_id:
            raise ValueError(f"Expected a non-empty value for `quote_id` but received {quote_id!r}")
        return self._get(
            f"/quotes/{quote_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Quote,
        )

    def update(
        self,
        quote_id: str,
        *,
        character_id: Optional[str] | Omit = omit,
        context: Optional[str] | Omit = omit,
        episode_id: Optional[str] | Omit = omit,
        is_funny: Optional[bool] | Omit = omit,
        is_inspirational: Optional[bool] | Omit = omit,
        moment_type: Optional[QuoteMoment] | Omit = omit,
        popularity_score: Optional[float] | Omit = omit,
        secondary_themes: Optional[List[QuoteTheme]] | Omit = omit,
        text: Optional[str] | Omit = omit,
        theme: Optional[QuoteTheme] | Omit = omit,
        times_shared: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Quote:
        """
        Update specific fields of an existing quote.

        Args:
          moment_type: Types of moments when quotes occur.

          theme: Themes that quotes can be categorized under.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not quote_id:
            raise ValueError(f"Expected a non-empty value for `quote_id` but received {quote_id!r}")
        return self._patch(
            f"/quotes/{quote_id}",
            body=maybe_transform(
                {
                    "character_id": character_id,
                    "context": context,
                    "episode_id": episode_id,
                    "is_funny": is_funny,
                    "is_inspirational": is_inspirational,
                    "moment_type": moment_type,
                    "popularity_score": popularity_score,
                    "secondary_themes": secondary_themes,
                    "text": text,
                    "theme": theme,
                    "times_shared": times_shared,
                },
                quote_update_params.QuoteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Quote,
        )

    def list(
        self,
        *,
        character_id: Optional[str] | Omit = omit,
        funny: Optional[bool] | Omit = omit,
        inspirational: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        moment_type: Optional[QuoteMoment] | Omit = omit,
        skip: int | Omit = omit,
        theme: Optional[QuoteTheme] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimitPage[Quote]:
        """
        Get a paginated list of all memorable Ted Lasso quotes with optional filtering.

        Args:
          character_id: Filter by character

          funny: Filter funny quotes

          inspirational: Filter inspirational quotes

          limit: Maximum number of items to return (max: 100)

          moment_type: Types of moments when quotes occur.

          skip: Number of items to skip (offset)

          theme: Themes that quotes can be categorized under.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/quotes",
            page=SyncSkipLimitPage[Quote],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "character_id": character_id,
                        "funny": funny,
                        "inspirational": inspirational,
                        "limit": limit,
                        "moment_type": moment_type,
                        "skip": skip,
                        "theme": theme,
                    },
                    quote_list_params.QuoteListParams,
                ),
            ),
            model=Quote,
        )

    def delete(
        self,
        quote_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a quote from the collection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not quote_id:
            raise ValueError(f"Expected a non-empty value for `quote_id` but received {quote_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/quotes/{quote_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_random(
        self,
        *,
        character_id: Optional[str] | Omit = omit,
        inspirational: Optional[bool] | Omit = omit,
        theme: Optional[QuoteTheme] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Quote:
        """
        Get a random Ted Lasso quote, optionally filtered.

        Args:
          character_id: Filter by character

          inspirational: Filter inspirational quotes

          theme: Themes that quotes can be categorized under.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/quotes/random",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "character_id": character_id,
                        "inspirational": inspirational,
                        "theme": theme,
                    },
                    quote_get_random_params.QuoteGetRandomParams,
                ),
            ),
            cast_to=Quote,
        )

    def list_by_character(
        self,
        character_id: str,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimitPage[Quote]:
        """
        Get a paginated list of quotes from a specific character.

        Args:
          limit: Maximum number of items to return (max: 100)

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not character_id:
            raise ValueError(f"Expected a non-empty value for `character_id` but received {character_id!r}")
        return self._get_api_list(
            f"/quotes/characters/{character_id}",
            page=SyncSkipLimitPage[Quote],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    quote_list_by_character_params.QuoteListByCharacterParams,
                ),
            ),
            model=Quote,
        )

    def list_by_theme(
        self,
        theme: QuoteTheme,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimitPage[Quote]:
        """
        Get a paginated list of quotes related to a specific theme.

        Args:
          theme: Themes that quotes can be categorized under.

          limit: Maximum number of items to return (max: 100)

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not theme:
            raise ValueError(f"Expected a non-empty value for `theme` but received {theme!r}")
        return self._get_api_list(
            f"/quotes/themes/{theme}",
            page=SyncSkipLimitPage[Quote],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    quote_list_by_theme_params.QuoteListByThemeParams,
                ),
            ),
            model=Quote,
        )


class AsyncQuotesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQuotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQuotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/believe-python#with_streaming_response
        """
        return AsyncQuotesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        character_id: str,
        context: str,
        moment_type: QuoteMoment,
        text: str,
        theme: QuoteTheme,
        episode_id: Optional[str] | Omit = omit,
        is_funny: bool | Omit = omit,
        is_inspirational: bool | Omit = omit,
        popularity_score: Optional[float] | Omit = omit,
        secondary_themes: List[QuoteTheme] | Omit = omit,
        times_shared: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Quote:
        """
        Add a new memorable quote to the collection.

        Args:
          character_id: ID of the character who said it

          context: Context in which the quote was said

          moment_type: Type of moment when the quote was said

          text: The quote text

          theme: Primary theme of the quote

          episode_id: Episode where the quote appears

          is_funny: Whether this quote is humorous

          is_inspirational: Whether this quote is inspirational

          popularity_score: Popularity/virality score (0-100)

          secondary_themes: Additional themes

          times_shared: Number of times shared on social media

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/quotes",
            body=await async_maybe_transform(
                {
                    "character_id": character_id,
                    "context": context,
                    "moment_type": moment_type,
                    "text": text,
                    "theme": theme,
                    "episode_id": episode_id,
                    "is_funny": is_funny,
                    "is_inspirational": is_inspirational,
                    "popularity_score": popularity_score,
                    "secondary_themes": secondary_themes,
                    "times_shared": times_shared,
                },
                quote_create_params.QuoteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Quote,
        )

    async def retrieve(
        self,
        quote_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Quote:
        """
        Retrieve a specific quote by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not quote_id:
            raise ValueError(f"Expected a non-empty value for `quote_id` but received {quote_id!r}")
        return await self._get(
            f"/quotes/{quote_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Quote,
        )

    async def update(
        self,
        quote_id: str,
        *,
        character_id: Optional[str] | Omit = omit,
        context: Optional[str] | Omit = omit,
        episode_id: Optional[str] | Omit = omit,
        is_funny: Optional[bool] | Omit = omit,
        is_inspirational: Optional[bool] | Omit = omit,
        moment_type: Optional[QuoteMoment] | Omit = omit,
        popularity_score: Optional[float] | Omit = omit,
        secondary_themes: Optional[List[QuoteTheme]] | Omit = omit,
        text: Optional[str] | Omit = omit,
        theme: Optional[QuoteTheme] | Omit = omit,
        times_shared: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Quote:
        """
        Update specific fields of an existing quote.

        Args:
          moment_type: Types of moments when quotes occur.

          theme: Themes that quotes can be categorized under.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not quote_id:
            raise ValueError(f"Expected a non-empty value for `quote_id` but received {quote_id!r}")
        return await self._patch(
            f"/quotes/{quote_id}",
            body=await async_maybe_transform(
                {
                    "character_id": character_id,
                    "context": context,
                    "episode_id": episode_id,
                    "is_funny": is_funny,
                    "is_inspirational": is_inspirational,
                    "moment_type": moment_type,
                    "popularity_score": popularity_score,
                    "secondary_themes": secondary_themes,
                    "text": text,
                    "theme": theme,
                    "times_shared": times_shared,
                },
                quote_update_params.QuoteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Quote,
        )

    def list(
        self,
        *,
        character_id: Optional[str] | Omit = omit,
        funny: Optional[bool] | Omit = omit,
        inspirational: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        moment_type: Optional[QuoteMoment] | Omit = omit,
        skip: int | Omit = omit,
        theme: Optional[QuoteTheme] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Quote, AsyncSkipLimitPage[Quote]]:
        """
        Get a paginated list of all memorable Ted Lasso quotes with optional filtering.

        Args:
          character_id: Filter by character

          funny: Filter funny quotes

          inspirational: Filter inspirational quotes

          limit: Maximum number of items to return (max: 100)

          moment_type: Types of moments when quotes occur.

          skip: Number of items to skip (offset)

          theme: Themes that quotes can be categorized under.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/quotes",
            page=AsyncSkipLimitPage[Quote],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "character_id": character_id,
                        "funny": funny,
                        "inspirational": inspirational,
                        "limit": limit,
                        "moment_type": moment_type,
                        "skip": skip,
                        "theme": theme,
                    },
                    quote_list_params.QuoteListParams,
                ),
            ),
            model=Quote,
        )

    async def delete(
        self,
        quote_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a quote from the collection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not quote_id:
            raise ValueError(f"Expected a non-empty value for `quote_id` but received {quote_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/quotes/{quote_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_random(
        self,
        *,
        character_id: Optional[str] | Omit = omit,
        inspirational: Optional[bool] | Omit = omit,
        theme: Optional[QuoteTheme] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Quote:
        """
        Get a random Ted Lasso quote, optionally filtered.

        Args:
          character_id: Filter by character

          inspirational: Filter inspirational quotes

          theme: Themes that quotes can be categorized under.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/quotes/random",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "character_id": character_id,
                        "inspirational": inspirational,
                        "theme": theme,
                    },
                    quote_get_random_params.QuoteGetRandomParams,
                ),
            ),
            cast_to=Quote,
        )

    def list_by_character(
        self,
        character_id: str,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Quote, AsyncSkipLimitPage[Quote]]:
        """
        Get a paginated list of quotes from a specific character.

        Args:
          limit: Maximum number of items to return (max: 100)

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not character_id:
            raise ValueError(f"Expected a non-empty value for `character_id` but received {character_id!r}")
        return self._get_api_list(
            f"/quotes/characters/{character_id}",
            page=AsyncSkipLimitPage[Quote],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    quote_list_by_character_params.QuoteListByCharacterParams,
                ),
            ),
            model=Quote,
        )

    def list_by_theme(
        self,
        theme: QuoteTheme,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Quote, AsyncSkipLimitPage[Quote]]:
        """
        Get a paginated list of quotes related to a specific theme.

        Args:
          theme: Themes that quotes can be categorized under.

          limit: Maximum number of items to return (max: 100)

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not theme:
            raise ValueError(f"Expected a non-empty value for `theme` but received {theme!r}")
        return self._get_api_list(
            f"/quotes/themes/{theme}",
            page=AsyncSkipLimitPage[Quote],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    quote_list_by_theme_params.QuoteListByThemeParams,
                ),
            ),
            model=Quote,
        )


class QuotesResourceWithRawResponse:
    def __init__(self, quotes: QuotesResource) -> None:
        self._quotes = quotes

        self.create = to_raw_response_wrapper(
            quotes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            quotes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            quotes.update,
        )
        self.list = to_raw_response_wrapper(
            quotes.list,
        )
        self.delete = to_raw_response_wrapper(
            quotes.delete,
        )
        self.get_random = to_raw_response_wrapper(
            quotes.get_random,
        )
        self.list_by_character = to_raw_response_wrapper(
            quotes.list_by_character,
        )
        self.list_by_theme = to_raw_response_wrapper(
            quotes.list_by_theme,
        )


class AsyncQuotesResourceWithRawResponse:
    def __init__(self, quotes: AsyncQuotesResource) -> None:
        self._quotes = quotes

        self.create = async_to_raw_response_wrapper(
            quotes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            quotes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            quotes.update,
        )
        self.list = async_to_raw_response_wrapper(
            quotes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            quotes.delete,
        )
        self.get_random = async_to_raw_response_wrapper(
            quotes.get_random,
        )
        self.list_by_character = async_to_raw_response_wrapper(
            quotes.list_by_character,
        )
        self.list_by_theme = async_to_raw_response_wrapper(
            quotes.list_by_theme,
        )


class QuotesResourceWithStreamingResponse:
    def __init__(self, quotes: QuotesResource) -> None:
        self._quotes = quotes

        self.create = to_streamed_response_wrapper(
            quotes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            quotes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            quotes.update,
        )
        self.list = to_streamed_response_wrapper(
            quotes.list,
        )
        self.delete = to_streamed_response_wrapper(
            quotes.delete,
        )
        self.get_random = to_streamed_response_wrapper(
            quotes.get_random,
        )
        self.list_by_character = to_streamed_response_wrapper(
            quotes.list_by_character,
        )
        self.list_by_theme = to_streamed_response_wrapper(
            quotes.list_by_theme,
        )


class AsyncQuotesResourceWithStreamingResponse:
    def __init__(self, quotes: AsyncQuotesResource) -> None:
        self._quotes = quotes

        self.create = async_to_streamed_response_wrapper(
            quotes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            quotes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            quotes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            quotes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            quotes.delete,
        )
        self.get_random = async_to_streamed_response_wrapper(
            quotes.get_random,
        )
        self.list_by_character = async_to_streamed_response_wrapper(
            quotes.list_by_character,
        )
        self.list_by_theme = async_to_streamed_response_wrapper(
            quotes.list_by_theme,
        )
