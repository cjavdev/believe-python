# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional

import httpx

from .logo import (
    LogoResource,
    AsyncLogoResource,
    LogoResourceWithRawResponse,
    AsyncLogoResourceWithRawResponse,
    LogoResourceWithStreamingResponse,
    AsyncLogoResourceWithStreamingResponse,
)
from ...types import League, team_list_params, team_create_params, team_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSkipLimitPage, AsyncSkipLimitPage
from ...types.team import Team
from ..._base_client import AsyncPaginator, make_request_options
from ...types.league import League
from ...types.team_values_param import TeamValuesParam
from ...types.geo_location_param import GeoLocationParam
from ...types.team_get_rivals_response import TeamGetRivalsResponse
from ...types.team_list_logos_response import TeamListLogosResponse
from ...types.team_get_culture_response import TeamGetCultureResponse

__all__ = ["TeamsResource", "AsyncTeamsResource"]


class TeamsResource(SyncAPIResource):
    @cached_property
    def logo(self) -> LogoResource:
        return LogoResource(self._client)

    @cached_property
    def with_raw_response(self) -> TeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return TeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return TeamsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        culture_score: int,
        founded_year: int,
        league: League,
        name: str,
        stadium: str,
        values: TeamValuesParam,
        annual_budget_gbp: Union[float, str, None] | Omit = omit,
        average_attendance: Optional[float] | Omit = omit,
        contact_email: Optional[str] | Omit = omit,
        is_active: bool | Omit = omit,
        nickname: Optional[str] | Omit = omit,
        primary_color: Optional[str] | Omit = omit,
        rival_teams: SequenceNotStr[str] | Omit = omit,
        secondary_color: Optional[str] | Omit = omit,
        stadium_location: Optional[GeoLocationParam] | Omit = omit,
        website: Optional[str] | Omit = omit,
        win_percentage: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Team:
        """
        Add a new team to the league.

        Args:
          culture_score: Team culture/morale score (0-100)

          founded_year: Year the club was founded

          league: Current league

          name: Team name

          stadium: Home stadium name

          values: Team's core values

          annual_budget_gbp: Annual budget in GBP

          average_attendance: Average match attendance

          contact_email: Team contact email

          is_active: Whether the team is currently active

          nickname: Team nickname

          primary_color: Primary team color (hex)

          rival_teams: List of rival team IDs

          secondary_color: Secondary team color (hex)

          stadium_location: Geographic coordinates for a location.

          website: Official team website

          win_percentage: Season win percentage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/teams",
            body=maybe_transform(
                {
                    "culture_score": culture_score,
                    "founded_year": founded_year,
                    "league": league,
                    "name": name,
                    "stadium": stadium,
                    "values": values,
                    "annual_budget_gbp": annual_budget_gbp,
                    "average_attendance": average_attendance,
                    "contact_email": contact_email,
                    "is_active": is_active,
                    "nickname": nickname,
                    "primary_color": primary_color,
                    "rival_teams": rival_teams,
                    "secondary_color": secondary_color,
                    "stadium_location": stadium_location,
                    "website": website,
                    "win_percentage": win_percentage,
                },
                team_create_params.TeamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Team,
        )

    def retrieve(
        self,
        team_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Team:
        """
        Retrieve detailed information about a specific team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return self._get(
            f"/teams/{team_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Team,
        )

    def update(
        self,
        team_id: str,
        *,
        annual_budget_gbp: Union[float, str, None] | Omit = omit,
        average_attendance: Optional[float] | Omit = omit,
        contact_email: Optional[str] | Omit = omit,
        culture_score: Optional[int] | Omit = omit,
        founded_year: Optional[int] | Omit = omit,
        is_active: Optional[bool] | Omit = omit,
        league: Optional[League] | Omit = omit,
        name: Optional[str] | Omit = omit,
        nickname: Optional[str] | Omit = omit,
        primary_color: Optional[str] | Omit = omit,
        rival_teams: Optional[SequenceNotStr[str]] | Omit = omit,
        secondary_color: Optional[str] | Omit = omit,
        stadium: Optional[str] | Omit = omit,
        stadium_location: Optional[GeoLocationParam] | Omit = omit,
        values: Optional[TeamValuesParam] | Omit = omit,
        website: Optional[str] | Omit = omit,
        win_percentage: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Team:
        """
        Update specific fields of an existing team.

        Args:
          league: Football leagues.

          stadium_location: Geographic coordinates for a location.

          values: Core values that define a team's culture.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return self._patch(
            f"/teams/{team_id}",
            body=maybe_transform(
                {
                    "annual_budget_gbp": annual_budget_gbp,
                    "average_attendance": average_attendance,
                    "contact_email": contact_email,
                    "culture_score": culture_score,
                    "founded_year": founded_year,
                    "is_active": is_active,
                    "league": league,
                    "name": name,
                    "nickname": nickname,
                    "primary_color": primary_color,
                    "rival_teams": rival_teams,
                    "secondary_color": secondary_color,
                    "stadium": stadium,
                    "stadium_location": stadium_location,
                    "values": values,
                    "website": website,
                    "win_percentage": win_percentage,
                },
                team_update_params.TeamUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Team,
        )

    def list(
        self,
        *,
        league: Optional[League] | Omit = omit,
        limit: int | Omit = omit,
        min_culture_score: Optional[int] | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimitPage[Team]:
        """
        Get a paginated list of all teams with optional filtering by league or culture
        score.

        Args:
          league: Filter by league

          limit: Maximum number of items to return (max: 100)

          min_culture_score: Minimum culture score

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/teams",
            page=SyncSkipLimitPage[Team],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "league": league,
                        "limit": limit,
                        "min_culture_score": min_culture_score,
                        "skip": skip,
                    },
                    team_list_params.TeamListParams,
                ),
            ),
            model=Team,
        )

    def delete(
        self,
        team_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a team from the database (relegation to oblivion).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/teams/{team_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_culture(
        self,
        team_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TeamGetCultureResponse:
        """
        Get detailed culture and values information for a team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return self._get(
            f"/teams/{team_id}/culture",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamGetCultureResponse,
        )

    def get_rivals(
        self,
        team_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TeamGetRivalsResponse:
        """
        Get all rival teams for a specific team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return self._get(
            f"/teams/{team_id}/rivals",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamGetRivalsResponse,
        )

    def list_logos(
        self,
        team_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TeamListLogosResponse:
        """
        List all uploaded logos for a team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return self._get(
            f"/teams/{team_id}/logos",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamListLogosResponse,
        )


class AsyncTeamsResource(AsyncAPIResource):
    @cached_property
    def logo(self) -> AsyncLogoResource:
        return AsyncLogoResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return AsyncTeamsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        culture_score: int,
        founded_year: int,
        league: League,
        name: str,
        stadium: str,
        values: TeamValuesParam,
        annual_budget_gbp: Union[float, str, None] | Omit = omit,
        average_attendance: Optional[float] | Omit = omit,
        contact_email: Optional[str] | Omit = omit,
        is_active: bool | Omit = omit,
        nickname: Optional[str] | Omit = omit,
        primary_color: Optional[str] | Omit = omit,
        rival_teams: SequenceNotStr[str] | Omit = omit,
        secondary_color: Optional[str] | Omit = omit,
        stadium_location: Optional[GeoLocationParam] | Omit = omit,
        website: Optional[str] | Omit = omit,
        win_percentage: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Team:
        """
        Add a new team to the league.

        Args:
          culture_score: Team culture/morale score (0-100)

          founded_year: Year the club was founded

          league: Current league

          name: Team name

          stadium: Home stadium name

          values: Team's core values

          annual_budget_gbp: Annual budget in GBP

          average_attendance: Average match attendance

          contact_email: Team contact email

          is_active: Whether the team is currently active

          nickname: Team nickname

          primary_color: Primary team color (hex)

          rival_teams: List of rival team IDs

          secondary_color: Secondary team color (hex)

          stadium_location: Geographic coordinates for a location.

          website: Official team website

          win_percentage: Season win percentage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/teams",
            body=await async_maybe_transform(
                {
                    "culture_score": culture_score,
                    "founded_year": founded_year,
                    "league": league,
                    "name": name,
                    "stadium": stadium,
                    "values": values,
                    "annual_budget_gbp": annual_budget_gbp,
                    "average_attendance": average_attendance,
                    "contact_email": contact_email,
                    "is_active": is_active,
                    "nickname": nickname,
                    "primary_color": primary_color,
                    "rival_teams": rival_teams,
                    "secondary_color": secondary_color,
                    "stadium_location": stadium_location,
                    "website": website,
                    "win_percentage": win_percentage,
                },
                team_create_params.TeamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Team,
        )

    async def retrieve(
        self,
        team_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Team:
        """
        Retrieve detailed information about a specific team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return await self._get(
            f"/teams/{team_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Team,
        )

    async def update(
        self,
        team_id: str,
        *,
        annual_budget_gbp: Union[float, str, None] | Omit = omit,
        average_attendance: Optional[float] | Omit = omit,
        contact_email: Optional[str] | Omit = omit,
        culture_score: Optional[int] | Omit = omit,
        founded_year: Optional[int] | Omit = omit,
        is_active: Optional[bool] | Omit = omit,
        league: Optional[League] | Omit = omit,
        name: Optional[str] | Omit = omit,
        nickname: Optional[str] | Omit = omit,
        primary_color: Optional[str] | Omit = omit,
        rival_teams: Optional[SequenceNotStr[str]] | Omit = omit,
        secondary_color: Optional[str] | Omit = omit,
        stadium: Optional[str] | Omit = omit,
        stadium_location: Optional[GeoLocationParam] | Omit = omit,
        values: Optional[TeamValuesParam] | Omit = omit,
        website: Optional[str] | Omit = omit,
        win_percentage: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Team:
        """
        Update specific fields of an existing team.

        Args:
          league: Football leagues.

          stadium_location: Geographic coordinates for a location.

          values: Core values that define a team's culture.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return await self._patch(
            f"/teams/{team_id}",
            body=await async_maybe_transform(
                {
                    "annual_budget_gbp": annual_budget_gbp,
                    "average_attendance": average_attendance,
                    "contact_email": contact_email,
                    "culture_score": culture_score,
                    "founded_year": founded_year,
                    "is_active": is_active,
                    "league": league,
                    "name": name,
                    "nickname": nickname,
                    "primary_color": primary_color,
                    "rival_teams": rival_teams,
                    "secondary_color": secondary_color,
                    "stadium": stadium,
                    "stadium_location": stadium_location,
                    "values": values,
                    "website": website,
                    "win_percentage": win_percentage,
                },
                team_update_params.TeamUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Team,
        )

    def list(
        self,
        *,
        league: Optional[League] | Omit = omit,
        limit: int | Omit = omit,
        min_culture_score: Optional[int] | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Team, AsyncSkipLimitPage[Team]]:
        """
        Get a paginated list of all teams with optional filtering by league or culture
        score.

        Args:
          league: Filter by league

          limit: Maximum number of items to return (max: 100)

          min_culture_score: Minimum culture score

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/teams",
            page=AsyncSkipLimitPage[Team],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "league": league,
                        "limit": limit,
                        "min_culture_score": min_culture_score,
                        "skip": skip,
                    },
                    team_list_params.TeamListParams,
                ),
            ),
            model=Team,
        )

    async def delete(
        self,
        team_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a team from the database (relegation to oblivion).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/teams/{team_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_culture(
        self,
        team_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TeamGetCultureResponse:
        """
        Get detailed culture and values information for a team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return await self._get(
            f"/teams/{team_id}/culture",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamGetCultureResponse,
        )

    async def get_rivals(
        self,
        team_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TeamGetRivalsResponse:
        """
        Get all rival teams for a specific team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return await self._get(
            f"/teams/{team_id}/rivals",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamGetRivalsResponse,
        )

    async def list_logos(
        self,
        team_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TeamListLogosResponse:
        """
        List all uploaded logos for a team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return await self._get(
            f"/teams/{team_id}/logos",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamListLogosResponse,
        )


class TeamsResourceWithRawResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.create = to_raw_response_wrapper(
            teams.create,
        )
        self.retrieve = to_raw_response_wrapper(
            teams.retrieve,
        )
        self.update = to_raw_response_wrapper(
            teams.update,
        )
        self.list = to_raw_response_wrapper(
            teams.list,
        )
        self.delete = to_raw_response_wrapper(
            teams.delete,
        )
        self.get_culture = to_raw_response_wrapper(
            teams.get_culture,
        )
        self.get_rivals = to_raw_response_wrapper(
            teams.get_rivals,
        )
        self.list_logos = to_raw_response_wrapper(
            teams.list_logos,
        )

    @cached_property
    def logo(self) -> LogoResourceWithRawResponse:
        return LogoResourceWithRawResponse(self._teams.logo)


class AsyncTeamsResourceWithRawResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.create = async_to_raw_response_wrapper(
            teams.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            teams.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            teams.update,
        )
        self.list = async_to_raw_response_wrapper(
            teams.list,
        )
        self.delete = async_to_raw_response_wrapper(
            teams.delete,
        )
        self.get_culture = async_to_raw_response_wrapper(
            teams.get_culture,
        )
        self.get_rivals = async_to_raw_response_wrapper(
            teams.get_rivals,
        )
        self.list_logos = async_to_raw_response_wrapper(
            teams.list_logos,
        )

    @cached_property
    def logo(self) -> AsyncLogoResourceWithRawResponse:
        return AsyncLogoResourceWithRawResponse(self._teams.logo)


class TeamsResourceWithStreamingResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.create = to_streamed_response_wrapper(
            teams.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            teams.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            teams.update,
        )
        self.list = to_streamed_response_wrapper(
            teams.list,
        )
        self.delete = to_streamed_response_wrapper(
            teams.delete,
        )
        self.get_culture = to_streamed_response_wrapper(
            teams.get_culture,
        )
        self.get_rivals = to_streamed_response_wrapper(
            teams.get_rivals,
        )
        self.list_logos = to_streamed_response_wrapper(
            teams.list_logos,
        )

    @cached_property
    def logo(self) -> LogoResourceWithStreamingResponse:
        return LogoResourceWithStreamingResponse(self._teams.logo)


class AsyncTeamsResourceWithStreamingResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.create = async_to_streamed_response_wrapper(
            teams.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            teams.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            teams.update,
        )
        self.list = async_to_streamed_response_wrapper(
            teams.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            teams.delete,
        )
        self.get_culture = async_to_streamed_response_wrapper(
            teams.get_culture,
        )
        self.get_rivals = async_to_streamed_response_wrapper(
            teams.get_rivals,
        )
        self.list_logos = async_to_streamed_response_wrapper(
            teams.list_logos,
        )

    @cached_property
    def logo(self) -> AsyncLogoResourceWithStreamingResponse:
        return AsyncLogoResourceWithStreamingResponse(self._teams.logo)
