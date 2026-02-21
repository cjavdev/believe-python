# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import (
    Position,
    CoachSpecialty,
    team_member_list_params,
    team_member_create_params,
    team_member_update_params,
    team_member_list_staff_params,
    team_member_list_coaches_params,
    team_member_list_players_params,
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
from ..types.coach import Coach
from .._base_client import AsyncPaginator, make_request_options
from ..types.player import Player
from ..types.position import Position
from ..types.coach_specialty import CoachSpecialty
from ..types.team_member_list_response import TeamMemberListResponse
from ..types.team_member_create_response import TeamMemberCreateResponse
from ..types.team_member_update_response import TeamMemberUpdateResponse
from ..types.team_member_retrieve_response import TeamMemberRetrieveResponse
from ..types.team_member_list_staff_response import TeamMemberListStaffResponse

__all__ = ["TeamMembersResource", "AsyncTeamMembersResource"]


class TeamMembersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TeamMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return TeamMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return TeamMembersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        member: team_member_create_params.Member,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TeamMemberCreateResponse:
        """
        Add a new team member to a team.

        The request body is a **union type (oneOf)** - you must include the
        `member_type` discriminator field:

        - `"member_type": "player"` - Creates a player (requires position,
          jersey_number, etc.)
        - `"member_type": "coach"` - Creates a coach (requires specialty, etc.)
        - `"member_type": "medical_staff"` - Creates medical staff (requires medical
          specialty, etc.)
        - `"member_type": "equipment_manager"` - Creates equipment manager (requires
          responsibilities, etc.)

        The `character_id` field references an existing character from
        `/characters/{id}`.

        **Example for creating a player:**

        ```json
        {
          "member_type": "player",
          "character_id": "sam-obisanya",
          "team_id": "afc-richmond",
          "years_with_team": 2,
          "position": "midfielder",
          "jersey_number": 24,
          "goals_scored": 12,
          "assists": 15
        }
        ```

        Args:
          member: A football player on the team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            TeamMemberCreateResponse,
            self._post(
                "/team-members",
                body=maybe_transform(member, team_member_create_params.TeamMemberCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, TeamMemberCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TeamMemberRetrieveResponse:
        """
        Retrieve detailed information about a specific team member.

        The response is a **union type (oneOf)** - the actual shape depends on the
        member's type:

        - **player**: Includes position, jersey_number, goals_scored, assists,
          is_captain
        - **coach**: Includes specialty, certifications, win_rate
        - **medical_staff**: Includes specialty, qualifications, license_number
        - **equipment_manager**: Includes responsibilities, is_head_kitman

        Use `character_id` to fetch full character details from
        `/characters/{character_id}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return cast(
            TeamMemberRetrieveResponse,
            self._get(
                f"/team-members/{member_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, TeamMemberRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        member_id: str,
        *,
        updates: team_member_update_params.Updates,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TeamMemberUpdateResponse:
        """Update specific fields of an existing team member.

        Fields vary by member type.

        Args:
          updates: Update model for players.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return cast(
            TeamMemberUpdateResponse,
            self._patch(
                f"/team-members/{member_id}",
                body=maybe_transform(updates, team_member_update_params.TeamMemberUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, TeamMemberUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        member_type: Optional[Literal["player", "coach", "medical_staff", "equipment_manager"]] | Omit = omit,
        skip: int | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimitPage[TeamMemberListResponse]:
        """
        Get a paginated list of all team members.

        This endpoint demonstrates **union types (oneOf)** in the response. Each team
        member can be one of: Player, Coach, MedicalStaff, or EquipmentManager. The
        `member_type` field acts as a discriminator to determine the shape of each
        object.

        Args:
          limit: Maximum number of items to return (max: 100)

          member_type: Filter by member type

          skip: Number of items to skip (offset)

          team_id: Filter by team ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/team-members",
            page=SyncSkipLimitPage[TeamMemberListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "member_type": member_type,
                        "skip": skip,
                        "team_id": team_id,
                    },
                    team_member_list_params.TeamMemberListParams,
                ),
            ),
            model=cast(Any, TeamMemberListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def delete(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a team member from the roster.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/team-members/{member_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_coaches(
        self,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        specialty: Optional[CoachSpecialty] | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimitPage[Coach]:
        """
        Get only coaches (filtered subset of team members).

        Args:
          limit: Maximum number of items to return (max: 100)

          skip: Number of items to skip (offset)

          specialty: Filter by specialty

          team_id: Filter by team ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/team-members/coaches/",
            page=SyncSkipLimitPage[Coach],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                        "specialty": specialty,
                        "team_id": team_id,
                    },
                    team_member_list_coaches_params.TeamMemberListCoachesParams,
                ),
            ),
            model=Coach,
        )

    def list_players(
        self,
        *,
        limit: int | Omit = omit,
        position: Optional[Position] | Omit = omit,
        skip: int | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimitPage[Player]:
        """
        Get only players (filtered subset of team members).

        Args:
          limit: Maximum number of items to return (max: 100)

          position: Filter by position

          skip: Number of items to skip (offset)

          team_id: Filter by team ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/team-members/players/",
            page=SyncSkipLimitPage[Player],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "position": position,
                        "skip": skip,
                        "team_id": team_id,
                    },
                    team_member_list_players_params.TeamMemberListPlayersParams,
                ),
            ),
            model=Player,
        )

    def list_staff(
        self,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimitPage[TeamMemberListStaffResponse]:
        """
        Get all staff members (medical staff and equipment managers).

        This demonstrates a **narrower union type** - the response is oneOf MedicalStaff
        or EquipmentManager.

        Args:
          limit: Maximum number of items to return (max: 100)

          skip: Number of items to skip (offset)

          team_id: Filter by team ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/team-members/staff/",
            page=SyncSkipLimitPage[TeamMemberListStaffResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                        "team_id": team_id,
                    },
                    team_member_list_staff_params.TeamMemberListStaffParams,
                ),
            ),
            model=cast(
                Any, TeamMemberListStaffResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )


class AsyncTeamMembersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTeamMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTeamMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return AsyncTeamMembersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        member: team_member_create_params.Member,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TeamMemberCreateResponse:
        """
        Add a new team member to a team.

        The request body is a **union type (oneOf)** - you must include the
        `member_type` discriminator field:

        - `"member_type": "player"` - Creates a player (requires position,
          jersey_number, etc.)
        - `"member_type": "coach"` - Creates a coach (requires specialty, etc.)
        - `"member_type": "medical_staff"` - Creates medical staff (requires medical
          specialty, etc.)
        - `"member_type": "equipment_manager"` - Creates equipment manager (requires
          responsibilities, etc.)

        The `character_id` field references an existing character from
        `/characters/{id}`.

        **Example for creating a player:**

        ```json
        {
          "member_type": "player",
          "character_id": "sam-obisanya",
          "team_id": "afc-richmond",
          "years_with_team": 2,
          "position": "midfielder",
          "jersey_number": 24,
          "goals_scored": 12,
          "assists": 15
        }
        ```

        Args:
          member: A football player on the team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            TeamMemberCreateResponse,
            await self._post(
                "/team-members",
                body=await async_maybe_transform(member, team_member_create_params.TeamMemberCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, TeamMemberCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TeamMemberRetrieveResponse:
        """
        Retrieve detailed information about a specific team member.

        The response is a **union type (oneOf)** - the actual shape depends on the
        member's type:

        - **player**: Includes position, jersey_number, goals_scored, assists,
          is_captain
        - **coach**: Includes specialty, certifications, win_rate
        - **medical_staff**: Includes specialty, qualifications, license_number
        - **equipment_manager**: Includes responsibilities, is_head_kitman

        Use `character_id` to fetch full character details from
        `/characters/{character_id}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return cast(
            TeamMemberRetrieveResponse,
            await self._get(
                f"/team-members/{member_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, TeamMemberRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        member_id: str,
        *,
        updates: team_member_update_params.Updates,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TeamMemberUpdateResponse:
        """Update specific fields of an existing team member.

        Fields vary by member type.

        Args:
          updates: Update model for players.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return cast(
            TeamMemberUpdateResponse,
            await self._patch(
                f"/team-members/{member_id}",
                body=await async_maybe_transform(updates, team_member_update_params.TeamMemberUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, TeamMemberUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        member_type: Optional[Literal["player", "coach", "medical_staff", "equipment_manager"]] | Omit = omit,
        skip: int | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TeamMemberListResponse, AsyncSkipLimitPage[TeamMemberListResponse]]:
        """
        Get a paginated list of all team members.

        This endpoint demonstrates **union types (oneOf)** in the response. Each team
        member can be one of: Player, Coach, MedicalStaff, or EquipmentManager. The
        `member_type` field acts as a discriminator to determine the shape of each
        object.

        Args:
          limit: Maximum number of items to return (max: 100)

          member_type: Filter by member type

          skip: Number of items to skip (offset)

          team_id: Filter by team ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/team-members",
            page=AsyncSkipLimitPage[TeamMemberListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "member_type": member_type,
                        "skip": skip,
                        "team_id": team_id,
                    },
                    team_member_list_params.TeamMemberListParams,
                ),
            ),
            model=cast(Any, TeamMemberListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def delete(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a team member from the roster.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/team-members/{member_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_coaches(
        self,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        specialty: Optional[CoachSpecialty] | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Coach, AsyncSkipLimitPage[Coach]]:
        """
        Get only coaches (filtered subset of team members).

        Args:
          limit: Maximum number of items to return (max: 100)

          skip: Number of items to skip (offset)

          specialty: Filter by specialty

          team_id: Filter by team ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/team-members/coaches/",
            page=AsyncSkipLimitPage[Coach],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                        "specialty": specialty,
                        "team_id": team_id,
                    },
                    team_member_list_coaches_params.TeamMemberListCoachesParams,
                ),
            ),
            model=Coach,
        )

    def list_players(
        self,
        *,
        limit: int | Omit = omit,
        position: Optional[Position] | Omit = omit,
        skip: int | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Player, AsyncSkipLimitPage[Player]]:
        """
        Get only players (filtered subset of team members).

        Args:
          limit: Maximum number of items to return (max: 100)

          position: Filter by position

          skip: Number of items to skip (offset)

          team_id: Filter by team ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/team-members/players/",
            page=AsyncSkipLimitPage[Player],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "position": position,
                        "skip": skip,
                        "team_id": team_id,
                    },
                    team_member_list_players_params.TeamMemberListPlayersParams,
                ),
            ),
            model=Player,
        )

    def list_staff(
        self,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TeamMemberListStaffResponse, AsyncSkipLimitPage[TeamMemberListStaffResponse]]:
        """
        Get all staff members (medical staff and equipment managers).

        This demonstrates a **narrower union type** - the response is oneOf MedicalStaff
        or EquipmentManager.

        Args:
          limit: Maximum number of items to return (max: 100)

          skip: Number of items to skip (offset)

          team_id: Filter by team ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/team-members/staff/",
            page=AsyncSkipLimitPage[TeamMemberListStaffResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                        "team_id": team_id,
                    },
                    team_member_list_staff_params.TeamMemberListStaffParams,
                ),
            ),
            model=cast(
                Any, TeamMemberListStaffResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )


class TeamMembersResourceWithRawResponse:
    def __init__(self, team_members: TeamMembersResource) -> None:
        self._team_members = team_members

        self.create = to_raw_response_wrapper(
            team_members.create,
        )
        self.retrieve = to_raw_response_wrapper(
            team_members.retrieve,
        )
        self.update = to_raw_response_wrapper(
            team_members.update,
        )
        self.list = to_raw_response_wrapper(
            team_members.list,
        )
        self.delete = to_raw_response_wrapper(
            team_members.delete,
        )
        self.list_coaches = to_raw_response_wrapper(
            team_members.list_coaches,
        )
        self.list_players = to_raw_response_wrapper(
            team_members.list_players,
        )
        self.list_staff = to_raw_response_wrapper(
            team_members.list_staff,
        )


class AsyncTeamMembersResourceWithRawResponse:
    def __init__(self, team_members: AsyncTeamMembersResource) -> None:
        self._team_members = team_members

        self.create = async_to_raw_response_wrapper(
            team_members.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            team_members.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            team_members.update,
        )
        self.list = async_to_raw_response_wrapper(
            team_members.list,
        )
        self.delete = async_to_raw_response_wrapper(
            team_members.delete,
        )
        self.list_coaches = async_to_raw_response_wrapper(
            team_members.list_coaches,
        )
        self.list_players = async_to_raw_response_wrapper(
            team_members.list_players,
        )
        self.list_staff = async_to_raw_response_wrapper(
            team_members.list_staff,
        )


class TeamMembersResourceWithStreamingResponse:
    def __init__(self, team_members: TeamMembersResource) -> None:
        self._team_members = team_members

        self.create = to_streamed_response_wrapper(
            team_members.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            team_members.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            team_members.update,
        )
        self.list = to_streamed_response_wrapper(
            team_members.list,
        )
        self.delete = to_streamed_response_wrapper(
            team_members.delete,
        )
        self.list_coaches = to_streamed_response_wrapper(
            team_members.list_coaches,
        )
        self.list_players = to_streamed_response_wrapper(
            team_members.list_players,
        )
        self.list_staff = to_streamed_response_wrapper(
            team_members.list_staff,
        )


class AsyncTeamMembersResourceWithStreamingResponse:
    def __init__(self, team_members: AsyncTeamMembersResource) -> None:
        self._team_members = team_members

        self.create = async_to_streamed_response_wrapper(
            team_members.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            team_members.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            team_members.update,
        )
        self.list = async_to_streamed_response_wrapper(
            team_members.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            team_members.delete,
        )
        self.list_coaches = async_to_streamed_response_wrapper(
            team_members.list_coaches,
        )
        self.list_players = async_to_streamed_response_wrapper(
            team_members.list_players,
        )
        self.list_staff = async_to_streamed_response_wrapper(
            team_members.list_staff,
        )
