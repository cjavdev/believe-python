# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime

import httpx

from ...types import (
    MatchType,
    MatchResult,
    match_list_params,
    match_create_params,
    match_update_params,
    match_stream_live_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .commentary import (
    CommentaryResource,
    AsyncCommentaryResource,
    CommentaryResourceWithRawResponse,
    AsyncCommentaryResourceWithRawResponse,
    CommentaryResourceWithStreamingResponse,
    AsyncCommentaryResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSkipLimitPage, AsyncSkipLimitPage
from ...types.match import Match
from ..._base_client import AsyncPaginator, make_request_options
from ...types.match_type import MatchType
from ...types.match_result import MatchResult
from ...types.turning_point_param import TurningPointParam
from ...types.match_get_lesson_response import MatchGetLessonResponse
from ...types.match_get_turning_points_response import MatchGetTurningPointsResponse

__all__ = ["MatchesResource", "AsyncMatchesResource"]


class MatchesResource(SyncAPIResource):
    @cached_property
    def commentary(self) -> CommentaryResource:
        return CommentaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> MatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return MatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return MatchesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        away_team_id: str,
        date: Union[str, datetime],
        home_team_id: str,
        match_type: MatchType,
        attendance: Optional[int] | Omit = omit,
        away_score: int | Omit = omit,
        episode_id: Optional[str] | Omit = omit,
        home_score: int | Omit = omit,
        lesson_learned: Optional[str] | Omit = omit,
        possession_percentage: Optional[float] | Omit = omit,
        result: MatchResult | Omit = omit,
        ted_halftime_speech: Optional[str] | Omit = omit,
        ticket_revenue_gbp: Union[float, str, None] | Omit = omit,
        turning_points: Iterable[TurningPointParam] | Omit = omit,
        weather_temp_celsius: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Match:
        """
        Schedule a new match.

        Args:
          away_team_id: Away team ID

          date: Match date and time

          home_team_id: Home team ID

          match_type: Type of match

          attendance: Match attendance

          away_score: Away team score

          episode_id: Episode ID where this match is featured

          home_score: Home team score

          lesson_learned: The life lesson learned from this match

          possession_percentage: Home team possession percentage

          result: Match result from home team perspective

          ted_halftime_speech: Ted's inspirational halftime speech

          ticket_revenue_gbp: Total ticket revenue in GBP

          turning_points: Key moments that changed the match

          weather_temp_celsius: Temperature at kickoff in Celsius

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/matches",
            body=maybe_transform(
                {
                    "away_team_id": away_team_id,
                    "date": date,
                    "home_team_id": home_team_id,
                    "match_type": match_type,
                    "attendance": attendance,
                    "away_score": away_score,
                    "episode_id": episode_id,
                    "home_score": home_score,
                    "lesson_learned": lesson_learned,
                    "possession_percentage": possession_percentage,
                    "result": result,
                    "ted_halftime_speech": ted_halftime_speech,
                    "ticket_revenue_gbp": ticket_revenue_gbp,
                    "turning_points": turning_points,
                    "weather_temp_celsius": weather_temp_celsius,
                },
                match_create_params.MatchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Match,
        )

    def retrieve(
        self,
        match_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Match:
        """
        Retrieve detailed information about a specific match.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not match_id:
            raise ValueError(f"Expected a non-empty value for `match_id` but received {match_id!r}")
        return self._get(
            f"/matches/{match_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Match,
        )

    def update(
        self,
        match_id: str,
        *,
        attendance: Optional[int] | Omit = omit,
        away_score: Optional[int] | Omit = omit,
        away_team_id: Optional[str] | Omit = omit,
        date: Union[str, datetime, None] | Omit = omit,
        episode_id: Optional[str] | Omit = omit,
        home_score: Optional[int] | Omit = omit,
        home_team_id: Optional[str] | Omit = omit,
        lesson_learned: Optional[str] | Omit = omit,
        match_type: Optional[MatchType] | Omit = omit,
        possession_percentage: Optional[float] | Omit = omit,
        result: Optional[MatchResult] | Omit = omit,
        ted_halftime_speech: Optional[str] | Omit = omit,
        ticket_revenue_gbp: Union[float, str, None] | Omit = omit,
        turning_points: Optional[Iterable[TurningPointParam]] | Omit = omit,
        weather_temp_celsius: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Match:
        """
        Update specific fields of an existing match (e.g., update score).

        Args:
          match_type: Types of matches.

          result: Match result types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not match_id:
            raise ValueError(f"Expected a non-empty value for `match_id` but received {match_id!r}")
        return self._patch(
            f"/matches/{match_id}",
            body=maybe_transform(
                {
                    "attendance": attendance,
                    "away_score": away_score,
                    "away_team_id": away_team_id,
                    "date": date,
                    "episode_id": episode_id,
                    "home_score": home_score,
                    "home_team_id": home_team_id,
                    "lesson_learned": lesson_learned,
                    "match_type": match_type,
                    "possession_percentage": possession_percentage,
                    "result": result,
                    "ted_halftime_speech": ted_halftime_speech,
                    "ticket_revenue_gbp": ticket_revenue_gbp,
                    "turning_points": turning_points,
                    "weather_temp_celsius": weather_temp_celsius,
                },
                match_update_params.MatchUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Match,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        match_type: Optional[MatchType] | Omit = omit,
        result: Optional[MatchResult] | Omit = omit,
        skip: int | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimitPage[Match]:
        """
        Get a paginated list of all matches with optional filtering.

        Args:
          limit: Maximum number of items to return (max: 100)

          match_type: Filter by match type

          result: Filter by result

          skip: Number of items to skip (offset)

          team_id: Filter by team (home or away)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/matches",
            page=SyncSkipLimitPage[Match],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "match_type": match_type,
                        "result": result,
                        "skip": skip,
                        "team_id": team_id,
                    },
                    match_list_params.MatchListParams,
                ),
            ),
            model=Match,
        )

    def delete(
        self,
        match_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a match from the database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not match_id:
            raise ValueError(f"Expected a non-empty value for `match_id` but received {match_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/matches/{match_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_lesson(
        self,
        match_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MatchGetLessonResponse:
        """
        Get the life lesson learned from a specific match.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not match_id:
            raise ValueError(f"Expected a non-empty value for `match_id` but received {match_id!r}")
        return self._get(
            f"/matches/{match_id}/lesson",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MatchGetLessonResponse,
        )

    def get_turning_points(
        self,
        match_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MatchGetTurningPointsResponse:
        """
        Get all turning points from a specific match.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not match_id:
            raise ValueError(f"Expected a non-empty value for `match_id` but received {match_id!r}")
        return self._get(
            f"/matches/{match_id}/turning-points",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MatchGetTurningPointsResponse,
        )

    def stream_live(
        self,
        *,
        away_team: str | Omit = omit,
        excitement_level: int | Omit = omit,
        home_team: str | Omit = omit,
        speed: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        WebSocket endpoint for real-time live match simulation.

        Connect to receive a stream of match events as they happen in a simulated
        football match.

        ## Connection

        Connect via WebSocket with optional query parameters to customize the
        simulation.

        ## Example WebSocket URL

        ```
        ws://localhost:8000/matches/live?home_team=AFC%20Richmond&away_team=Manchester%20City&speed=2.0&excitement_level=7
        ```

        ## Server Messages

        The server sends JSON messages with these types:

        - `match_start` - When the match begins
        - `match_event` - For each match event (goals, fouls, cards, etc.)
        - `match_end` - When the match concludes
        - `error` - If an error occurs
        - `pong` - Response to client ping

        ## Client Messages

        Send JSON to control the simulation:

        - `{"action": "ping"}` - Keep-alive, server responds with `{"type": "pong"}`
        - `{"action": "pause"}` - Pause the simulation
        - `{"action": "resume"}` - Resume a paused simulation
        - `{"action": "set_speed", "speed": 2.0}` - Change playback speed (0.1-10.0)
        - `{"action": "get_status"}` - Request current match status

        Args:
          away_team: Away team name

          excitement_level: How eventful the match should be (1=boring, 10=chaos)

          home_team: Home team name

          speed: Simulation speed multiplier (1.0 = real-time)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/matches/live",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "away_team": away_team,
                        "excitement_level": excitement_level,
                        "home_team": home_team,
                        "speed": speed,
                    },
                    match_stream_live_params.MatchStreamLiveParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncMatchesResource(AsyncAPIResource):
    @cached_property
    def commentary(self) -> AsyncCommentaryResource:
        return AsyncCommentaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return AsyncMatchesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        away_team_id: str,
        date: Union[str, datetime],
        home_team_id: str,
        match_type: MatchType,
        attendance: Optional[int] | Omit = omit,
        away_score: int | Omit = omit,
        episode_id: Optional[str] | Omit = omit,
        home_score: int | Omit = omit,
        lesson_learned: Optional[str] | Omit = omit,
        possession_percentage: Optional[float] | Omit = omit,
        result: MatchResult | Omit = omit,
        ted_halftime_speech: Optional[str] | Omit = omit,
        ticket_revenue_gbp: Union[float, str, None] | Omit = omit,
        turning_points: Iterable[TurningPointParam] | Omit = omit,
        weather_temp_celsius: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Match:
        """
        Schedule a new match.

        Args:
          away_team_id: Away team ID

          date: Match date and time

          home_team_id: Home team ID

          match_type: Type of match

          attendance: Match attendance

          away_score: Away team score

          episode_id: Episode ID where this match is featured

          home_score: Home team score

          lesson_learned: The life lesson learned from this match

          possession_percentage: Home team possession percentage

          result: Match result from home team perspective

          ted_halftime_speech: Ted's inspirational halftime speech

          ticket_revenue_gbp: Total ticket revenue in GBP

          turning_points: Key moments that changed the match

          weather_temp_celsius: Temperature at kickoff in Celsius

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/matches",
            body=await async_maybe_transform(
                {
                    "away_team_id": away_team_id,
                    "date": date,
                    "home_team_id": home_team_id,
                    "match_type": match_type,
                    "attendance": attendance,
                    "away_score": away_score,
                    "episode_id": episode_id,
                    "home_score": home_score,
                    "lesson_learned": lesson_learned,
                    "possession_percentage": possession_percentage,
                    "result": result,
                    "ted_halftime_speech": ted_halftime_speech,
                    "ticket_revenue_gbp": ticket_revenue_gbp,
                    "turning_points": turning_points,
                    "weather_temp_celsius": weather_temp_celsius,
                },
                match_create_params.MatchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Match,
        )

    async def retrieve(
        self,
        match_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Match:
        """
        Retrieve detailed information about a specific match.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not match_id:
            raise ValueError(f"Expected a non-empty value for `match_id` but received {match_id!r}")
        return await self._get(
            f"/matches/{match_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Match,
        )

    async def update(
        self,
        match_id: str,
        *,
        attendance: Optional[int] | Omit = omit,
        away_score: Optional[int] | Omit = omit,
        away_team_id: Optional[str] | Omit = omit,
        date: Union[str, datetime, None] | Omit = omit,
        episode_id: Optional[str] | Omit = omit,
        home_score: Optional[int] | Omit = omit,
        home_team_id: Optional[str] | Omit = omit,
        lesson_learned: Optional[str] | Omit = omit,
        match_type: Optional[MatchType] | Omit = omit,
        possession_percentage: Optional[float] | Omit = omit,
        result: Optional[MatchResult] | Omit = omit,
        ted_halftime_speech: Optional[str] | Omit = omit,
        ticket_revenue_gbp: Union[float, str, None] | Omit = omit,
        turning_points: Optional[Iterable[TurningPointParam]] | Omit = omit,
        weather_temp_celsius: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Match:
        """
        Update specific fields of an existing match (e.g., update score).

        Args:
          match_type: Types of matches.

          result: Match result types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not match_id:
            raise ValueError(f"Expected a non-empty value for `match_id` but received {match_id!r}")
        return await self._patch(
            f"/matches/{match_id}",
            body=await async_maybe_transform(
                {
                    "attendance": attendance,
                    "away_score": away_score,
                    "away_team_id": away_team_id,
                    "date": date,
                    "episode_id": episode_id,
                    "home_score": home_score,
                    "home_team_id": home_team_id,
                    "lesson_learned": lesson_learned,
                    "match_type": match_type,
                    "possession_percentage": possession_percentage,
                    "result": result,
                    "ted_halftime_speech": ted_halftime_speech,
                    "ticket_revenue_gbp": ticket_revenue_gbp,
                    "turning_points": turning_points,
                    "weather_temp_celsius": weather_temp_celsius,
                },
                match_update_params.MatchUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Match,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        match_type: Optional[MatchType] | Omit = omit,
        result: Optional[MatchResult] | Omit = omit,
        skip: int | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Match, AsyncSkipLimitPage[Match]]:
        """
        Get a paginated list of all matches with optional filtering.

        Args:
          limit: Maximum number of items to return (max: 100)

          match_type: Filter by match type

          result: Filter by result

          skip: Number of items to skip (offset)

          team_id: Filter by team (home or away)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/matches",
            page=AsyncSkipLimitPage[Match],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "match_type": match_type,
                        "result": result,
                        "skip": skip,
                        "team_id": team_id,
                    },
                    match_list_params.MatchListParams,
                ),
            ),
            model=Match,
        )

    async def delete(
        self,
        match_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a match from the database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not match_id:
            raise ValueError(f"Expected a non-empty value for `match_id` but received {match_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/matches/{match_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_lesson(
        self,
        match_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MatchGetLessonResponse:
        """
        Get the life lesson learned from a specific match.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not match_id:
            raise ValueError(f"Expected a non-empty value for `match_id` but received {match_id!r}")
        return await self._get(
            f"/matches/{match_id}/lesson",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MatchGetLessonResponse,
        )

    async def get_turning_points(
        self,
        match_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MatchGetTurningPointsResponse:
        """
        Get all turning points from a specific match.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not match_id:
            raise ValueError(f"Expected a non-empty value for `match_id` but received {match_id!r}")
        return await self._get(
            f"/matches/{match_id}/turning-points",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MatchGetTurningPointsResponse,
        )

    async def stream_live(
        self,
        *,
        away_team: str | Omit = omit,
        excitement_level: int | Omit = omit,
        home_team: str | Omit = omit,
        speed: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        WebSocket endpoint for real-time live match simulation.

        Connect to receive a stream of match events as they happen in a simulated
        football match.

        ## Connection

        Connect via WebSocket with optional query parameters to customize the
        simulation.

        ## Example WebSocket URL

        ```
        ws://localhost:8000/matches/live?home_team=AFC%20Richmond&away_team=Manchester%20City&speed=2.0&excitement_level=7
        ```

        ## Server Messages

        The server sends JSON messages with these types:

        - `match_start` - When the match begins
        - `match_event` - For each match event (goals, fouls, cards, etc.)
        - `match_end` - When the match concludes
        - `error` - If an error occurs
        - `pong` - Response to client ping

        ## Client Messages

        Send JSON to control the simulation:

        - `{"action": "ping"}` - Keep-alive, server responds with `{"type": "pong"}`
        - `{"action": "pause"}` - Pause the simulation
        - `{"action": "resume"}` - Resume a paused simulation
        - `{"action": "set_speed", "speed": 2.0}` - Change playback speed (0.1-10.0)
        - `{"action": "get_status"}` - Request current match status

        Args:
          away_team: Away team name

          excitement_level: How eventful the match should be (1=boring, 10=chaos)

          home_team: Home team name

          speed: Simulation speed multiplier (1.0 = real-time)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/matches/live",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "away_team": away_team,
                        "excitement_level": excitement_level,
                        "home_team": home_team,
                        "speed": speed,
                    },
                    match_stream_live_params.MatchStreamLiveParams,
                ),
            ),
            cast_to=NoneType,
        )


