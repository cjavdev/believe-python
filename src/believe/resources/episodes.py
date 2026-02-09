# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date

import httpx

from ..types import episode_list_params, episode_create_params, episode_update_params, episode_list_by_season_params
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
from ..types.episode import Episode
from ..types.episode_get_wisdom_response import EpisodeGetWisdomResponse

__all__ = ["EpisodesResource", "AsyncEpisodesResource"]


class EpisodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EpisodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/believe-python#accessing-raw-response-data-eg-headers
        """
        return EpisodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EpisodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/believe-python#with_streaming_response
        """
        return EpisodesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        air_date: Union[str, date],
        character_focus: SequenceNotStr[str],
        director: str,
        episode_number: int,
        main_theme: str,
        runtime_minutes: int,
        season: int,
        synopsis: str,
        ted_wisdom: str,
        title: str,
        writer: str,
        biscuits_with_boss_moment: Optional[str] | Omit = omit,
        memorable_moments: SequenceNotStr[str] | Omit = omit,
        us_viewers_millions: Optional[float] | Omit = omit,
        viewer_rating: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Episode:
        """
        Add a new episode to the series.

        Args:
          air_date: Original air date

          character_focus: Characters with significant development

          director: Episode director

          episode_number: Episode number within season

          main_theme: Central theme of the episode

          runtime_minutes: Episode runtime in minutes

          season: Season number

          synopsis: Brief plot synopsis

          ted_wisdom: Key piece of Ted wisdom from the episode

          title: Episode title

          writer: Episode writer(s)

          biscuits_with_boss_moment: Notable biscuits with the boss scene

          memorable_moments: Standout moments from the episode

          us_viewers_millions: US viewership in millions

          viewer_rating: Viewer rating out of 10

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/episodes",
            body=maybe_transform(
                {
                    "air_date": air_date,
                    "character_focus": character_focus,
                    "director": director,
                    "episode_number": episode_number,
                    "main_theme": main_theme,
                    "runtime_minutes": runtime_minutes,
                    "season": season,
                    "synopsis": synopsis,
                    "ted_wisdom": ted_wisdom,
                    "title": title,
                    "writer": writer,
                    "biscuits_with_boss_moment": biscuits_with_boss_moment,
                    "memorable_moments": memorable_moments,
                    "us_viewers_millions": us_viewers_millions,
                    "viewer_rating": viewer_rating,
                },
                episode_create_params.EpisodeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Episode,
        )

    def retrieve(
        self,
        episode_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Episode:
        """
        Retrieve detailed information about a specific episode.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not episode_id:
            raise ValueError(f"Expected a non-empty value for `episode_id` but received {episode_id!r}")
        return self._get(
            f"/episodes/{episode_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Episode,
        )

    def update(
        self,
        episode_id: str,
        *,
        air_date: Union[str, date, None] | Omit = omit,
        biscuits_with_boss_moment: Optional[str] | Omit = omit,
        character_focus: Optional[SequenceNotStr[str]] | Omit = omit,
        director: Optional[str] | Omit = omit,
        episode_number: Optional[int] | Omit = omit,
        main_theme: Optional[str] | Omit = omit,
        memorable_moments: Optional[SequenceNotStr[str]] | Omit = omit,
        runtime_minutes: Optional[int] | Omit = omit,
        season: Optional[int] | Omit = omit,
        synopsis: Optional[str] | Omit = omit,
        ted_wisdom: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        us_viewers_millions: Optional[float] | Omit = omit,
        viewer_rating: Optional[float] | Omit = omit,
        writer: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Episode:
        """
        Update specific fields of an existing episode.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not episode_id:
            raise ValueError(f"Expected a non-empty value for `episode_id` but received {episode_id!r}")
        return self._patch(
            f"/episodes/{episode_id}",
            body=maybe_transform(
                {
                    "air_date": air_date,
                    "biscuits_with_boss_moment": biscuits_with_boss_moment,
                    "character_focus": character_focus,
                    "director": director,
                    "episode_number": episode_number,
                    "main_theme": main_theme,
                    "memorable_moments": memorable_moments,
                    "runtime_minutes": runtime_minutes,
                    "season": season,
                    "synopsis": synopsis,
                    "ted_wisdom": ted_wisdom,
                    "title": title,
                    "us_viewers_millions": us_viewers_millions,
                    "viewer_rating": viewer_rating,
                    "writer": writer,
                },
                episode_update_params.EpisodeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Episode,
        )

    def list(
        self,
        *,
        character_focus: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        season: Optional[int] | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimitPage[Episode]:
        """
        Get a paginated list of all Ted Lasso episodes with optional filtering by
        season.

        Args:
          character_focus: Filter by character focus (character ID)

          limit: Maximum number of items to return (max: 100)

          season: Filter by season

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/episodes",
            page=SyncSkipLimitPage[Episode],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "character_focus": character_focus,
                        "limit": limit,
                        "season": season,
                        "skip": skip,
                    },
                    episode_list_params.EpisodeListParams,
                ),
            ),
            model=Episode,
        )

    def delete(
        self,
        episode_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove an episode from the database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not episode_id:
            raise ValueError(f"Expected a non-empty value for `episode_id` but received {episode_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/episodes/{episode_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_wisdom(
        self,
        episode_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EpisodeGetWisdomResponse:
        """
        Get Ted's wisdom and memorable moments from a specific episode.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not episode_id:
            raise ValueError(f"Expected a non-empty value for `episode_id` but received {episode_id!r}")
        return self._get(
            f"/episodes/{episode_id}/wisdom",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EpisodeGetWisdomResponse,
        )

    def list_by_season(
        self,
        season_number: int,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimitPage[Episode]:
        """
        Get a paginated list of episodes from a specific season.

        Args:
          limit: Maximum number of items to return (max: 100)

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/episodes/seasons/{season_number}",
            page=SyncSkipLimitPage[Episode],
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
                    episode_list_by_season_params.EpisodeListBySeasonParams,
                ),
            ),
            model=Episode,
        )


class AsyncEpisodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEpisodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEpisodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEpisodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/believe-python#with_streaming_response
        """
        return AsyncEpisodesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        air_date: Union[str, date],
        character_focus: SequenceNotStr[str],
        director: str,
        episode_number: int,
        main_theme: str,
        runtime_minutes: int,
        season: int,
        synopsis: str,
        ted_wisdom: str,
        title: str,
        writer: str,
        biscuits_with_boss_moment: Optional[str] | Omit = omit,
        memorable_moments: SequenceNotStr[str] | Omit = omit,
        us_viewers_millions: Optional[float] | Omit = omit,
        viewer_rating: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Episode:
        """
        Add a new episode to the series.

        Args:
          air_date: Original air date

          character_focus: Characters with significant development

          director: Episode director

          episode_number: Episode number within season

          main_theme: Central theme of the episode

          runtime_minutes: Episode runtime in minutes

          season: Season number

          synopsis: Brief plot synopsis

          ted_wisdom: Key piece of Ted wisdom from the episode

          title: Episode title

          writer: Episode writer(s)

          biscuits_with_boss_moment: Notable biscuits with the boss scene

          memorable_moments: Standout moments from the episode

          us_viewers_millions: US viewership in millions

          viewer_rating: Viewer rating out of 10

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/episodes",
            body=await async_maybe_transform(
                {
                    "air_date": air_date,
                    "character_focus": character_focus,
                    "director": director,
                    "episode_number": episode_number,
                    "main_theme": main_theme,
                    "runtime_minutes": runtime_minutes,
                    "season": season,
                    "synopsis": synopsis,
                    "ted_wisdom": ted_wisdom,
                    "title": title,
                    "writer": writer,
                    "biscuits_with_boss_moment": biscuits_with_boss_moment,
                    "memorable_moments": memorable_moments,
                    "us_viewers_millions": us_viewers_millions,
                    "viewer_rating": viewer_rating,
                },
                episode_create_params.EpisodeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Episode,
        )

    async def retrieve(
        self,
        episode_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Episode:
        """
        Retrieve detailed information about a specific episode.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not episode_id:
            raise ValueError(f"Expected a non-empty value for `episode_id` but received {episode_id!r}")
        return await self._get(
            f"/episodes/{episode_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Episode,
        )

    async def update(
        self,
        episode_id: str,
        *,
        air_date: Union[str, date, None] | Omit = omit,
        biscuits_with_boss_moment: Optional[str] | Omit = omit,
        character_focus: Optional[SequenceNotStr[str]] | Omit = omit,
        director: Optional[str] | Omit = omit,
        episode_number: Optional[int] | Omit = omit,
        main_theme: Optional[str] | Omit = omit,
        memorable_moments: Optional[SequenceNotStr[str]] | Omit = omit,
        runtime_minutes: Optional[int] | Omit = omit,
        season: Optional[int] | Omit = omit,
        synopsis: Optional[str] | Omit = omit,
        ted_wisdom: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        us_viewers_millions: Optional[float] | Omit = omit,
        viewer_rating: Optional[float] | Omit = omit,
        writer: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Episode:
        """
        Update specific fields of an existing episode.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not episode_id:
            raise ValueError(f"Expected a non-empty value for `episode_id` but received {episode_id!r}")
        return await self._patch(
            f"/episodes/{episode_id}",
            body=await async_maybe_transform(
                {
                    "air_date": air_date,
                    "biscuits_with_boss_moment": biscuits_with_boss_moment,
                    "character_focus": character_focus,
                    "director": director,
                    "episode_number": episode_number,
                    "main_theme": main_theme,
                    "memorable_moments": memorable_moments,
                    "runtime_minutes": runtime_minutes,
                    "season": season,
                    "synopsis": synopsis,
                    "ted_wisdom": ted_wisdom,
                    "title": title,
                    "us_viewers_millions": us_viewers_millions,
                    "viewer_rating": viewer_rating,
                    "writer": writer,
                },
                episode_update_params.EpisodeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Episode,
        )

    def list(
        self,
        *,
        character_focus: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        season: Optional[int] | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Episode, AsyncSkipLimitPage[Episode]]:
        """
        Get a paginated list of all Ted Lasso episodes with optional filtering by
        season.

        Args:
          character_focus: Filter by character focus (character ID)

          limit: Maximum number of items to return (max: 100)

          season: Filter by season

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/episodes",
            page=AsyncSkipLimitPage[Episode],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "character_focus": character_focus,
                        "limit": limit,
                        "season": season,
                        "skip": skip,
                    },
                    episode_list_params.EpisodeListParams,
                ),
            ),
            model=Episode,
        )

    async def delete(
        self,
        episode_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove an episode from the database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not episode_id:
            raise ValueError(f"Expected a non-empty value for `episode_id` but received {episode_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/episodes/{episode_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_wisdom(
        self,
        episode_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EpisodeGetWisdomResponse:
        """
        Get Ted's wisdom and memorable moments from a specific episode.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not episode_id:
            raise ValueError(f"Expected a non-empty value for `episode_id` but received {episode_id!r}")
        return await self._get(
            f"/episodes/{episode_id}/wisdom",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EpisodeGetWisdomResponse,
        )

    def list_by_season(
        self,
        season_number: int,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Episode, AsyncSkipLimitPage[Episode]]:
        """
        Get a paginated list of episodes from a specific season.

        Args:
          limit: Maximum number of items to return (max: 100)

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/episodes/seasons/{season_number}",
            page=AsyncSkipLimitPage[Episode],
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
                    episode_list_by_season_params.EpisodeListBySeasonParams,
                ),
            ),
            model=Episode,
        )


class EpisodesResourceWithRawResponse:
    def __init__(self, episodes: EpisodesResource) -> None:
        self._episodes = episodes

        self.create = to_raw_response_wrapper(
            episodes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            episodes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            episodes.update,
        )
        self.list = to_raw_response_wrapper(
            episodes.list,
        )
        self.delete = to_raw_response_wrapper(
            episodes.delete,
        )
        self.get_wisdom = to_raw_response_wrapper(
            episodes.get_wisdom,
        )
        self.list_by_season = to_raw_response_wrapper(
            episodes.list_by_season,
        )


class AsyncEpisodesResourceWithRawResponse:
    def __init__(self, episodes: AsyncEpisodesResource) -> None:
        self._episodes = episodes

        self.create = async_to_raw_response_wrapper(
            episodes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            episodes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            episodes.update,
        )
        self.list = async_to_raw_response_wrapper(
            episodes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            episodes.delete,
        )
        self.get_wisdom = async_to_raw_response_wrapper(
            episodes.get_wisdom,
        )
        self.list_by_season = async_to_raw_response_wrapper(
            episodes.list_by_season,
        )


class EpisodesResourceWithStreamingResponse:
    def __init__(self, episodes: EpisodesResource) -> None:
        self._episodes = episodes

        self.create = to_streamed_response_wrapper(
            episodes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            episodes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            episodes.update,
        )
        self.list = to_streamed_response_wrapper(
            episodes.list,
        )
        self.delete = to_streamed_response_wrapper(
            episodes.delete,
        )
        self.get_wisdom = to_streamed_response_wrapper(
            episodes.get_wisdom,
        )
        self.list_by_season = to_streamed_response_wrapper(
            episodes.list_by_season,
        )


class AsyncEpisodesResourceWithStreamingResponse:
    def __init__(self, episodes: AsyncEpisodesResource) -> None:
        self._episodes = episodes

        self.create = async_to_streamed_response_wrapper(
            episodes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            episodes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            episodes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            episodes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            episodes.delete,
        )
        self.get_wisdom = async_to_streamed_response_wrapper(
            episodes.get_wisdom,
        )
        self.list_by_season = async_to_streamed_response_wrapper(
            episodes.list_by_season,
        )
