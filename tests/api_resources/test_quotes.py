# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from believe import Believe, AsyncBelieve
from tests.utils import assert_matches_type
from believe.types import (
    Quote,
)
from believe.pagination import SyncSkipLimitPage, AsyncSkipLimitPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Believe) -> None:
        quote = client.quotes.create(
            character_id="ted-lasso",
            context="Ted's first team meeting, revealing his coaching philosophy",
            moment_type="locker_room",
            text="I believe in believe.",
            theme="belief",
        )
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Believe) -> None:
        quote = client.quotes.create(
            character_id="ted-lasso",
            context="Ted's first team meeting, revealing his coaching philosophy",
            moment_type="locker_room",
            text="I believe in believe.",
            theme="belief",
            episode_id="s01e01",
            is_funny=False,
            is_inspirational=True,
            popularity_score=98.5,
            secondary_themes=["leadership", "teamwork"],
            times_shared=250000,
        )
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Believe) -> None:
        response = client.quotes.with_raw_response.create(
            character_id="ted-lasso",
            context="Ted's first team meeting, revealing his coaching philosophy",
            moment_type="locker_room",
            text="I believe in believe.",
            theme="belief",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Believe) -> None:
        with client.quotes.with_streaming_response.create(
            character_id="ted-lasso",
            context="Ted's first team meeting, revealing his coaching philosophy",
            moment_type="locker_room",
            text="I believe in believe.",
            theme="belief",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(Quote, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Believe) -> None:
        quote = client.quotes.retrieve(
            "quote_id",
        )
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Believe) -> None:
        response = client.quotes.with_raw_response.retrieve(
            "quote_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Believe) -> None:
        with client.quotes.with_streaming_response.retrieve(
            "quote_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(Quote, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `quote_id` but received ''"):
            client.quotes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Believe) -> None:
        quote = client.quotes.update(
            quote_id="quote_id",
        )
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Believe) -> None:
        quote = client.quotes.update(
            quote_id="quote_id",
            character_id="character_id",
            context="context",
            episode_id="episode_id",
            is_funny=True,
            is_inspirational=True,
            moment_type="halftime_speech",
            popularity_score=0,
            secondary_themes=["belief"],
            text="x",
            theme="belief",
            times_shared=0,
        )
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Believe) -> None:
        response = client.quotes.with_raw_response.update(
            quote_id="quote_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Believe) -> None:
        with client.quotes.with_streaming_response.update(
            quote_id="quote_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(Quote, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `quote_id` but received ''"):
            client.quotes.with_raw_response.update(
                quote_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Believe) -> None:
        quote = client.quotes.list()
        assert_matches_type(SyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Believe) -> None:
        quote = client.quotes.list(
            character_id="character_id",
            funny=True,
            inspirational=True,
            limit=10,
            moment_type="halftime_speech",
            skip=0,
            theme="belief",
        )
        assert_matches_type(SyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Believe) -> None:
        response = client.quotes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(SyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Believe) -> None:
        with client.quotes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(SyncSkipLimitPage[Quote], quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Believe) -> None:
        quote = client.quotes.delete(
            "quote_id",
        )
        assert quote is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Believe) -> None:
        response = client.quotes.with_raw_response.delete(
            "quote_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert quote is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Believe) -> None:
        with client.quotes.with_streaming_response.delete(
            "quote_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert quote is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `quote_id` but received ''"):
            client.quotes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_random(self, client: Believe) -> None:
        quote = client.quotes.get_random()
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_random_with_all_params(self, client: Believe) -> None:
        quote = client.quotes.get_random(
            character_id="character_id",
            inspirational=True,
            theme="belief",
        )
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_random(self, client: Believe) -> None:
        response = client.quotes.with_raw_response.get_random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_random(self, client: Believe) -> None:
        with client.quotes.with_streaming_response.get_random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(Quote, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_character(self, client: Believe) -> None:
        quote = client.quotes.list_by_character(
            character_id="character_id",
        )
        assert_matches_type(SyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_character_with_all_params(self, client: Believe) -> None:
        quote = client.quotes.list_by_character(
            character_id="character_id",
            limit=10,
            skip=0,
        )
        assert_matches_type(SyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_by_character(self, client: Believe) -> None:
        response = client.quotes.with_raw_response.list_by_character(
            character_id="character_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(SyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_by_character(self, client: Believe) -> None:
        with client.quotes.with_streaming_response.list_by_character(
            character_id="character_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(SyncSkipLimitPage[Quote], quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_by_character(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `character_id` but received ''"):
            client.quotes.with_raw_response.list_by_character(
                character_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_theme(self, client: Believe) -> None:
        quote = client.quotes.list_by_theme(
            theme="belief",
        )
        assert_matches_type(SyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_theme_with_all_params(self, client: Believe) -> None:
        quote = client.quotes.list_by_theme(
            theme="belief",
            limit=10,
            skip=0,
        )
        assert_matches_type(SyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_by_theme(self, client: Believe) -> None:
        response = client.quotes.with_raw_response.list_by_theme(
            theme="belief",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(SyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_by_theme(self, client: Believe) -> None:
        with client.quotes.with_streaming_response.list_by_theme(
            theme="belief",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(SyncSkipLimitPage[Quote], quote, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQuotes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBelieve) -> None:
        quote = await async_client.quotes.create(
            character_id="ted-lasso",
            context="Ted's first team meeting, revealing his coaching philosophy",
            moment_type="locker_room",
            text="I believe in believe.",
            theme="belief",
        )
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBelieve) -> None:
        quote = await async_client.quotes.create(
            character_id="ted-lasso",
            context="Ted's first team meeting, revealing his coaching philosophy",
            moment_type="locker_room",
            text="I believe in believe.",
            theme="belief",
            episode_id="s01e01",
            is_funny=False,
            is_inspirational=True,
            popularity_score=98.5,
            secondary_themes=["leadership", "teamwork"],
            times_shared=250000,
        )
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBelieve) -> None:
        response = await async_client.quotes.with_raw_response.create(
            character_id="ted-lasso",
            context="Ted's first team meeting, revealing his coaching philosophy",
            moment_type="locker_room",
            text="I believe in believe.",
            theme="belief",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBelieve) -> None:
        async with async_client.quotes.with_streaming_response.create(
            character_id="ted-lasso",
            context="Ted's first team meeting, revealing his coaching philosophy",
            moment_type="locker_room",
            text="I believe in believe.",
            theme="belief",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(Quote, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBelieve) -> None:
        quote = await async_client.quotes.retrieve(
            "quote_id",
        )
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBelieve) -> None:
        response = await async_client.quotes.with_raw_response.retrieve(
            "quote_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBelieve) -> None:
        async with async_client.quotes.with_streaming_response.retrieve(
            "quote_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(Quote, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `quote_id` but received ''"):
            await async_client.quotes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBelieve) -> None:
        quote = await async_client.quotes.update(
            quote_id="quote_id",
        )
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBelieve) -> None:
        quote = await async_client.quotes.update(
            quote_id="quote_id",
            character_id="character_id",
            context="context",
            episode_id="episode_id",
            is_funny=True,
            is_inspirational=True,
            moment_type="halftime_speech",
            popularity_score=0,
            secondary_themes=["belief"],
            text="x",
            theme="belief",
            times_shared=0,
        )
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBelieve) -> None:
        response = await async_client.quotes.with_raw_response.update(
            quote_id="quote_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBelieve) -> None:
        async with async_client.quotes.with_streaming_response.update(
            quote_id="quote_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(Quote, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `quote_id` but received ''"):
            await async_client.quotes.with_raw_response.update(
                quote_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBelieve) -> None:
        quote = await async_client.quotes.list()
        assert_matches_type(AsyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBelieve) -> None:
        quote = await async_client.quotes.list(
            character_id="character_id",
            funny=True,
            inspirational=True,
            limit=10,
            moment_type="halftime_speech",
            skip=0,
            theme="belief",
        )
        assert_matches_type(AsyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBelieve) -> None:
        response = await async_client.quotes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(AsyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBelieve) -> None:
        async with async_client.quotes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(AsyncSkipLimitPage[Quote], quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBelieve) -> None:
        quote = await async_client.quotes.delete(
            "quote_id",
        )
        assert quote is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBelieve) -> None:
        response = await async_client.quotes.with_raw_response.delete(
            "quote_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert quote is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBelieve) -> None:
        async with async_client.quotes.with_streaming_response.delete(
            "quote_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert quote is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `quote_id` but received ''"):
            await async_client.quotes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_random(self, async_client: AsyncBelieve) -> None:
        quote = await async_client.quotes.get_random()
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_random_with_all_params(self, async_client: AsyncBelieve) -> None:
        quote = await async_client.quotes.get_random(
            character_id="character_id",
            inspirational=True,
            theme="belief",
        )
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_random(self, async_client: AsyncBelieve) -> None:
        response = await async_client.quotes.with_raw_response.get_random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(Quote, quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_random(self, async_client: AsyncBelieve) -> None:
        async with async_client.quotes.with_streaming_response.get_random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(Quote, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_character(self, async_client: AsyncBelieve) -> None:
        quote = await async_client.quotes.list_by_character(
            character_id="character_id",
        )
        assert_matches_type(AsyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_character_with_all_params(self, async_client: AsyncBelieve) -> None:
        quote = await async_client.quotes.list_by_character(
            character_id="character_id",
            limit=10,
            skip=0,
        )
        assert_matches_type(AsyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_by_character(self, async_client: AsyncBelieve) -> None:
        response = await async_client.quotes.with_raw_response.list_by_character(
            character_id="character_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(AsyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_by_character(self, async_client: AsyncBelieve) -> None:
        async with async_client.quotes.with_streaming_response.list_by_character(
            character_id="character_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(AsyncSkipLimitPage[Quote], quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_by_character(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `character_id` but received ''"):
            await async_client.quotes.with_raw_response.list_by_character(
                character_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_theme(self, async_client: AsyncBelieve) -> None:
        quote = await async_client.quotes.list_by_theme(
            theme="belief",
        )
        assert_matches_type(AsyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_theme_with_all_params(self, async_client: AsyncBelieve) -> None:
        quote = await async_client.quotes.list_by_theme(
            theme="belief",
            limit=10,
            skip=0,
        )
        assert_matches_type(AsyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_by_theme(self, async_client: AsyncBelieve) -> None:
        response = await async_client.quotes.with_raw_response.list_by_theme(
            theme="belief",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(AsyncSkipLimitPage[Quote], quote, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_by_theme(self, async_client: AsyncBelieve) -> None:
        async with async_client.quotes.with_streaming_response.list_by_theme(
            theme="belief",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(AsyncSkipLimitPage[Quote], quote, path=["response"])

        assert cast(Any, response.is_closed) is True
