# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from believe import Believe, AsyncBelieve
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommentary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream(self, client: Believe) -> None:
        commentary = client.matches.commentary.stream(
            "match_id",
        )
        assert_matches_type(object, commentary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream(self, client: Believe) -> None:
        response = client.matches.commentary.with_raw_response.stream(
            "match_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commentary = response.parse()
        assert_matches_type(object, commentary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream(self, client: Believe) -> None:
        with client.matches.commentary.with_streaming_response.stream(
            "match_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commentary = response.parse()
            assert_matches_type(object, commentary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stream(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `match_id` but received ''"):
            client.matches.commentary.with_raw_response.stream(
                "",
            )


class TestAsyncCommentary:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream(self, async_client: AsyncBelieve) -> None:
        commentary = await async_client.matches.commentary.stream(
            "match_id",
        )
        assert_matches_type(object, commentary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncBelieve) -> None:
        response = await async_client.matches.commentary.with_raw_response.stream(
            "match_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commentary = await response.parse()
        assert_matches_type(object, commentary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncBelieve) -> None:
        async with async_client.matches.commentary.with_streaming_response.stream(
            "match_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commentary = await response.parse()
            assert_matches_type(object, commentary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stream(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `match_id` but received ''"):
            await async_client.matches.commentary.with_raw_response.stream(
                "",
            )
