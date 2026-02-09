# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from believe import Believe, AsyncBelieve
from tests.utils import assert_matches_type
from believe.types import Biscuit
from believe.pagination import SyncSkipLimitPage, AsyncSkipLimitPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBiscuits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Believe) -> None:
        biscuit = client.biscuits.retrieve(
            "biscuit_id",
        )
        assert_matches_type(Biscuit, biscuit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Believe) -> None:
        response = client.biscuits.with_raw_response.retrieve(
            "biscuit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        biscuit = response.parse()
        assert_matches_type(Biscuit, biscuit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Believe) -> None:
        with client.biscuits.with_streaming_response.retrieve(
            "biscuit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            biscuit = response.parse()
            assert_matches_type(Biscuit, biscuit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `biscuit_id` but received ''"):
            client.biscuits.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Believe) -> None:
        biscuit = client.biscuits.list()
        assert_matches_type(SyncSkipLimitPage[Biscuit], biscuit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Believe) -> None:
        biscuit = client.biscuits.list(
            limit=10,
            skip=0,
        )
        assert_matches_type(SyncSkipLimitPage[Biscuit], biscuit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Believe) -> None:
        response = client.biscuits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        biscuit = response.parse()
        assert_matches_type(SyncSkipLimitPage[Biscuit], biscuit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Believe) -> None:
        with client.biscuits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            biscuit = response.parse()
            assert_matches_type(SyncSkipLimitPage[Biscuit], biscuit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_fresh(self, client: Believe) -> None:
        biscuit = client.biscuits.get_fresh()
        assert_matches_type(Biscuit, biscuit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_fresh(self, client: Believe) -> None:
        response = client.biscuits.with_raw_response.get_fresh()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        biscuit = response.parse()
        assert_matches_type(Biscuit, biscuit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_fresh(self, client: Believe) -> None:
        with client.biscuits.with_streaming_response.get_fresh() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            biscuit = response.parse()
            assert_matches_type(Biscuit, biscuit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBiscuits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBelieve) -> None:
        biscuit = await async_client.biscuits.retrieve(
            "biscuit_id",
        )
        assert_matches_type(Biscuit, biscuit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBelieve) -> None:
        response = await async_client.biscuits.with_raw_response.retrieve(
            "biscuit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        biscuit = await response.parse()
        assert_matches_type(Biscuit, biscuit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBelieve) -> None:
        async with async_client.biscuits.with_streaming_response.retrieve(
            "biscuit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            biscuit = await response.parse()
            assert_matches_type(Biscuit, biscuit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `biscuit_id` but received ''"):
            await async_client.biscuits.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBelieve) -> None:
        biscuit = await async_client.biscuits.list()
        assert_matches_type(AsyncSkipLimitPage[Biscuit], biscuit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBelieve) -> None:
        biscuit = await async_client.biscuits.list(
            limit=10,
            skip=0,
        )
        assert_matches_type(AsyncSkipLimitPage[Biscuit], biscuit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBelieve) -> None:
        response = await async_client.biscuits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        biscuit = await response.parse()
        assert_matches_type(AsyncSkipLimitPage[Biscuit], biscuit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBelieve) -> None:
        async with async_client.biscuits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            biscuit = await response.parse()
            assert_matches_type(AsyncSkipLimitPage[Biscuit], biscuit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_fresh(self, async_client: AsyncBelieve) -> None:
        biscuit = await async_client.biscuits.get_fresh()
        assert_matches_type(Biscuit, biscuit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_fresh(self, async_client: AsyncBelieve) -> None:
        response = await async_client.biscuits.with_raw_response.get_fresh()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        biscuit = await response.parse()
        assert_matches_type(Biscuit, biscuit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_fresh(self, async_client: AsyncBelieve) -> None:
        async with async_client.biscuits.with_streaming_response.get_fresh() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            biscuit = await response.parse()
            assert_matches_type(Biscuit, biscuit, path=["response"])

        assert cast(Any, response.is_closed) is True
