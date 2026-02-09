# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from believe import Believe, AsyncBelieve
from tests.utils import assert_matches_type
from believe.types import (
    Coach,
    Player,
    TeamMemberListResponse,
    TeamMemberCreateResponse,
    TeamMemberUpdateResponse,
    TeamMemberRetrieveResponse,
    TeamMemberListStaffResponse,
)
from believe.pagination import SyncSkipLimitPage, AsyncSkipLimitPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTeamMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Believe) -> None:
        team_member = client.team_members.create(
            member={
                "character_id": "jamie-tartt",
                "jersey_number": 9,
                "position": "forward",
                "team_id": "afc-richmond",
                "years_with_team": 3,
                "member_type": "player",
            },
        )
        assert_matches_type(TeamMemberCreateResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Believe) -> None:
        team_member = client.team_members.create(
            member={
                "character_id": "jamie-tartt",
                "jersey_number": 9,
                "position": "forward",
                "team_id": "afc-richmond",
                "years_with_team": 3,
                "assists": 23,
                "goals_scored": 47,
                "is_captain": False,
                "member_type": "player",
            },
        )
        assert_matches_type(TeamMemberCreateResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Believe) -> None:
        response = client.team_members.with_raw_response.create(
            member={
                "character_id": "jamie-tartt",
                "jersey_number": 9,
                "position": "forward",
                "team_id": "afc-richmond",
                "years_with_team": 3,
                "member_type": "player",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = response.parse()
        assert_matches_type(TeamMemberCreateResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Believe) -> None:
        with client.team_members.with_streaming_response.create(
            member={
                "character_id": "jamie-tartt",
                "jersey_number": 9,
                "position": "forward",
                "team_id": "afc-richmond",
                "years_with_team": 3,
                "member_type": "player",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = response.parse()
            assert_matches_type(TeamMemberCreateResponse, team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Believe) -> None:
        team_member = client.team_members.retrieve(
            "member_id",
        )
        assert_matches_type(TeamMemberRetrieveResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Believe) -> None:
        response = client.team_members.with_raw_response.retrieve(
            "member_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = response.parse()
        assert_matches_type(TeamMemberRetrieveResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Believe) -> None:
        with client.team_members.with_streaming_response.retrieve(
            "member_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = response.parse()
            assert_matches_type(TeamMemberRetrieveResponse, team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.team_members.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Believe) -> None:
        team_member = client.team_members.update(
            member_id="member_id",
            updates={},
        )
        assert_matches_type(TeamMemberUpdateResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Believe) -> None:
        team_member = client.team_members.update(
            member_id="member_id",
            updates={
                "assists": 0,
                "goals_scored": 0,
                "is_captain": True,
                "jersey_number": 1,
                "position": "goalkeeper",
                "team_id": "team_id",
                "years_with_team": 0,
            },
        )
        assert_matches_type(TeamMemberUpdateResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Believe) -> None:
        response = client.team_members.with_raw_response.update(
            member_id="member_id",
            updates={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = response.parse()
        assert_matches_type(TeamMemberUpdateResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Believe) -> None:
        with client.team_members.with_streaming_response.update(
            member_id="member_id",
            updates={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = response.parse()
            assert_matches_type(TeamMemberUpdateResponse, team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.team_members.with_raw_response.update(
                member_id="",
                updates={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Believe) -> None:
        team_member = client.team_members.list()
        assert_matches_type(SyncSkipLimitPage[TeamMemberListResponse], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Believe) -> None:
        team_member = client.team_members.list(
            limit=10,
            member_type="player",
            skip=0,
            team_id="team_id",
        )
        assert_matches_type(SyncSkipLimitPage[TeamMemberListResponse], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Believe) -> None:
        response = client.team_members.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = response.parse()
        assert_matches_type(SyncSkipLimitPage[TeamMemberListResponse], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Believe) -> None:
        with client.team_members.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = response.parse()
            assert_matches_type(SyncSkipLimitPage[TeamMemberListResponse], team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Believe) -> None:
        team_member = client.team_members.delete(
            "member_id",
        )
        assert team_member is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Believe) -> None:
        response = client.team_members.with_raw_response.delete(
            "member_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = response.parse()
        assert team_member is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Believe) -> None:
        with client.team_members.with_streaming_response.delete(
            "member_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = response.parse()
            assert team_member is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.team_members.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_coaches(self, client: Believe) -> None:
        team_member = client.team_members.list_coaches()
        assert_matches_type(SyncSkipLimitPage[Coach], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_coaches_with_all_params(self, client: Believe) -> None:
        team_member = client.team_members.list_coaches(
            limit=10,
            skip=0,
            specialty="head_coach",
            team_id="team_id",
        )
        assert_matches_type(SyncSkipLimitPage[Coach], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_coaches(self, client: Believe) -> None:
        response = client.team_members.with_raw_response.list_coaches()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = response.parse()
        assert_matches_type(SyncSkipLimitPage[Coach], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_coaches(self, client: Believe) -> None:
        with client.team_members.with_streaming_response.list_coaches() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = response.parse()
            assert_matches_type(SyncSkipLimitPage[Coach], team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_players(self, client: Believe) -> None:
        team_member = client.team_members.list_players()
        assert_matches_type(SyncSkipLimitPage[Player], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_players_with_all_params(self, client: Believe) -> None:
        team_member = client.team_members.list_players(
            limit=10,
            position="goalkeeper",
            skip=0,
            team_id="team_id",
        )
        assert_matches_type(SyncSkipLimitPage[Player], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_players(self, client: Believe) -> None:
        response = client.team_members.with_raw_response.list_players()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = response.parse()
        assert_matches_type(SyncSkipLimitPage[Player], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_players(self, client: Believe) -> None:
        with client.team_members.with_streaming_response.list_players() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = response.parse()
            assert_matches_type(SyncSkipLimitPage[Player], team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_staff(self, client: Believe) -> None:
        team_member = client.team_members.list_staff()
        assert_matches_type(SyncSkipLimitPage[TeamMemberListStaffResponse], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_staff_with_all_params(self, client: Believe) -> None:
        team_member = client.team_members.list_staff(
            limit=10,
            skip=0,
            team_id="team_id",
        )
        assert_matches_type(SyncSkipLimitPage[TeamMemberListStaffResponse], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_staff(self, client: Believe) -> None:
        response = client.team_members.with_raw_response.list_staff()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = response.parse()
        assert_matches_type(SyncSkipLimitPage[TeamMemberListStaffResponse], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_staff(self, client: Believe) -> None:
        with client.team_members.with_streaming_response.list_staff() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = response.parse()
            assert_matches_type(SyncSkipLimitPage[TeamMemberListStaffResponse], team_member, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTeamMembers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBelieve) -> None:
        team_member = await async_client.team_members.create(
            member={
                "character_id": "jamie-tartt",
                "jersey_number": 9,
                "position": "forward",
                "team_id": "afc-richmond",
                "years_with_team": 3,
                "member_type": "player",
            },
        )
        assert_matches_type(TeamMemberCreateResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBelieve) -> None:
        team_member = await async_client.team_members.create(
            member={
                "character_id": "jamie-tartt",
                "jersey_number": 9,
                "position": "forward",
                "team_id": "afc-richmond",
                "years_with_team": 3,
                "assists": 23,
                "goals_scored": 47,
                "is_captain": False,
                "member_type": "player",
            },
        )
        assert_matches_type(TeamMemberCreateResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBelieve) -> None:
        response = await async_client.team_members.with_raw_response.create(
            member={
                "character_id": "jamie-tartt",
                "jersey_number": 9,
                "position": "forward",
                "team_id": "afc-richmond",
                "years_with_team": 3,
                "member_type": "player",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = await response.parse()
        assert_matches_type(TeamMemberCreateResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBelieve) -> None:
        async with async_client.team_members.with_streaming_response.create(
            member={
                "character_id": "jamie-tartt",
                "jersey_number": 9,
                "position": "forward",
                "team_id": "afc-richmond",
                "years_with_team": 3,
                "member_type": "player",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = await response.parse()
            assert_matches_type(TeamMemberCreateResponse, team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBelieve) -> None:
        team_member = await async_client.team_members.retrieve(
            "member_id",
        )
        assert_matches_type(TeamMemberRetrieveResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBelieve) -> None:
        response = await async_client.team_members.with_raw_response.retrieve(
            "member_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = await response.parse()
        assert_matches_type(TeamMemberRetrieveResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBelieve) -> None:
        async with async_client.team_members.with_streaming_response.retrieve(
            "member_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = await response.parse()
            assert_matches_type(TeamMemberRetrieveResponse, team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.team_members.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBelieve) -> None:
        team_member = await async_client.team_members.update(
            member_id="member_id",
            updates={},
        )
        assert_matches_type(TeamMemberUpdateResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBelieve) -> None:
        team_member = await async_client.team_members.update(
            member_id="member_id",
            updates={
                "assists": 0,
                "goals_scored": 0,
                "is_captain": True,
                "jersey_number": 1,
                "position": "goalkeeper",
                "team_id": "team_id",
                "years_with_team": 0,
            },
        )
        assert_matches_type(TeamMemberUpdateResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBelieve) -> None:
        response = await async_client.team_members.with_raw_response.update(
            member_id="member_id",
            updates={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = await response.parse()
        assert_matches_type(TeamMemberUpdateResponse, team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBelieve) -> None:
        async with async_client.team_members.with_streaming_response.update(
            member_id="member_id",
            updates={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = await response.parse()
            assert_matches_type(TeamMemberUpdateResponse, team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.team_members.with_raw_response.update(
                member_id="",
                updates={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBelieve) -> None:
        team_member = await async_client.team_members.list()
        assert_matches_type(AsyncSkipLimitPage[TeamMemberListResponse], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBelieve) -> None:
        team_member = await async_client.team_members.list(
            limit=10,
            member_type="player",
            skip=0,
            team_id="team_id",
        )
        assert_matches_type(AsyncSkipLimitPage[TeamMemberListResponse], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBelieve) -> None:
        response = await async_client.team_members.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = await response.parse()
        assert_matches_type(AsyncSkipLimitPage[TeamMemberListResponse], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBelieve) -> None:
        async with async_client.team_members.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = await response.parse()
            assert_matches_type(AsyncSkipLimitPage[TeamMemberListResponse], team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBelieve) -> None:
        team_member = await async_client.team_members.delete(
            "member_id",
        )
        assert team_member is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBelieve) -> None:
        response = await async_client.team_members.with_raw_response.delete(
            "member_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = await response.parse()
        assert team_member is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBelieve) -> None:
        async with async_client.team_members.with_streaming_response.delete(
            "member_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = await response.parse()
            assert team_member is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.team_members.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_coaches(self, async_client: AsyncBelieve) -> None:
        team_member = await async_client.team_members.list_coaches()
        assert_matches_type(AsyncSkipLimitPage[Coach], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_coaches_with_all_params(self, async_client: AsyncBelieve) -> None:
        team_member = await async_client.team_members.list_coaches(
            limit=10,
            skip=0,
            specialty="head_coach",
            team_id="team_id",
        )
        assert_matches_type(AsyncSkipLimitPage[Coach], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_coaches(self, async_client: AsyncBelieve) -> None:
        response = await async_client.team_members.with_raw_response.list_coaches()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = await response.parse()
        assert_matches_type(AsyncSkipLimitPage[Coach], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_coaches(self, async_client: AsyncBelieve) -> None:
        async with async_client.team_members.with_streaming_response.list_coaches() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = await response.parse()
            assert_matches_type(AsyncSkipLimitPage[Coach], team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_players(self, async_client: AsyncBelieve) -> None:
        team_member = await async_client.team_members.list_players()
        assert_matches_type(AsyncSkipLimitPage[Player], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_players_with_all_params(self, async_client: AsyncBelieve) -> None:
        team_member = await async_client.team_members.list_players(
            limit=10,
            position="goalkeeper",
            skip=0,
            team_id="team_id",
        )
        assert_matches_type(AsyncSkipLimitPage[Player], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_players(self, async_client: AsyncBelieve) -> None:
        response = await async_client.team_members.with_raw_response.list_players()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = await response.parse()
        assert_matches_type(AsyncSkipLimitPage[Player], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_players(self, async_client: AsyncBelieve) -> None:
        async with async_client.team_members.with_streaming_response.list_players() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = await response.parse()
            assert_matches_type(AsyncSkipLimitPage[Player], team_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_staff(self, async_client: AsyncBelieve) -> None:
        team_member = await async_client.team_members.list_staff()
        assert_matches_type(AsyncSkipLimitPage[TeamMemberListStaffResponse], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_staff_with_all_params(self, async_client: AsyncBelieve) -> None:
        team_member = await async_client.team_members.list_staff(
            limit=10,
            skip=0,
            team_id="team_id",
        )
        assert_matches_type(AsyncSkipLimitPage[TeamMemberListStaffResponse], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_staff(self, async_client: AsyncBelieve) -> None:
        response = await async_client.team_members.with_raw_response.list_staff()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team_member = await response.parse()
        assert_matches_type(AsyncSkipLimitPage[TeamMemberListStaffResponse], team_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_staff(self, async_client: AsyncBelieve) -> None:
        async with async_client.team_members.with_streaming_response.list_staff() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team_member = await response.parse()
            assert_matches_type(AsyncSkipLimitPage[TeamMemberListStaffResponse], team_member, path=["response"])

        assert cast(Any, response.is_closed) is True