class MatchesResourceWithRawResponse:
    def __init__(self, matches: MatchesResource) -> None:
        self._matches = matches

        self.create = to_raw_response_wrapper(
            matches.create,
        )
        self.retrieve = to_raw_response_wrapper(
            matches.retrieve,
        )
        self.update = to_raw_response_wrapper(
            matches.update,
        )
        self.list = to_raw_response_wrapper(
            matches.list,
        )
        self.delete = to_raw_response_wrapper(
            matches.delete,
        )
        self.get_lesson = to_raw_response_wrapper(
            matches.get_lesson,
        )
        self.get_turning_points = to_raw_response_wrapper(
            matches.get_turning_points,
        )
        self.stream_live = to_raw_response_wrapper(
            matches.stream_live,
        )

    @cached_property
    def commentary(self) -> CommentaryResourceWithRawResponse:
        return CommentaryResourceWithRawResponse(self._matches.commentary)


class AsyncMatchesResourceWithRawResponse:
    def __init__(self, matches: AsyncMatchesResource) -> None:
        self._matches = matches

        self.create = async_to_raw_response_wrapper(
            matches.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            matches.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            matches.update,
        )
        self.list = async_to_raw_response_wrapper(
            matches.list,
        )
        self.delete = async_to_raw_response_wrapper(
            matches.delete,
        )
        self.get_lesson = async_to_raw_response_wrapper(
            matches.get_lesson,
        )
        self.get_turning_points = async_to_raw_response_wrapper(
            matches.get_turning_points,
        )
        self.stream_live = async_to_raw_response_wrapper(
            matches.stream_live,
        )

    @cached_property
    def commentary(self) -> AsyncCommentaryResourceWithRawResponse:
        return AsyncCommentaryResourceWithRawResponse(self._matches.commentary)


