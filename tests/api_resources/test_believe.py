# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from believe import Believe, AsyncBelieve
from tests.utils import assert_matches_type
from believe.types import BelieveSubmitResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBelieve:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: Believe) -> None:
        believe = client.believe.submit(
            situation="I just got passed over for a promotion I've been working toward for two years.",
            situation_type="work_challenge",
        )
        assert_matches_type(BelieveSubmitResponse, believe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_with_all_params(self, client: Believe) -> None:
        believe = client.believe.submit(
            situation="I just got passed over for a promotion I've been working toward for two years.",
            situation_type="work_challenge",
            context="I've always tried to be a team player and support my colleagues.",
            intensity=7,
        )
        assert_matches_type(BelieveSubmitResponse, believe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Believe) -> None:
        response = client.believe.with_raw_response.submit(
            situation="I just got passed over for a promotion I've been working toward for two years.",
            situation_type="work_challenge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        believe = response.parse()
        assert_matches_type(BelieveSubmitResponse, believe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Believe) -> None:
        with client.believe.with_streaming_response.submit(
            situation="I just got passed over for a promotion I've been working toward for two years.",
            situation_type="work_challenge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            believe = response.parse()
            assert_matches_type(BelieveSubmitResponse, believe, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBelieve:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncBelieve) -> None:
        believe = await async_client.believe.submit(
            situation="I just got passed over for a promotion I've been working toward for two years.",
            situation_type="work_challenge",
        )
        assert_matches_type(BelieveSubmitResponse, believe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncBelieve) -> None:
        believe = await async_client.believe.submit(
            situation="I just got passed over for a promotion I've been working toward for two years.",
            situation_type="work_challenge",
            context="I've always tried to be a team player and support my colleagues.",
            intensity=7,
        )
        assert_matches_type(BelieveSubmitResponse, believe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncBelieve) -> None:
        response = await async_client.believe.with_raw_response.submit(
            situation="I just got passed over for a promotion I've been working toward for two years.",
            situation_type="work_challenge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        believe = await response.parse()
        assert_matches_type(BelieveSubmitResponse, believe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncBelieve) -> None:
        async with async_client.believe.with_streaming_response.submit(
            situation="I just got passed over for a promotion I've been working toward for two years.",
            situation_type="work_challenge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            believe = await response.parse()
            assert_matches_type(BelieveSubmitResponse, believe, path=["response"])

        assert cast(Any, response.is_closed) is True
