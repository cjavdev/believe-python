# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from believe import Believe, AsyncBelieve
from tests.utils import assert_matches_type
from believe.pagination import SyncSkipLimitPage, AsyncSkipLimitPage
from believe.types.coaching import CoachingPrinciple

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrinciples:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Believe) -> None:
        principle = client.coaching.principles.retrieve(
            "principle_id",
        )
        assert_matches_type(CoachingPrinciple, principle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Believe) -> None:
        response = client.coaching.principles.with_raw_response.retrieve(
            "principle_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        principle = response.parse()
        assert_matches_type(CoachingPrinciple, principle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Believe) -> None:
        with client.coaching.principles.with_streaming_response.retrieve(
            "principle_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            principle = response.parse()
            assert_matches_type(CoachingPrinciple, principle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `principle_id` but received ''"):
            client.coaching.principles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Believe) -> None:
        principle = client.coaching.principles.list()
        assert_matches_type(SyncSkipLimitPage[CoachingPrinciple], principle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Believe) -> None:
        principle = client.coaching.principles.list(
            limit=10,
            skip=0,
        )
        assert_matches_type(SyncSkipLimitPage[CoachingPrinciple], principle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Believe) -> None:
        response = client.coaching.principles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        principle = response.parse()
        assert_matches_type(SyncSkipLimitPage[CoachingPrinciple], principle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Believe) -> None:
        with client.coaching.principles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            principle = response.parse()
            assert_matches_type(SyncSkipLimitPage[CoachingPrinciple], principle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_random(self, client: Believe) -> None:
        principle = client.coaching.principles.get_random()
        assert_matches_type(CoachingPrinciple, principle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_random(self, client: Believe) -> None:
        response = client.coaching.principles.with_raw_response.get_random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        principle = response.parse()
        assert_matches_type(CoachingPrinciple, principle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_random(self, client: Believe) -> None:
        with client.coaching.principles.with_streaming_response.get_random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            principle = response.parse()
            assert_matches_type(CoachingPrinciple, principle, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrinciples:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBelieve) -> None:
        principle = await async_client.coaching.principles.retrieve(
            "principle_id",
        )
        assert_matches_type(CoachingPrinciple, principle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBelieve) -> None:
        response = await async_client.coaching.principles.with_raw_response.retrieve(
            "principle_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        principle = await response.parse()
        assert_matches_type(CoachingPrinciple, principle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBelieve) -> None:
        async with async_client.coaching.principles.with_streaming_response.retrieve(
            "principle_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            principle = await response.parse()
            assert_matches_type(CoachingPrinciple, principle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `principle_id` but received ''"):
            await async_client.coaching.principles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBelieve) -> None:
        principle = await async_client.coaching.principles.list()
        assert_matches_type(AsyncSkipLimitPage[CoachingPrinciple], principle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBelieve) -> None:
        principle = await async_client.coaching.principles.list(
            limit=10,
            skip=0,
        )
        assert_matches_type(AsyncSkipLimitPage[CoachingPrinciple], principle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBelieve) -> None:
        response = await async_client.coaching.principles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        principle = await response.parse()
        assert_matches_type(AsyncSkipLimitPage[CoachingPrinciple], principle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBelieve) -> None:
        async with async_client.coaching.principles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            principle = await response.parse()
            assert_matches_type(AsyncSkipLimitPage[CoachingPrinciple], principle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_random(self, async_client: AsyncBelieve) -> None:
        principle = await async_client.coaching.principles.get_random()
        assert_matches_type(CoachingPrinciple, principle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_random(self, async_client: AsyncBelieve) -> None:
        response = await async_client.coaching.principles.with_raw_response.get_random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        principle = await response.parse()
        assert_matches_type(CoachingPrinciple, principle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_random(self, async_client: AsyncBelieve) -> None:
        async with async_client.coaching.principles.with_streaming_response.get_random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            principle = await response.parse()
            assert_matches_type(CoachingPrinciple, principle, path=["response"])

        assert cast(Any, response.is_closed) is True