class MatchesResourceWithStreamingResponse:
    def __init__(self, matches: MatchesResource) -> None:
        self._matches = matches

        self.create = to_streamed_response_wrapper(
            matches.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            matches.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            matches.update,
        )
        self.list = to_streamed_response_wrapper(
            matches.list,
        )
        self.delete = to_streamed_response_wrapper(
            matches.delete,
        )
        self.get_lesson = to_streamed_response_wrapper(
            matches.get_lesson,
        )
        self.get_turning_points = to_streamed_response_wrapper(
            matches.get_turning_points,
        )
        self.stream_live = to_streamed_response_wrapper(
            matches.stream_live,
        )

    @cached_property
    def commentary(self) -> CommentaryResourceWithStreamingResponse:
        return CommentaryResourceWithStreamingResponse(self._matches.commentary)


class AsyncMatchesResourceWithStreamingResponse:
    def __init__(self, matches: AsyncMatchesResource) -> None:
        self._matches = matches

        self.create = async_to_streamed_response_wrapper(
            matches.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            matches.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            matches.update,
        )
        self.list = async_to_streamed_response_wrapper(
            matches.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            matches.delete,
        )
        self.get_lesson = async_to_streamed_response_wrapper(
            matches.get_lesson,
        )
        self.get_turning_points = async_to_streamed_response_wrapper(
            matches.get_turning_points,
        )
        self.stream_live = async_to_streamed_response_wrapper(
            matches.stream_live,
        )

    @cached_property
    def commentary(self) -> AsyncCommentaryResourceWithStreamingResponse:
        return AsyncCommentaryResourceWithStreamingResponse(self._matches.commentary)
