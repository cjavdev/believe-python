# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from believe import Believe, AsyncBelieve
from tests.utils import assert_matches_type
from believe.types import PressSimulateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPress:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_simulate(self, client: Believe) -> None:
        press = client.press.simulate(
            question="Ted, your team just lost 5-0. How do you explain this embarrassing defeat?",
        )
        assert_matches_type(PressSimulateResponse, press, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_simulate_with_all_params(self, client: Believe) -> None:
        press = client.press.simulate(
            question="Ted, your team just lost 5-0. How do you explain this embarrassing defeat?",
            hostile=True,
            topic="match_result",
        )
        assert_matches_type(PressSimulateResponse, press, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_simulate(self, client: Believe) -> None:
        response = client.press.with_raw_response.simulate(
            question="Ted, your team just lost 5-0. How do you explain this embarrassing defeat?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        press = response.parse()
        assert_matches_type(PressSimulateResponse, press, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_simulate(self, client: Believe) -> None:
        with client.press.with_streaming_response.simulate(
            question="Ted, your team just lost 5-0. How do you explain this embarrassing defeat?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            press = response.parse()
            assert_matches_type(PressSimulateResponse, press, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPress:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_simulate(self, async_client: AsyncBelieve) -> None:
        press = await async_client.press.simulate(
            question="Ted, your team just lost 5-0. How do you explain this embarrassing defeat?",
        )
        assert_matches_type(PressSimulateResponse, press, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_simulate_with_all_params(self, async_client: AsyncBelieve) -> None:
        press = await async_client.press.simulate(
            question="Ted, your team just lost 5-0. How do you explain this embarrassing defeat?",
            hostile=True,
            topic="match_result",
        )
        assert_matches_type(PressSimulateResponse, press, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_simulate(self, async_client: AsyncBelieve) -> None:
        response = await async_client.press.with_raw_response.simulate(
            question="Ted, your team just lost 5-0. How do you explain this embarrassing defeat?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        press = await response.parse()
        assert_matches_type(PressSimulateResponse, press, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_simulate(self, async_client: AsyncBelieve) -> None:
        async with async_client.press.with_streaming_response.simulate(
            question="Ted, your team just lost 5-0. How do you explain this embarrassing defeat?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            press = await response.parse()
            assert_matches_type(PressSimulateResponse, press, path=["response"])

        assert cast(Any, response.is_closed) is True
