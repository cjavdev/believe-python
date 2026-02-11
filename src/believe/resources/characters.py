# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date

import httpx

from ..types import (
    CharacterRole,
    character_list_params,
    character_create_params,
    character_update_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from .._base_client import AsyncPaginator, make_request_options
from ..types.character import Character
from ..types.character_role import CharacterRole
from ..types.growth_arc_param import GrowthArcParam
from ..types.emotional_stats_param import EmotionalStatsParam
from ..types.character_get_quotes_response import CharacterGetQuotesResponse

__all__ = ["CharactersResource", "AsyncCharactersResource"]


class CharactersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CharactersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return CharactersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CharactersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return CharactersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        background: str,
        emotional_stats: EmotionalStatsParam,
        name: str,
        personality_traits: SequenceNotStr[str],
        role: CharacterRole,
        date_of_birth: Union[str, date, None] | Omit = omit,
        email: Optional[str] | Omit = omit,
        growth_arcs: Iterable[GrowthArcParam] | Omit = omit,
        height_meters: Optional[float] | Omit = omit,
        profile_image_url: Optional[str] | Omit = omit,
        salary_gbp: Union[float, str, None] | Omit = omit,
        signature_quotes: SequenceNotStr[str] | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Character:
        """
        Add a new character to the Ted Lasso universe.

        Args:
          background: Character background and history

          emotional_stats: Emotional intelligence stats

          name: Character's full name

          personality_traits: Key personality traits

          role: Character's role

          date_of_birth: Character's date of birth

          email: Character's email address

          growth_arcs: Character development across seasons

          height_meters: Height in meters

          profile_image_url: URL to character's profile image

          salary_gbp: Annual salary in GBP

          signature_quotes: Memorable quotes from this character

          team_id: ID of the team they belong to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/characters",
            body=maybe_transform(
                {
                    "background": background,
                    "emotional_stats": emotional_stats,
                    "name": name,
                    "personality_traits": personality_traits,
                    "role": role,
                    "date_of_birth": date_of_birth,
                    "email": email,
                    "growth_arcs": growth_arcs,
                    "height_meters": height_meters,
                    "profile_image_url": profile_image_url,
                    "salary_gbp": salary_gbp,
                    "signature_quotes": signature_quotes,
                    "team_id": team_id,
                },
                character_create_params.CharacterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Character,
        )

    def retrieve(
        self,
        character_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Character:
        """
        Retrieve detailed information about a specific character.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not character_id:
            raise ValueError(f"Expected a non-empty value for `character_id` but received {character_id!r}")
        return self._get(
            f"/characters/{character_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Character,
        )

    def update(
        self,
        character_id: str,
        *,
        background: Optional[str] | Omit = omit,
        date_of_birth: Union[str, date, None] | Omit = omit,
        email: Optional[str] | Omit = omit,
        emotional_stats: Optional[EmotionalStatsParam] | Omit = omit,
        growth_arcs: Optional[Iterable[GrowthArcParam]] | Omit = omit,
        height_meters: Optional[float] | Omit = omit,
        name: Optional[str] | Omit = omit,
        personality_traits: Optional[SequenceNotStr[str]] | Omit = omit,
        profile_image_url: Optional[str] | Omit = omit,
        role: Optional[CharacterRole] | Omit = omit,
        salary_gbp: Union[float, str, None] | Omit = omit,
        signature_quotes: Optional[SequenceNotStr[str]] | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Character:
        """
        Update specific fields of an existing character.

        Args:
          emotional_stats: Emotional intelligence statistics for a character.

          role: Roles characters can have.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not character_id:
            raise ValueError(f"Expected a non-empty value for `character_id` but received {character_id!r}")
        return self._patch(
            f"/characters/{character_id}",
            body=maybe_transform(
                {
                    "background": background,
                    "date_of_birth": date_of_birth,
                    "email": email,
                    "emotional_stats": emotional_stats,
                    "growth_arcs": growth_arcs,
                    "height_meters": height_meters,
                    "name": name,
                    "personality_traits": personality_traits,
                    "profile_image_url": profile_image_url,
                    "role": role,
                    "salary_gbp": salary_gbp,
                    "signature_quotes": signature_quotes,
                    "team_id": team_id,
                },
                character_update_params.CharacterUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Character,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        min_optimism: Optional[int] | Omit = omit,
        role: Optional[CharacterRole] | Omit = omit,
        skip: int | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimitPage[Character]:
        """
        Get a paginated list of Ted Lasso characters.

        Args:
          limit: Maximum number of items to return (max: 100)

          min_optimism: Minimum optimism score

          role: Filter by role

          skip: Number of items to skip (offset)

          team_id: Filter by team ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/characters",
            page=SyncSkipLimitPage[Character],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "min_optimism": min_optimism,
                        "role": role,
                        "skip": skip,
                        "team_id": team_id,
                    },
                    character_list_params.CharacterListParams,
                ),
            ),
            model=Character,
        )

    def delete(
        self,
        character_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a character from the database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not character_id:
            raise ValueError(f"Expected a non-empty value for `character_id` but received {character_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/characters/{character_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_quotes(
        self,
        character_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CharacterGetQuotesResponse:
        """
        Get all signature quotes from a specific character.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not character_id:
            raise ValueError(f"Expected a non-empty value for `character_id` but received {character_id!r}")
        return self._get(
            f"/characters/{character_id}/quotes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CharacterGetQuotesResponse,
        )


class AsyncCharactersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCharactersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCharactersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCharactersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return AsyncCharactersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        background: str,
        emotional_stats: EmotionalStatsParam,
        name: str,
        personality_traits: SequenceNotStr[str],
        role: CharacterRole,
        date_of_birth: Union[str, date, None] | Omit = omit,
        email: Optional[str] | Omit = omit,
        growth_arcs: Iterable[GrowthArcParam] | Omit = omit,
        height_meters: Optional[float] | Omit = omit,
        profile_image_url: Optional[str] | Omit = omit,
        salary_gbp: Union[float, str, None] | Omit = omit,
        signature_quotes: SequenceNotStr[str] | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Character:
        """
        Add a new character to the Ted Lasso universe.

        Args:
          background: Character background and history

          emotional_stats: Emotional intelligence stats

          name: Character's full name

          personality_traits: Key personality traits

          role: Character's role

          date_of_birth: Character's date of birth

          email: Character's email address

          growth_arcs: Character development across seasons

          height_meters: Height in meters

          profile_image_url: URL to character's profile image

          salary_gbp: Annual salary in GBP

          signature_quotes: Memorable quotes from this character

          team_id: ID of the team they belong to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/characters",
            body=await async_maybe_transform(
                {
                    "background": background,
                    "emotional_stats": emotional_stats,
                    "name": name,
                    "personality_traits": personality_traits,
                    "role": role,
                    "date_of_birth": date_of_birth,
                    "email": email,
                    "growth_arcs": growth_arcs,
                    "height_meters": height_meters,
                    "profile_image_url": profile_image_url,
                    "salary_gbp": salary_gbp,
                    "signature_quotes": signature_quotes,
                    "team_id": team_id,
                },
                character_create_params.CharacterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Character,
        )

    async def retrieve(
        self,
        character_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Character:
        """
        Retrieve detailed information about a specific character.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not character_id:
            raise ValueError(f"Expected a non-empty value for `character_id` but received {character_id!r}")
        return await self._get(
            f"/characters/{character_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Character,
        )

    async def update(
        self,
        character_id: str,
        *,
        background: Optional[str] | Omit = omit,
        date_of_birth: Union[str, date, None] | Omit = omit,
        email: Optional[str] | Omit = omit,
        emotional_stats: Optional[EmotionalStatsParam] | Omit = omit,
        growth_arcs: Optional[Iterable[GrowthArcParam]] | Omit = omit,
        height_meters: Optional[float] | Omit = omit,
        name: Optional[str] | Omit = omit,
        personality_traits: Optional[SequenceNotStr[str]] | Omit = omit,
        profile_image_url: Optional[str] | Omit = omit,
        role: Optional[CharacterRole] | Omit = omit,
        salary_gbp: Union[float, str, None] | Omit = omit,
        signature_quotes: Optional[SequenceNotStr[str]] | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Character:
        """
        Update specific fields of an existing character.

        Args:
          emotional_stats: Emotional intelligence statistics for a character.

          role: Roles characters can have.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not character_id:
            raise ValueError(f"Expected a non-empty value for `character_id` but received {character_id!r}")
        return await self._patch(
            f"/characters/{character_id}",
            body=await async_maybe_transform(
                {
                    "background": background,
                    "date_of_birth": date_of_birth,
                    "email": email,
                    "emotional_stats": emotional_stats,
                    "growth_arcs": growth_arcs,
                    "height_meters": height_meters,
                    "name": name,
                    "personality_traits": personality_traits,
                    "profile_image_url": profile_image_url,
                    "role": role,
                    "salary_gbp": salary_gbp,
                    "signature_quotes": signature_quotes,
                    "team_id": team_id,
                },
                character_update_params.CharacterUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Character,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        min_optimism: Optional[int] | Omit = omit,
        role: Optional[CharacterRole] | Omit = omit,
        skip: int | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Character, AsyncSkipLimitPage[Character]]:
        """
        Get a paginated list of Ted Lasso characters.

        Args:
          limit: Maximum number of items to return (max: 100)

          min_optimism: Minimum optimism score

          role: Filter by role

          skip: Number of items to skip (offset)

          team_id: Filter by team ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/characters",
            page=AsyncSkipLimitPage[Character],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "min_optimism": min_optimism,
                        "role": role,
                        "skip": skip,
                        "team_id": team_id,
                    },
                    character_list_params.CharacterListParams,
                ),
            ),
            model=Character,
        )

    async def delete(
        self,
        character_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a character from the database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not character_id:
            raise ValueError(f"Expected a non-empty value for `character_id` but received {character_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/characters/{character_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_quotes(
        self,
        character_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CharacterGetQuotesResponse:
        """
        Get all signature quotes from a specific character.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not character_id:
            raise ValueError(f"Expected a non-empty value for `character_id` but received {character_id!r}")
        return await self._get(
            f"/characters/{character_id}/quotes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CharacterGetQuotesResponse,
        )


class CharactersResourceWithRawResponse:
    def __init__(self, characters: CharactersResource) -> None:
        self._characters = characters

        self.create = to_raw_response_wrapper(
            characters.create,
        )
        self.retrieve = to_raw_response_wrapper(
            characters.retrieve,
        )
        self.update = to_raw_response_wrapper(
            characters.update,
        )
        self.list = to_raw_response_wrapper(
            characters.list,
        )
        self.delete = to_raw_response_wrapper(
            characters.delete,
        )
        self.get_quotes = to_raw_response_wrapper(
            characters.get_quotes,
        )


class AsyncCharactersResourceWithRawResponse:
    def __init__(self, characters: AsyncCharactersResource) -> None:
        self._characters = characters

        self.create = async_to_raw_response_wrapper(
            characters.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            characters.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            characters.update,
        )
        self.list = async_to_raw_response_wrapper(
            characters.list,
        )
        self.delete = async_to_raw_response_wrapper(
            characters.delete,
        )
        self.get_quotes = async_to_raw_response_wrapper(
            characters.get_quotes,
        )


class CharactersResourceWithStreamingResponse:
    def __init__(self, characters: CharactersResource) -> None:
        self._characters = characters

        self.create = to_streamed_response_wrapper(
            characters.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            characters.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            characters.update,
        )
        self.list = to_streamed_response_wrapper(
            characters.list,
        )
        self.delete = to_streamed_response_wrapper(
            characters.delete,
        )
        self.get_quotes = to_streamed_response_wrapper(
            characters.get_quotes,
        )


class AsyncCharactersResourceWithStreamingResponse:
    def __init__(self, characters: AsyncCharactersResource) -> None:
        self._characters = characters

        self.create = async_to_streamed_response_wrapper(
            characters.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            characters.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            characters.update,
        )
        self.list = async_to_streamed_response_wrapper(
            characters.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            characters.delete,
        )
        self.get_quotes = async_to_streamed_response_wrapper(
            characters.get_quotes,
        )
