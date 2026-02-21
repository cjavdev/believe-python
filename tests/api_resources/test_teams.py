# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from believe import Believe, AsyncBelieve
from tests.utils import assert_matches_type
from believe.types import (
    Team,
    TeamGetRivalsResponse,
    TeamListLogosResponse,
    TeamGetCultureResponse,
)
from believe.pagination import SyncSkipLimitPage, AsyncSkipLimitPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTeams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Believe) -> None:
        team = client.teams.create(
            culture_score=70,
            founded_year=1895,
            league="Premier League",
            name="West Ham United",
            stadium="London Stadium",
            values={
                "primary_value": "Pride",
                "secondary_values": ["History", "Community", "Passion"],
                "team_motto": "Forever Blowing Bubbles",
            },
        )
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Believe) -> None:
        team = client.teams.create(
            culture_score=70,
            founded_year=1895,
            league="Premier League",
            name="West Ham United",
            stadium="London Stadium",
            values={
                "primary_value": "Pride",
                "secondary_values": ["History", "Community", "Passion"],
                "team_motto": "Forever Blowing Bubbles",
            },
            annual_budget_gbp="150000000.00",
            average_attendance=59988,
            contact_email="info@westhamunited.co.uk",
            is_active=True,
            nickname="The Hammers",
            primary_color="#7A263A",
            rival_teams=["afc-richmond", "tottenham"],
            secondary_color="#1BB1E7",
            stadium_location={
                "latitude": 51.5387,
                "longitude": -0.0166,
            },
            website="https://www.whufc.com",
            win_percentage=52.3,
        )
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Believe) -> None:
        response = client.teams.with_raw_response.create(
            culture_score=70,
            founded_year=1895,
            league="Premier League",
            name="West Ham United",
            stadium="London Stadium",
            values={
                "primary_value": "Pride",
                "secondary_values": ["History", "Community", "Passion"],
                "team_motto": "Forever Blowing Bubbles",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Believe) -> None:
        with client.teams.with_streaming_response.create(
            culture_score=70,
            founded_year=1895,
            league="Premier League",
            name="West Ham United",
            stadium="London Stadium",
            values={
                "primary_value": "Pride",
                "secondary_values": ["History", "Community", "Passion"],
                "team_motto": "Forever Blowing Bubbles",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(Team, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Believe) -> None:
        team = client.teams.retrieve(
            "team_id",
        )
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Believe) -> None:
        response = client.teams.with_raw_response.retrieve(
            "team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Believe) -> None:
        with client.teams.with_streaming_response.retrieve(
            "team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(Team, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Believe) -> None:
        team = client.teams.update(
            team_id="team_id",
        )
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Believe) -> None:
        team = client.teams.update(
            team_id="team_id",
            annual_budget_gbp=0,
            average_attendance=0,
            contact_email="dev@stainless.com",
            culture_score=0,
            founded_year=1800,
            is_active=True,
            league="Premier League",
            name="x",
            nickname="nickname",
            primary_color="primary_color",
            rival_teams=["string"],
            secondary_color="secondary_color",
            stadium="stadium",
            stadium_location={
                "latitude": 51.4816,
                "longitude": -0.191,
            },
            values={
                "primary_value": "Believe",
                "secondary_values": ["Family", "Resilience", "Joy"],
                "team_motto": "Football is life!",
            },
            website="https://example.com",
            win_percentage=0,
        )
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Believe) -> None:
        response = client.teams.with_raw_response.update(
            team_id="team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Believe) -> None:
        with client.teams.with_streaming_response.update(
            team_id="team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(Team, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.with_raw_response.update(
                team_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Believe) -> None:
        team = client.teams.list()
        assert_matches_type(SyncSkipLimitPage[Team], team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Believe) -> None:
        team = client.teams.list(
            league="Premier League",
            limit=10,
            min_culture_score=0,
            skip=0,
        )
        assert_matches_type(SyncSkipLimitPage[Team], team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Believe) -> None:
        response = client.teams.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(SyncSkipLimitPage[Team], team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Believe) -> None:
        with client.teams.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(SyncSkipLimitPage[Team], team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Believe) -> None:
        team = client.teams.delete(
            "team_id",
        )
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Believe) -> None:
        response = client.teams.with_raw_response.delete(
            "team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Believe) -> None:
        with client.teams.with_streaming_response.delete(
            "team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert team is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_culture(self, client: Believe) -> None:
        team = client.teams.get_culture(
            "team_id",
        )
        assert_matches_type(TeamGetCultureResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_culture(self, client: Believe) -> None:
        response = client.teams.with_raw_response.get_culture(
            "team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(TeamGetCultureResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_culture(self, client: Believe) -> None:
        with client.teams.with_streaming_response.get_culture(
            "team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(TeamGetCultureResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_culture(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.with_raw_response.get_culture(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_rivals(self, client: Believe) -> None:
        team = client.teams.get_rivals(
            "team_id",
        )
        assert_matches_type(TeamGetRivalsResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_rivals(self, client: Believe) -> None:
        response = client.teams.with_raw_response.get_rivals(
            "team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(TeamGetRivalsResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_rivals(self, client: Believe) -> None:
        with client.teams.with_streaming_response.get_rivals(
            "team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(TeamGetRivalsResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_rivals(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.with_raw_response.get_rivals(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_logos(self, client: Believe) -> None:
        team = client.teams.list_logos(
            "team_id",
        )
        assert_matches_type(TeamListLogosResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_logos(self, client: Believe) -> None:
        response = client.teams.with_raw_response.list_logos(
            "team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(TeamListLogosResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_logos(self, client: Believe) -> None:
        with client.teams.with_streaming_response.list_logos(
            "team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(TeamListLogosResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_logos(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.with_raw_response.list_logos(
                "",
            )


class TestAsyncTeams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBelieve) -> None:
        team = await async_client.teams.create(
            culture_score=70,
            founded_year=1895,
            league="Premier League",
            name="West Ham United",
            stadium="London Stadium",
            values={
                "primary_value": "Pride",
                "secondary_values": ["History", "Community", "Passion"],
                "team_motto": "Forever Blowing Bubbles",
            },
        )
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBelieve) -> None:
        team = await async_client.teams.create(
            culture_score=70,
            founded_year=1895,
            league="Premier League",
            name="West Ham United",
            stadium="London Stadium",
            values={
                "primary_value": "Pride",
                "secondary_values": ["History", "Community", "Passion"],
                "team_motto": "Forever Blowing Bubbles",
            },
            annual_budget_gbp="150000000.00",
            average_attendance=59988,
            contact_email="info@westhamunited.co.uk",
            is_active=True,
            nickname="The Hammers",
            primary_color="#7A263A",
            rival_teams=["afc-richmond", "tottenham"],
            secondary_color="#1BB1E7",
            stadium_location={
                "latitude": 51.5387,
                "longitude": -0.0166,
            },
            website="https://www.whufc.com",
            win_percentage=52.3,
        )
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBelieve) -> None:
        response = await async_client.teams.with_raw_response.create(
            culture_score=70,
            founded_year=1895,
            league="Premier League",
            name="West Ham United",
            stadium="London Stadium",
            values={
                "primary_value": "Pride",
                "secondary_values": ["History", "Community", "Passion"],
                "team_motto": "Forever Blowing Bubbles",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBelieve) -> None:
        async with async_client.teams.with_streaming_response.create(
            culture_score=70,
            founded_year=1895,
            league="Premier League",
            name="West Ham United",
            stadium="London Stadium",
            values={
                "primary_value": "Pride",
                "secondary_values": ["History", "Community", "Passion"],
                "team_motto": "Forever Blowing Bubbles",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(Team, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBelieve) -> None:
        team = await async_client.teams.retrieve(
            "team_id",
        )
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBelieve) -> None:
        response = await async_client.teams.with_raw_response.retrieve(
            "team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBelieve) -> None:
        async with async_client.teams.with_streaming_response.retrieve(
            "team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(Team, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBelieve) -> None:
        team = await async_client.teams.update(
            team_id="team_id",
        )
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBelieve) -> None:
        team = await async_client.teams.update(
            team_id="team_id",
            annual_budget_gbp=0,
            average_attendance=0,
            contact_email="dev@stainless.com",
            culture_score=0,
            founded_year=1800,
            is_active=True,
            league="Premier League",
            name="x",
            nickname="nickname",
            primary_color="primary_color",
            rival_teams=["string"],
            secondary_color="secondary_color",
            stadium="stadium",
            stadium_location={
                "latitude": 51.4816,
                "longitude": -0.191,
            },
            values={
                "primary_value": "Believe",
                "secondary_values": ["Family", "Resilience", "Joy"],
                "team_motto": "Football is life!",
            },
            website="https://example.com",
            win_percentage=0,
        )
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBelieve) -> None:
        response = await async_client.teams.with_raw_response.update(
            team_id="team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(Team, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBelieve) -> None:
        async with async_client.teams.with_streaming_response.update(
            team_id="team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(Team, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.with_raw_response.update(
                team_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBelieve) -> None:
        team = await async_client.teams.list()
        assert_matches_type(AsyncSkipLimitPage[Team], team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBelieve) -> None:
        team = await async_client.teams.list(
            league="Premier League",
            limit=10,
            min_culture_score=0,
            skip=0,
        )
        assert_matches_type(AsyncSkipLimitPage[Team], team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBelieve) -> None:
        response = await async_client.teams.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(AsyncSkipLimitPage[Team], team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBelieve) -> None:
        async with async_client.teams.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(AsyncSkipLimitPage[Team], team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBelieve) -> None:
        team = await async_client.teams.delete(
            "team_id",
        )
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBelieve) -> None:
        response = await async_client.teams.with_raw_response.delete(
            "team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBelieve) -> None:
        async with async_client.teams.with_streaming_response.delete(
            "team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert team is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_culture(self, async_client: AsyncBelieve) -> None:
        team = await async_client.teams.get_culture(
            "team_id",
        )
        assert_matches_type(TeamGetCultureResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_culture(self, async_client: AsyncBelieve) -> None:
        response = await async_client.teams.with_raw_response.get_culture(
            "team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(TeamGetCultureResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_culture(self, async_client: AsyncBelieve) -> None:
        async with async_client.teams.with_streaming_response.get_culture(
            "team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(TeamGetCultureResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_culture(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.with_raw_response.get_culture(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_rivals(self, async_client: AsyncBelieve) -> None:
        team = await async_client.teams.get_rivals(
            "team_id",
        )
        assert_matches_type(TeamGetRivalsResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_rivals(self, async_client: AsyncBelieve) -> None:
        response = await async_client.teams.with_raw_response.get_rivals(
            "team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(TeamGetRivalsResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_rivals(self, async_client: AsyncBelieve) -> None:
        async with async_client.teams.with_streaming_response.get_rivals(
            "team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(TeamGetRivalsResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_rivals(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.with_raw_response.get_rivals(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_logos(self, async_client: AsyncBelieve) -> None:
        team = await async_client.teams.list_logos(
            "team_id",
        )
        assert_matches_type(TeamListLogosResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_logos(self, async_client: AsyncBelieve) -> None:
        response = await async_client.teams.with_raw_response.list_logos(
            "team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(TeamListLogosResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_logos(self, async_client: AsyncBelieve) -> None:
        async with async_client.teams.with_streaming_response.list_logos(
            "team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(TeamListLogosResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_logos(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.with_raw_response.list_logos(
                "",
            )
