# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from believe import Believe, AsyncBelieve

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_test(self, client: Believe) -> None:
        w = client.client.ws.test()
        assert w is None

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_test(self, client: Believe) -> None:
        response = client.client.ws.with_raw_response.test()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        w = response.parse()
        assert w is None

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_test(self, client: Believe) -> None:
        with client.client.ws.with_streaming_response.test() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            w = response.parse()
            assert w is None

        assert cast(Any, response.is_closed) is True


class TestAsyncWs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_test(self, async_client: AsyncBelieve) -> None:
        w = await async_client.client.ws.test()
        assert w is None

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncBelieve) -> None:
        response = await async_client.client.ws.with_raw_response.test()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        w = await response.parse()
        assert w is None

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncBelieve) -> None:
        async with async_client.client.ws.with_streaming_response.test() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            w = await response.parse()
            assert w is None

        assert cast(Any, response.is_closed) is True
