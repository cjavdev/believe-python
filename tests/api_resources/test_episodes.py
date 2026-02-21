# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from believe import Believe, AsyncBelieve
from tests.utils import assert_matches_type
from believe.types import (
    Episode,
    EpisodeGetWisdomResponse,
)
from believe._utils import parse_date
from believe.pagination import SyncSkipLimitPage, AsyncSkipLimitPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEpisodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Believe) -> None:
        episode = client.episodes.create(
            air_date=parse_date("2020-10-02"),
            character_focus=["ted-lasso", "coach-beard", "higgins", "nate"],
            director="MJ Delaney",
            episode_number=8,
            main_theme="The power of vulnerability and male friendship",
            runtime_minutes=29,
            season=1,
            synopsis="Ted creates a support group for the coaching staff while Rebecca faces a difficult decision about her future.",
            ted_wisdom="There's two buttons I never like to hit: that's panic and snooze.",
            title="The Diamond Dogs",
            writer="Jason Sudeikis, Brendan Hunt, Joe Kelly",
        )
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Believe) -> None:
        episode = client.episodes.create(
            air_date=parse_date("2020-10-02"),
            character_focus=["ted-lasso", "coach-beard", "higgins", "nate"],
            director="MJ Delaney",
            episode_number=8,
            main_theme="The power of vulnerability and male friendship",
            runtime_minutes=29,
            season=1,
            synopsis="Ted creates a support group for the coaching staff while Rebecca faces a difficult decision about her future.",
            ted_wisdom="There's two buttons I never like to hit: that's panic and snooze.",
            title="The Diamond Dogs",
            writer="Jason Sudeikis, Brendan Hunt, Joe Kelly",
            biscuits_with_boss_moment="Ted and Rebecca have an honest conversation about trust.",
            memorable_moments=[
                "First Diamond Dogs meeting",
                "The famous dart scene with Rupert",
                "Be curious, not judgmental speech",
            ],
            us_viewers_millions=1.42,
            viewer_rating=9.1,
        )
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Believe) -> None:
        response = client.episodes.with_raw_response.create(
            air_date=parse_date("2020-10-02"),
            character_focus=["ted-lasso", "coach-beard", "higgins", "nate"],
            director="MJ Delaney",
            episode_number=8,
            main_theme="The power of vulnerability and male friendship",
            runtime_minutes=29,
            season=1,
            synopsis="Ted creates a support group for the coaching staff while Rebecca faces a difficult decision about her future.",
            ted_wisdom="There's two buttons I never like to hit: that's panic and snooze.",
            title="The Diamond Dogs",
            writer="Jason Sudeikis, Brendan Hunt, Joe Kelly",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode = response.parse()
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Believe) -> None:
        with client.episodes.with_streaming_response.create(
            air_date=parse_date("2020-10-02"),
            character_focus=["ted-lasso", "coach-beard", "higgins", "nate"],
            director="MJ Delaney",
            episode_number=8,
            main_theme="The power of vulnerability and male friendship",
            runtime_minutes=29,
            season=1,
            synopsis="Ted creates a support group for the coaching staff while Rebecca faces a difficult decision about her future.",
            ted_wisdom="There's two buttons I never like to hit: that's panic and snooze.",
            title="The Diamond Dogs",
            writer="Jason Sudeikis, Brendan Hunt, Joe Kelly",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode = response.parse()
            assert_matches_type(Episode, episode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Believe) -> None:
        episode = client.episodes.retrieve(
            "episode_id",
        )
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Believe) -> None:
        response = client.episodes.with_raw_response.retrieve(
            "episode_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode = response.parse()
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Believe) -> None:
        with client.episodes.with_streaming_response.retrieve(
            "episode_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode = response.parse()
            assert_matches_type(Episode, episode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `episode_id` but received ''"):
            client.episodes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Believe) -> None:
        episode = client.episodes.update(
            episode_id="episode_id",
        )
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Believe) -> None:
        episode = client.episodes.update(
            episode_id="episode_id",
            air_date=parse_date("2019-12-27"),
            biscuits_with_boss_moment="biscuits_with_boss_moment",
            character_focus=["string"],
            director="director",
            episode_number=1,
            main_theme="main_theme",
            memorable_moments=["string"],
            runtime_minutes=20,
            season=1,
            synopsis="synopsis",
            ted_wisdom="ted_wisdom",
            title="x",
            us_viewers_millions=0,
            viewer_rating=0,
            writer="writer",
        )
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Believe) -> None:
        response = client.episodes.with_raw_response.update(
            episode_id="episode_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode = response.parse()
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Believe) -> None:
        with client.episodes.with_streaming_response.update(
            episode_id="episode_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode = response.parse()
            assert_matches_type(Episode, episode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `episode_id` but received ''"):
            client.episodes.with_raw_response.update(
                episode_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Believe) -> None:
        episode = client.episodes.list()
        assert_matches_type(SyncSkipLimitPage[Episode], episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Believe) -> None:
        episode = client.episodes.list(
            character_focus="character_focus",
            limit=10,
            season=1,
            skip=0,
        )
        assert_matches_type(SyncSkipLimitPage[Episode], episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Believe) -> None:
        response = client.episodes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode = response.parse()
        assert_matches_type(SyncSkipLimitPage[Episode], episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Believe) -> None:
        with client.episodes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode = response.parse()
            assert_matches_type(SyncSkipLimitPage[Episode], episode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Believe) -> None:
        episode = client.episodes.delete(
            "episode_id",
        )
        assert episode is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Believe) -> None:
        response = client.episodes.with_raw_response.delete(
            "episode_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode = response.parse()
        assert episode is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Believe) -> None:
        with client.episodes.with_streaming_response.delete(
            "episode_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode = response.parse()
            assert episode is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `episode_id` but received ''"):
            client.episodes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_wisdom(self, client: Believe) -> None:
        episode = client.episodes.get_wisdom(
            "episode_id",
        )
        assert_matches_type(EpisodeGetWisdomResponse, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_wisdom(self, client: Believe) -> None:
        response = client.episodes.with_raw_response.get_wisdom(
            "episode_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode = response.parse()
        assert_matches_type(EpisodeGetWisdomResponse, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_wisdom(self, client: Believe) -> None:
        with client.episodes.with_streaming_response.get_wisdom(
            "episode_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode = response.parse()
            assert_matches_type(EpisodeGetWisdomResponse, episode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_wisdom(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `episode_id` but received ''"):
            client.episodes.with_raw_response.get_wisdom(
                "",
            )


class TestAsyncEpisodes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBelieve) -> None:
        episode = await async_client.episodes.create(
            air_date=parse_date("2020-10-02"),
            character_focus=["ted-lasso", "coach-beard", "higgins", "nate"],
            director="MJ Delaney",
            episode_number=8,
            main_theme="The power of vulnerability and male friendship",
            runtime_minutes=29,
            season=1,
            synopsis="Ted creates a support group for the coaching staff while Rebecca faces a difficult decision about her future.",
            ted_wisdom="There's two buttons I never like to hit: that's panic and snooze.",
            title="The Diamond Dogs",
            writer="Jason Sudeikis, Brendan Hunt, Joe Kelly",
        )
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBelieve) -> None:
        episode = await async_client.episodes.create(
            air_date=parse_date("2020-10-02"),
            character_focus=["ted-lasso", "coach-beard", "higgins", "nate"],
            director="MJ Delaney",
            episode_number=8,
            main_theme="The power of vulnerability and male friendship",
            runtime_minutes=29,
            season=1,
            synopsis="Ted creates a support group for the coaching staff while Rebecca faces a difficult decision about her future.",
            ted_wisdom="There's two buttons I never like to hit: that's panic and snooze.",
            title="The Diamond Dogs",
            writer="Jason Sudeikis, Brendan Hunt, Joe Kelly",
            biscuits_with_boss_moment="Ted and Rebecca have an honest conversation about trust.",
            memorable_moments=[
                "First Diamond Dogs meeting",
                "The famous dart scene with Rupert",
                "Be curious, not judgmental speech",
            ],
            us_viewers_millions=1.42,
            viewer_rating=9.1,
        )
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBelieve) -> None:
        response = await async_client.episodes.with_raw_response.create(
            air_date=parse_date("2020-10-02"),
            character_focus=["ted-lasso", "coach-beard", "higgins", "nate"],
            director="MJ Delaney",
            episode_number=8,
            main_theme="The power of vulnerability and male friendship",
            runtime_minutes=29,
            season=1,
            synopsis="Ted creates a support group for the coaching staff while Rebecca faces a difficult decision about her future.",
            ted_wisdom="There's two buttons I never like to hit: that's panic and snooze.",
            title="The Diamond Dogs",
            writer="Jason Sudeikis, Brendan Hunt, Joe Kelly",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode = await response.parse()
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBelieve) -> None:
        async with async_client.episodes.with_streaming_response.create(
            air_date=parse_date("2020-10-02"),
            character_focus=["ted-lasso", "coach-beard", "higgins", "nate"],
            director="MJ Delaney",
            episode_number=8,
            main_theme="The power of vulnerability and male friendship",
            runtime_minutes=29,
            season=1,
            synopsis="Ted creates a support group for the coaching staff while Rebecca faces a difficult decision about her future.",
            ted_wisdom="There's two buttons I never like to hit: that's panic and snooze.",
            title="The Diamond Dogs",
            writer="Jason Sudeikis, Brendan Hunt, Joe Kelly",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode = await response.parse()
            assert_matches_type(Episode, episode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBelieve) -> None:
        episode = await async_client.episodes.retrieve(
            "episode_id",
        )
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBelieve) -> None:
        response = await async_client.episodes.with_raw_response.retrieve(
            "episode_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode = await response.parse()
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBelieve) -> None:
        async with async_client.episodes.with_streaming_response.retrieve(
            "episode_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode = await response.parse()
            assert_matches_type(Episode, episode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `episode_id` but received ''"):
            await async_client.episodes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBelieve) -> None:
        episode = await async_client.episodes.update(
            episode_id="episode_id",
        )
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBelieve) -> None:
        episode = await async_client.episodes.update(
            episode_id="episode_id",
            air_date=parse_date("2019-12-27"),
            biscuits_with_boss_moment="biscuits_with_boss_moment",
            character_focus=["string"],
            director="director",
            episode_number=1,
            main_theme="main_theme",
            memorable_moments=["string"],
            runtime_minutes=20,
            season=1,
            synopsis="synopsis",
            ted_wisdom="ted_wisdom",
            title="x",
            us_viewers_millions=0,
            viewer_rating=0,
            writer="writer",
        )
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBelieve) -> None:
        response = await async_client.episodes.with_raw_response.update(
            episode_id="episode_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode = await response.parse()
        assert_matches_type(Episode, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBelieve) -> None:
        async with async_client.episodes.with_streaming_response.update(
            episode_id="episode_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode = await response.parse()
            assert_matches_type(Episode, episode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `episode_id` but received ''"):
            await async_client.episodes.with_raw_response.update(
                episode_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBelieve) -> None:
        episode = await async_client.episodes.list()
        assert_matches_type(AsyncSkipLimitPage[Episode], episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBelieve) -> None:
        episode = await async_client.episodes.list(
            character_focus="character_focus",
            limit=10,
            season=1,
            skip=0,
        )
        assert_matches_type(AsyncSkipLimitPage[Episode], episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBelieve) -> None:
        response = await async_client.episodes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode = await response.parse()
        assert_matches_type(AsyncSkipLimitPage[Episode], episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBelieve) -> None:
        async with async_client.episodes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode = await response.parse()
            assert_matches_type(AsyncSkipLimitPage[Episode], episode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBelieve) -> None:
        episode = await async_client.episodes.delete(
            "episode_id",
        )
        assert episode is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBelieve) -> None:
        response = await async_client.episodes.with_raw_response.delete(
            "episode_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode = await response.parse()
        assert episode is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBelieve) -> None:
        async with async_client.episodes.with_streaming_response.delete(
            "episode_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode = await response.parse()
            assert episode is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `episode_id` but received ''"):
            await async_client.episodes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_wisdom(self, async_client: AsyncBelieve) -> None:
        episode = await async_client.episodes.get_wisdom(
            "episode_id",
        )
        assert_matches_type(EpisodeGetWisdomResponse, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_wisdom(self, async_client: AsyncBelieve) -> None:
        response = await async_client.episodes.with_raw_response.get_wisdom(
            "episode_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode = await response.parse()
        assert_matches_type(EpisodeGetWisdomResponse, episode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_wisdom(self, async_client: AsyncBelieve) -> None:
        async with async_client.episodes.with_streaming_response.get_wisdom(
            "episode_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode = await response.parse()
            assert_matches_type(EpisodeGetWisdomResponse, episode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_wisdom(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `episode_id` but received ''"):
            await async_client.episodes.with_raw_response.get_wisdom(
                "",
            )
