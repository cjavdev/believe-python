# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from believe import Believe, AsyncBelieve
from tests.utils import assert_matches_type
from believe.types import (
    Match,
    MatchGetLessonResponse,
    MatchGetTurningPointsResponse,
)
from believe._utils import parse_datetime
from believe.pagination import SyncSkipLimitPage, AsyncSkipLimitPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMatches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Believe) -> None:
        match = client.matches.create(
            away_team_id="tottenham",
            date=parse_datetime("2024-02-20T19:45:00Z"),
            home_team_id="afc-richmond",
            match_type="cup",
        )
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Believe) -> None:
        match = client.matches.create(
            away_team_id="tottenham",
            date=parse_datetime("2024-02-20T19:45:00Z"),
            home_team_id="afc-richmond",
            match_type="cup",
            attendance=24500,
            away_score=0,
            episode_id="s02e05",
            home_score=0,
            lesson_learned="It's not about the wins and losses, it's about helping these young fellas be the best versions of themselves.",
            possession_percentage=50,
            result="pending",
            ted_halftime_speech="You know what the happiest animal on Earth is? It's a goldfish. You know why? It's got a 10-second memory.",
            ticket_revenue_gbp="735000.00",
            turning_points=[
                {
                    "description": "description",
                    "emotional_impact": "Galvanized the team's fighting spirit",
                    "minute": 0,
                    "character_involved": "jamie-tartt",
                }
            ],
            weather_temp_celsius=8.5,
        )
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Believe) -> None:
        response = client.matches.with_raw_response.create(
            away_team_id="tottenham",
            date=parse_datetime("2024-02-20T19:45:00Z"),
            home_team_id="afc-richmond",
            match_type="cup",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = response.parse()
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Believe) -> None:
        with client.matches.with_streaming_response.create(
            away_team_id="tottenham",
            date=parse_datetime("2024-02-20T19:45:00Z"),
            home_team_id="afc-richmond",
            match_type="cup",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = response.parse()
            assert_matches_type(Match, match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Believe) -> None:
        match = client.matches.retrieve(
            "match_id",
        )
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Believe) -> None:
        response = client.matches.with_raw_response.retrieve(
            "match_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = response.parse()
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Believe) -> None:
        with client.matches.with_streaming_response.retrieve(
            "match_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = response.parse()
            assert_matches_type(Match, match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `match_id` but received ''"):
            client.matches.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Believe) -> None:
        match = client.matches.update(
            match_id="match_id",
        )
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Believe) -> None:
        match = client.matches.update(
            match_id="match_id",
            attendance=0,
            away_score=0,
            away_team_id="away_team_id",
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            episode_id="episode_id",
            home_score=0,
            home_team_id="home_team_id",
            lesson_learned="lesson_learned",
            match_type="league",
            possession_percentage=0,
            result="win",
            ted_halftime_speech="ted_halftime_speech",
            ticket_revenue_gbp=0,
            turning_points=[
                {
                    "description": "description",
                    "emotional_impact": "Galvanized the team's fighting spirit",
                    "minute": 0,
                    "character_involved": "jamie-tartt",
                }
            ],
            weather_temp_celsius=-30,
        )
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Believe) -> None:
        response = client.matches.with_raw_response.update(
            match_id="match_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = response.parse()
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Believe) -> None:
        with client.matches.with_streaming_response.update(
            match_id="match_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = response.parse()
            assert_matches_type(Match, match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `match_id` but received ''"):
            client.matches.with_raw_response.update(
                match_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Believe) -> None:
        match = client.matches.list()
        assert_matches_type(SyncSkipLimitPage[Match], match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Believe) -> None:
        match = client.matches.list(
            limit=10,
            match_type="league",
            result="win",
            skip=0,
            team_id="team_id",
        )
        assert_matches_type(SyncSkipLimitPage[Match], match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Believe) -> None:
        response = client.matches.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = response.parse()
        assert_matches_type(SyncSkipLimitPage[Match], match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Believe) -> None:
        with client.matches.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = response.parse()
            assert_matches_type(SyncSkipLimitPage[Match], match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Believe) -> None:
        match = client.matches.delete(
            "match_id",
        )
        assert match is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Believe) -> None:
        response = client.matches.with_raw_response.delete(
            "match_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = response.parse()
        assert match is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Believe) -> None:
        with client.matches.with_streaming_response.delete(
            "match_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = response.parse()
            assert match is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `match_id` but received ''"):
            client.matches.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_lesson(self, client: Believe) -> None:
        match = client.matches.get_lesson(
            "match_id",
        )
        assert_matches_type(MatchGetLessonResponse, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_lesson(self, client: Believe) -> None:
        response = client.matches.with_raw_response.get_lesson(
            "match_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = response.parse()
        assert_matches_type(MatchGetLessonResponse, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_lesson(self, client: Believe) -> None:
        with client.matches.with_streaming_response.get_lesson(
            "match_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = response.parse()
            assert_matches_type(MatchGetLessonResponse, match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_lesson(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `match_id` but received ''"):
            client.matches.with_raw_response.get_lesson(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_turning_points(self, client: Believe) -> None:
        match = client.matches.get_turning_points(
            "match_id",
        )
        assert_matches_type(MatchGetTurningPointsResponse, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_turning_points(self, client: Believe) -> None:
        response = client.matches.with_raw_response.get_turning_points(
            "match_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = response.parse()
        assert_matches_type(MatchGetTurningPointsResponse, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_turning_points(self, client: Believe) -> None:
        with client.matches.with_streaming_response.get_turning_points(
            "match_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = response.parse()
            assert_matches_type(MatchGetTurningPointsResponse, match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_turning_points(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `match_id` but received ''"):
            client.matches.with_raw_response.get_turning_points(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_live(self, client: Believe) -> None:
        match = client.matches.stream_live()
        assert match is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_live_with_all_params(self, client: Believe) -> None:
        match = client.matches.stream_live(
            away_team="away_team",
            excitement_level=1,
            home_team="home_team",
            speed=0.1,
        )
        assert match is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_live(self, client: Believe) -> None:
        response = client.matches.with_raw_response.stream_live()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = response.parse()
        assert match is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_live(self, client: Believe) -> None:
        with client.matches.with_streaming_response.stream_live() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = response.parse()
            assert match is None

        assert cast(Any, response.is_closed) is True


class TestAsyncMatches:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBelieve) -> None:
        match = await async_client.matches.create(
            away_team_id="tottenham",
            date=parse_datetime("2024-02-20T19:45:00Z"),
            home_team_id="afc-richmond",
            match_type="cup",
        )
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBelieve) -> None:
        match = await async_client.matches.create(
            away_team_id="tottenham",
            date=parse_datetime("2024-02-20T19:45:00Z"),
            home_team_id="afc-richmond",
            match_type="cup",
            attendance=24500,
            away_score=0,
            episode_id="s02e05",
            home_score=0,
            lesson_learned="It's not about the wins and losses, it's about helping these young fellas be the best versions of themselves.",
            possession_percentage=50,
            result="pending",
            ted_halftime_speech="You know what the happiest animal on Earth is? It's a goldfish. You know why? It's got a 10-second memory.",
            ticket_revenue_gbp="735000.00",
            turning_points=[
                {
                    "description": "description",
                    "emotional_impact": "Galvanized the team's fighting spirit",
                    "minute": 0,
                    "character_involved": "jamie-tartt",
                }
            ],
            weather_temp_celsius=8.5,
        )
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBelieve) -> None:
        response = await async_client.matches.with_raw_response.create(
            away_team_id="tottenham",
            date=parse_datetime("2024-02-20T19:45:00Z"),
            home_team_id="afc-richmond",
            match_type="cup",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = await response.parse()
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBelieve) -> None:
        async with async_client.matches.with_streaming_response.create(
            away_team_id="tottenham",
            date=parse_datetime("2024-02-20T19:45:00Z"),
            home_team_id="afc-richmond",
            match_type="cup",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = await response.parse()
            assert_matches_type(Match, match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBelieve) -> None:
        match = await async_client.matches.retrieve(
            "match_id",
        )
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBelieve) -> None:
        response = await async_client.matches.with_raw_response.retrieve(
            "match_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = await response.parse()
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBelieve) -> None:
        async with async_client.matches.with_streaming_response.retrieve(
            "match_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = await response.parse()
            assert_matches_type(Match, match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `match_id` but received ''"):
            await async_client.matches.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBelieve) -> None:
        match = await async_client.matches.update(
            match_id="match_id",
        )
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBelieve) -> None:
        match = await async_client.matches.update(
            match_id="match_id",
            attendance=0,
            away_score=0,
            away_team_id="away_team_id",
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            episode_id="episode_id",
            home_score=0,
            home_team_id="home_team_id",
            lesson_learned="lesson_learned",
            match_type="league",
            possession_percentage=0,
            result="win",
            ted_halftime_speech="ted_halftime_speech",
            ticket_revenue_gbp=0,
            turning_points=[
                {
                    "description": "description",
                    "emotional_impact": "Galvanized the team's fighting spirit",
                    "minute": 0,
                    "character_involved": "jamie-tartt",
                }
            ],
            weather_temp_celsius=-30,
        )
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBelieve) -> None:
        response = await async_client.matches.with_raw_response.update(
            match_id="match_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = await response.parse()
        assert_matches_type(Match, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBelieve) -> None:
        async with async_client.matches.with_streaming_response.update(
            match_id="match_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = await response.parse()
            assert_matches_type(Match, match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `match_id` but received ''"):
            await async_client.matches.with_raw_response.update(
                match_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBelieve) -> None:
        match = await async_client.matches.list()
        assert_matches_type(AsyncSkipLimitPage[Match], match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBelieve) -> None:
        match = await async_client.matches.list(
            limit=10,
            match_type="league",
            result="win",
            skip=0,
            team_id="team_id",
        )
        assert_matches_type(AsyncSkipLimitPage[Match], match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBelieve) -> None:
        response = await async_client.matches.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = await response.parse()
        assert_matches_type(AsyncSkipLimitPage[Match], match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBelieve) -> None:
        async with async_client.matches.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = await response.parse()
            assert_matches_type(AsyncSkipLimitPage[Match], match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBelieve) -> None:
        match = await async_client.matches.delete(
            "match_id",
        )
        assert match is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBelieve) -> None:
        response = await async_client.matches.with_raw_response.delete(
            "match_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = await response.parse()
        assert match is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBelieve) -> None:
        async with async_client.matches.with_streaming_response.delete(
            "match_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = await response.parse()
            assert match is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `match_id` but received ''"):
            await async_client.matches.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_lesson(self, async_client: AsyncBelieve) -> None:
        match = await async_client.matches.get_lesson(
            "match_id",
        )
        assert_matches_type(MatchGetLessonResponse, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_lesson(self, async_client: AsyncBelieve) -> None:
        response = await async_client.matches.with_raw_response.get_lesson(
            "match_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = await response.parse()
        assert_matches_type(MatchGetLessonResponse, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_lesson(self, async_client: AsyncBelieve) -> None:
        async with async_client.matches.with_streaming_response.get_lesson(
            "match_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = await response.parse()
            assert_matches_type(MatchGetLessonResponse, match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_lesson(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `match_id` but received ''"):
            await async_client.matches.with_raw_response.get_lesson(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_turning_points(self, async_client: AsyncBelieve) -> None:
        match = await async_client.matches.get_turning_points(
            "match_id",
        )
        assert_matches_type(MatchGetTurningPointsResponse, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_turning_points(self, async_client: AsyncBelieve) -> None:
        response = await async_client.matches.with_raw_response.get_turning_points(
            "match_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = await response.parse()
        assert_matches_type(MatchGetTurningPointsResponse, match, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_turning_points(self, async_client: AsyncBelieve) -> None:
        async with async_client.matches.with_streaming_response.get_turning_points(
            "match_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = await response.parse()
            assert_matches_type(MatchGetTurningPointsResponse, match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_turning_points(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `match_id` but received ''"):
            await async_client.matches.with_raw_response.get_turning_points(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_live(self, async_client: AsyncBelieve) -> None:
        match = await async_client.matches.stream_live()
        assert match is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_live_with_all_params(self, async_client: AsyncBelieve) -> None:
        match = await async_client.matches.stream_live(
            away_team="away_team",
            excitement_level=1,
            home_team="home_team",
            speed=0.1,
        )
        assert match is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_live(self, async_client: AsyncBelieve) -> None:
        response = await async_client.matches.with_raw_response.stream_live()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = await response.parse()
        assert match is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_live(self, async_client: AsyncBelieve) -> None:
        async with async_client.matches.with_streaming_response.stream_live() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = await response.parse()
            assert match is None

        assert cast(Any, response.is_closed) is True
