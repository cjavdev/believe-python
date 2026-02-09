# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from believe import Believe, AsyncBelieve
from tests.utils import assert_matches_type
from believe.types import ConflictResolveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConflicts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resolve(self, client: Believe) -> None:
        conflict = client.conflicts.resolve(
            conflict_type="interpersonal",
            description="Alex keeps taking credit for my ideas in meetings and I'm getting resentful.",
            parties_involved=["Me", "My teammate Alex"],
        )
        assert_matches_type(ConflictResolveResponse, conflict, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resolve_with_all_params(self, client: Believe) -> None:
        conflict = client.conflicts.resolve(
            conflict_type="interpersonal",
            description="Alex keeps taking credit for my ideas in meetings and I'm getting resentful.",
            parties_involved=["Me", "My teammate Alex"],
            attempts_made=["Mentioned it casually", "Avoided them"],
        )
        assert_matches_type(ConflictResolveResponse, conflict, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resolve(self, client: Believe) -> None:
        response = client.conflicts.with_raw_response.resolve(
            conflict_type="interpersonal",
            description="Alex keeps taking credit for my ideas in meetings and I'm getting resentful.",
            parties_involved=["Me", "My teammate Alex"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conflict = response.parse()
        assert_matches_type(ConflictResolveResponse, conflict, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resolve(self, client: Believe) -> None:
        with client.conflicts.with_streaming_response.resolve(
            conflict_type="interpersonal",
            description="Alex keeps taking credit for my ideas in meetings and I'm getting resentful.",
            parties_involved=["Me", "My teammate Alex"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conflict = response.parse()
            assert_matches_type(ConflictResolveResponse, conflict, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConflicts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resolve(self, async_client: AsyncBelieve) -> None:
        conflict = await async_client.conflicts.resolve(
            conflict_type="interpersonal",
            description="Alex keeps taking credit for my ideas in meetings and I'm getting resentful.",
            parties_involved=["Me", "My teammate Alex"],
        )
        assert_matches_type(ConflictResolveResponse, conflict, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resolve_with_all_params(self, async_client: AsyncBelieve) -> None:
        conflict = await async_client.conflicts.resolve(
            conflict_type="interpersonal",
            description="Alex keeps taking credit for my ideas in meetings and I'm getting resentful.",
            parties_involved=["Me", "My teammate Alex"],
            attempts_made=["Mentioned it casually", "Avoided them"],
        )
        assert_matches_type(ConflictResolveResponse, conflict, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resolve(self, async_client: AsyncBelieve) -> None:
        response = await async_client.conflicts.with_raw_response.resolve(
            conflict_type="interpersonal",
            description="Alex keeps taking credit for my ideas in meetings and I'm getting resentful.",
            parties_involved=["Me", "My teammate Alex"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conflict = await response.parse()
        assert_matches_type(ConflictResolveResponse, conflict, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resolve(self, async_client: AsyncBelieve) -> None:
        async with async_client.conflicts.with_streaming_response.resolve(
            conflict_type="interpersonal",
            description="Alex keeps taking credit for my ideas in meetings and I'm getting resentful.",
            parties_involved=["Me", "My teammate Alex"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conflict = await response.parse()
            assert_matches_type(ConflictResolveResponse, conflict, path=["response"])

        assert cast(Any, response.is_closed) is True
