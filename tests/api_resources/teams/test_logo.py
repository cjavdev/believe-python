# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from believe import Believe, AsyncBelieve
from tests.utils import assert_matches_type
from believe.types.teams import FileUpload

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Believe) -> None:
        logo = client.teams.logo.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="team_id",
        )
        assert logo is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Believe) -> None:
        response = client.teams.logo.with_raw_response.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logo = response.parse()
        assert logo is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Believe) -> None:
        with client.teams.logo.with_streaming_response.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logo = response.parse()
            assert logo is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.logo.with_raw_response.delete(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                team_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.teams.logo.with_raw_response.delete(
                file_id="",
                team_id="team_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_download(self, client: Believe) -> None:
        logo = client.teams.logo.download(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="team_id",
        )
        assert_matches_type(object, logo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_download(self, client: Believe) -> None:
        response = client.teams.logo.with_raw_response.download(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logo = response.parse()
        assert_matches_type(object, logo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_download(self, client: Believe) -> None:
        with client.teams.logo.with_streaming_response.download(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logo = response.parse()
            assert_matches_type(object, logo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_download(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.logo.with_raw_response.download(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                team_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.teams.logo.with_raw_response.download(
                file_id="",
                team_id="team_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: Believe) -> None:
        logo = client.teams.logo.upload(
            team_id="team_id",
            file=b"raw file contents",
        )
        assert_matches_type(FileUpload, logo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Believe) -> None:
        response = client.teams.logo.with_raw_response.upload(
            team_id="team_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logo = response.parse()
        assert_matches_type(FileUpload, logo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Believe) -> None:
        with client.teams.logo.with_streaming_response.upload(
            team_id="team_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logo = response.parse()
            assert_matches_type(FileUpload, logo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.logo.with_raw_response.upload(
                team_id="",
                file=b"raw file contents",
            )


class TestAsyncLogo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBelieve) -> None:
        logo = await async_client.teams.logo.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="team_id",
        )
        assert logo is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBelieve) -> None:
        response = await async_client.teams.logo.with_raw_response.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logo = await response.parse()
        assert logo is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBelieve) -> None:
        async with async_client.teams.logo.with_streaming_response.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logo = await response.parse()
            assert logo is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.logo.with_raw_response.delete(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                team_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.teams.logo.with_raw_response.delete(
                file_id="",
                team_id="team_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_download(self, async_client: AsyncBelieve) -> None:
        logo = await async_client.teams.logo.download(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="team_id",
        )
        assert_matches_type(object, logo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_download(self, async_client: AsyncBelieve) -> None:
        response = await async_client.teams.logo.with_raw_response.download(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logo = await response.parse()
        assert_matches_type(object, logo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncBelieve) -> None:
        async with async_client.teams.logo.with_streaming_response.download(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logo = await response.parse()
            assert_matches_type(object, logo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_download(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.logo.with_raw_response.download(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                team_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.teams.logo.with_raw_response.download(
                file_id="",
                team_id="team_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncBelieve) -> None:
        logo = await async_client.teams.logo.upload(
            team_id="team_id",
            file=b"raw file contents",
        )
        assert_matches_type(FileUpload, logo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncBelieve) -> None:
        response = await async_client.teams.logo.with_raw_response.upload(
            team_id="team_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logo = await response.parse()
        assert_matches_type(FileUpload, logo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncBelieve) -> None:
        async with async_client.teams.logo.with_streaming_response.upload(
            team_id="team_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logo = await response.parse()
            assert_matches_type(FileUpload, logo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.logo.with_raw_response.upload(
                team_id="",
                file=b"raw file contents",
            )
