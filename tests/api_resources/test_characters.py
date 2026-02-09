# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from believe import Believe, AsyncBelieve
from tests.utils import assert_matches_type
from believe.types import (
    Character,
    CharacterGetQuotesResponse,
)
from believe._utils import parse_date
from believe.pagination import SyncSkipLimitPage, AsyncSkipLimitPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCharacters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Believe) -> None:
        character = client.characters.create(
            background="Legendary midfielder for Chelsea and AFC Richmond, now assistant coach. Known for his gruff exterior hiding a heart of gold.",
            emotional_stats={
                "curiosity": 40,
                "empathy": 85,
                "optimism": 45,
                "resilience": 95,
                "vulnerability": 60,
            },
            name="Roy Kent",
            personality_traits=["intense", "loyal", "secretly caring", "profane"],
            role="coach",
        )
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Believe) -> None:
        character = client.characters.create(
            background="Legendary midfielder for Chelsea and AFC Richmond, now assistant coach. Known for his gruff exterior hiding a heart of gold.",
            emotional_stats={
                "curiosity": 40,
                "empathy": 85,
                "optimism": 45,
                "resilience": 95,
                "vulnerability": 60,
            },
            name="Roy Kent",
            personality_traits=["intense", "loyal", "secretly caring", "profane"],
            role="coach",
            date_of_birth=parse_date("1977-03-15"),
            email="roy.kent@afcrichmond.com",
            growth_arcs=[
                {
                    "breakthrough": "Finding purpose beyond playing",
                    "challenge": "Accepting his body's limitations",
                    "ending_point": "Retired but lost",
                    "season": 1,
                    "starting_point": "Aging footballer facing retirement",
                }
            ],
            height_meters=1.78,
            profile_image_url="https://afcrichmond.com/images/roy-kent.jpg",
            salary_gbp="175000.00",
            signature_quotes=["He's here, he's there, he's every-f***ing-where, Roy Kent!", "Whistle!"],
            team_id="afc-richmond",
        )
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Believe) -> None:
        response = client.characters.with_raw_response.create(
            background="Legendary midfielder for Chelsea and AFC Richmond, now assistant coach. Known for his gruff exterior hiding a heart of gold.",
            emotional_stats={
                "curiosity": 40,
                "empathy": 85,
                "optimism": 45,
                "resilience": 95,
                "vulnerability": 60,
            },
            name="Roy Kent",
            personality_traits=["intense", "loyal", "secretly caring", "profane"],
            role="coach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character = response.parse()
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Believe) -> None:
        with client.characters.with_streaming_response.create(
            background="Legendary midfielder for Chelsea and AFC Richmond, now assistant coach. Known for his gruff exterior hiding a heart of gold.",
            emotional_stats={
                "curiosity": 40,
                "empathy": 85,
                "optimism": 45,
                "resilience": 95,
                "vulnerability": 60,
            },
            name="Roy Kent",
            personality_traits=["intense", "loyal", "secretly caring", "profane"],
            role="coach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character = response.parse()
            assert_matches_type(Character, character, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Believe) -> None:
        character = client.characters.retrieve(
            "character_id",
        )
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Believe) -> None:
        response = client.characters.with_raw_response.retrieve(
            "character_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character = response.parse()
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Believe) -> None:
        with client.characters.with_streaming_response.retrieve(
            "character_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character = response.parse()
            assert_matches_type(Character, character, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `character_id` but received ''"):
            client.characters.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Believe) -> None:
        character = client.characters.update(
            character_id="character_id",
        )
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Believe) -> None:
        character = client.characters.update(
            character_id="character_id",
            background="background",
            date_of_birth=parse_date("2019-12-27"),
            email="dev@stainless.com",
            emotional_stats={
                "curiosity": 99,
                "empathy": 100,
                "optimism": 95,
                "resilience": 90,
                "vulnerability": 80,
            },
            growth_arcs=[
                {
                    "breakthrough": "breakthrough",
                    "challenge": "challenge",
                    "ending_point": "ending_point",
                    "season": 1,
                    "starting_point": "starting_point",
                }
            ],
            height_meters=1,
            name="x",
            personality_traits=["string"],
            profile_image_url="https://example.com",
            role="coach",
            salary_gbp=0,
            signature_quotes=["string"],
            team_id="team_id",
        )
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Believe) -> None:
        response = client.characters.with_raw_response.update(
            character_id="character_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character = response.parse()
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Believe) -> None:
        with client.characters.with_streaming_response.update(
            character_id="character_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character = response.parse()
            assert_matches_type(Character, character, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `character_id` but received ''"):
            client.characters.with_raw_response.update(
                character_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Believe) -> None:
        character = client.characters.list()
        assert_matches_type(SyncSkipLimitPage[Character], character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Believe) -> None:
        character = client.characters.list(
            limit=10,
            min_optimism=0,
            role="coach",
            skip=0,
            team_id="team_id",
        )
        assert_matches_type(SyncSkipLimitPage[Character], character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Believe) -> None:
        response = client.characters.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character = response.parse()
        assert_matches_type(SyncSkipLimitPage[Character], character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Believe) -> None:
        with client.characters.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character = response.parse()
            assert_matches_type(SyncSkipLimitPage[Character], character, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Believe) -> None:
        character = client.characters.delete(
            "character_id",
        )
        assert character is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Believe) -> None:
        response = client.characters.with_raw_response.delete(
            "character_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character = response.parse()
        assert character is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Believe) -> None:
        with client.characters.with_streaming_response.delete(
            "character_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character = response.parse()
            assert character is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `character_id` but received ''"):
            client.characters.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_quotes(self, client: Believe) -> None:
        character = client.characters.get_quotes(
            "character_id",
        )
        assert_matches_type(CharacterGetQuotesResponse, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_quotes(self, client: Believe) -> None:
        response = client.characters.with_raw_response.get_quotes(
            "character_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character = response.parse()
        assert_matches_type(CharacterGetQuotesResponse, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_quotes(self, client: Believe) -> None:
        with client.characters.with_streaming_response.get_quotes(
            "character_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character = response.parse()
            assert_matches_type(CharacterGetQuotesResponse, character, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_quotes(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `character_id` but received ''"):
            client.characters.with_raw_response.get_quotes(
                "",
            )


class TestAsyncCharacters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBelieve) -> None:
        character = await async_client.characters.create(
            background="Legendary midfielder for Chelsea and AFC Richmond, now assistant coach. Known for his gruff exterior hiding a heart of gold.",
            emotional_stats={
                "curiosity": 40,
                "empathy": 85,
                "optimism": 45,
                "resilience": 95,
                "vulnerability": 60,
            },
            name="Roy Kent",
            personality_traits=["intense", "loyal", "secretly caring", "profane"],
            role="coach",
        )
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBelieve) -> None:
        character = await async_client.characters.create(
            background="Legendary midfielder for Chelsea and AFC Richmond, now assistant coach. Known for his gruff exterior hiding a heart of gold.",
            emotional_stats={
                "curiosity": 40,
                "empathy": 85,
                "optimism": 45,
                "resilience": 95,
                "vulnerability": 60,
            },
            name="Roy Kent",
            personality_traits=["intense", "loyal", "secretly caring", "profane"],
            role="coach",
            date_of_birth=parse_date("1977-03-15"),
            email="roy.kent@afcrichmond.com",
            growth_arcs=[
                {
                    "breakthrough": "Finding purpose beyond playing",
                    "challenge": "Accepting his body's limitations",
                    "ending_point": "Retired but lost",
                    "season": 1,
                    "starting_point": "Aging footballer facing retirement",
                }
            ],
            height_meters=1.78,
            profile_image_url="https://afcrichmond.com/images/roy-kent.jpg",
            salary_gbp="175000.00",
            signature_quotes=["He's here, he's there, he's every-f***ing-where, Roy Kent!", "Whistle!"],
            team_id="afc-richmond",
        )
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBelieve) -> None:
        response = await async_client.characters.with_raw_response.create(
            background="Legendary midfielder for Chelsea and AFC Richmond, now assistant coach. Known for his gruff exterior hiding a heart of gold.",
            emotional_stats={
                "curiosity": 40,
                "empathy": 85,
                "optimism": 45,
                "resilience": 95,
                "vulnerability": 60,
            },
            name="Roy Kent",
            personality_traits=["intense", "loyal", "secretly caring", "profane"],
            role="coach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character = await response.parse()
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBelieve) -> None:
        async with async_client.characters.with_streaming_response.create(
            background="Legendary midfielder for Chelsea and AFC Richmond, now assistant coach. Known for his gruff exterior hiding a heart of gold.",
            emotional_stats={
                "curiosity": 40,
                "empathy": 85,
                "optimism": 45,
                "resilience": 95,
                "vulnerability": 60,
            },
            name="Roy Kent",
            personality_traits=["intense", "loyal", "secretly caring", "profane"],
            role="coach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character = await response.parse()
            assert_matches_type(Character, character, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBelieve) -> None:
        character = await async_client.characters.retrieve(
            "character_id",
        )
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBelieve) -> None:
        response = await async_client.characters.with_raw_response.retrieve(
            "character_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character = await response.parse()
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBelieve) -> None:
        async with async_client.characters.with_streaming_response.retrieve(
            "character_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character = await response.parse()
            assert_matches_type(Character, character, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `character_id` but received ''"):
            await async_client.characters.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBelieve) -> None:
        character = await async_client.characters.update(
            character_id="character_id",
        )
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBelieve) -> None:
        character = await async_client.characters.update(
            character_id="character_id",
            background="background",
            date_of_birth=parse_date("2019-12-27"),
            email="dev@stainless.com",
            emotional_stats={
                "curiosity": 99,
                "empathy": 100,
                "optimism": 95,
                "resilience": 90,
                "vulnerability": 80,
            },
            growth_arcs=[
                {
                    "breakthrough": "breakthrough",
                    "challenge": "challenge",
                    "ending_point": "ending_point",
                    "season": 1,
                    "starting_point": "starting_point",
                }
            ],
            height_meters=1,
            name="x",
            personality_traits=["string"],
            profile_image_url="https://example.com",
            role="coach",
            salary_gbp=0,
            signature_quotes=["string"],
            team_id="team_id",
        )
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBelieve) -> None:
        response = await async_client.characters.with_raw_response.update(
            character_id="character_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character = await response.parse()
        assert_matches_type(Character, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBelieve) -> None:
        async with async_client.characters.with_streaming_response.update(
            character_id="character_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character = await response.parse()
            assert_matches_type(Character, character, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `character_id` but received ''"):
            await async_client.characters.with_raw_response.update(
                character_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBelieve) -> None:
        character = await async_client.characters.list()
        assert_matches_type(AsyncSkipLimitPage[Character], character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBelieve) -> None:
        character = await async_client.characters.list(
            limit=10,
            min_optimism=0,
            role="coach",
            skip=0,
            team_id="team_id",
        )
        assert_matches_type(AsyncSkipLimitPage[Character], character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBelieve) -> None:
        response = await async_client.characters.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character = await response.parse()
        assert_matches_type(AsyncSkipLimitPage[Character], character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBelieve) -> None:
        async with async_client.characters.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character = await response.parse()
            assert_matches_type(AsyncSkipLimitPage[Character], character, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBelieve) -> None:
        character = await async_client.characters.delete(
            "character_id",
        )
        assert character is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBelieve) -> None:
        response = await async_client.characters.with_raw_response.delete(
            "character_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character = await response.parse()
        assert character is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBelieve) -> None:
        async with async_client.characters.with_streaming_response.delete(
            "character_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character = await response.parse()
            assert character is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `character_id` but received ''"):
            await async_client.characters.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_quotes(self, async_client: AsyncBelieve) -> None:
        character = await async_client.characters.get_quotes(
            "character_id",
        )
        assert_matches_type(CharacterGetQuotesResponse, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_quotes(self, async_client: AsyncBelieve) -> None:
        response = await async_client.characters.with_raw_response.get_quotes(
            "character_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character = await response.parse()
        assert_matches_type(CharacterGetQuotesResponse, character, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_quotes(self, async_client: AsyncBelieve) -> None:
        async with async_client.characters.with_streaming_response.get_quotes(
            "character_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character = await response.parse()
            assert_matches_type(CharacterGetQuotesResponse, character, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_quotes(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `character_id` but received ''"):
            await async_client.characters.with_raw_response.get_quotes(
                "",
            )
