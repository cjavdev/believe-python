# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from believe import Believe, AsyncBelieve

from believe.types import TicketSale

from typing import cast, Any

from believe.pagination import SyncSkipLimitPage, AsyncSkipLimitPage

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from believe import Believe, AsyncBelieve
from tests.utils import assert_matches_type
from believe.types import ticket_sale_create_params
from believe.types import ticket_sale_update_params
from believe.types import ticket_sale_list_params
from believe.types import PurchaseMethod
from believe.types import PurchaseMethod
from believe.types import PurchaseMethod

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestTicketSales:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Believe) -> None:
        ticket_sale = client.ticket_sales.create(
            buyer_name="Mae Green",
            currency="GBP",
            discount="9.00",
            match_id="match-001",
            purchase_method="online",
            quantity=2,
            subtotal="90.00",
            tax="16.20",
            total="97.20",
            unit_price="45.00",
        )
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Believe) -> None:
        ticket_sale = client.ticket_sales.create(
            buyer_name="Mae Green",
            currency="GBP",
            discount="9.00",
            match_id="match-001",
            purchase_method="online",
            quantity=2,
            subtotal="90.00",
            tax="16.20",
            total="97.20",
            unit_price="45.00",
            buyer_email="mae.green@example.com",
            coupon_code="BELIEVE10",
        )
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Believe) -> None:

        response = client.ticket_sales.with_raw_response.create(
            buyer_name="Mae Green",
            currency="GBP",
            discount="9.00",
            match_id="match-001",
            purchase_method="online",
            quantity=2,
            subtotal="90.00",
            tax="16.20",
            total="97.20",
            unit_price="45.00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        ticket_sale = response.parse()
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Believe) -> None:
        with client.ticket_sales.with_streaming_response.create(
            buyer_name="Mae Green",
            currency="GBP",
            discount="9.00",
            match_id="match-001",
            purchase_method="online",
            quantity=2,
            subtotal="90.00",
            tax="16.20",
            total="97.20",
            unit_price="45.00",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            ticket_sale = response.parse()
            assert_matches_type(TicketSale, ticket_sale, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Believe) -> None:
        ticket_sale = client.ticket_sales.retrieve(
            "ticket_sale_id",
        )
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Believe) -> None:

        response = client.ticket_sales.with_raw_response.retrieve(
            "ticket_sale_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        ticket_sale = response.parse()
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Believe) -> None:
        with client.ticket_sales.with_streaming_response.retrieve(
            "ticket_sale_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            ticket_sale = response.parse()
            assert_matches_type(TicketSale, ticket_sale, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_sale_id` but received ''"):
          client.ticket_sales.with_raw_response.retrieve(
              "",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Believe) -> None:
        ticket_sale = client.ticket_sales.update(
            ticket_sale_id="ticket_sale_id",
        )
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Believe) -> None:
        ticket_sale = client.ticket_sales.update(
            ticket_sale_id="ticket_sale_id",
            buyer_email="dev@stainless.com",
            buyer_name="buyer_name",
            coupon_code="coupon_code",
            currency="currency",
            discount="discount",
            match_id="match_id",
            purchase_method="online",
            quantity=1,
            subtotal="subtotal",
            tax="tax",
            total="total",
            unit_price="unit_price",
        )
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Believe) -> None:

        response = client.ticket_sales.with_raw_response.update(
            ticket_sale_id="ticket_sale_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        ticket_sale = response.parse()
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Believe) -> None:
        with client.ticket_sales.with_streaming_response.update(
            ticket_sale_id="ticket_sale_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            ticket_sale = response.parse()
            assert_matches_type(TicketSale, ticket_sale, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_sale_id` but received ''"):
          client.ticket_sales.with_raw_response.update(
              ticket_sale_id="",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Believe) -> None:
        ticket_sale = client.ticket_sales.list()
        assert_matches_type(SyncSkipLimitPage[TicketSale], ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Believe) -> None:
        ticket_sale = client.ticket_sales.list(
            coupon_code="coupon_code",
            currency="currency",
            limit=10,
            match_id="match_id",
            purchase_method="online",
            skip=0,
        )
        assert_matches_type(SyncSkipLimitPage[TicketSale], ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Believe) -> None:

        response = client.ticket_sales.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        ticket_sale = response.parse()
        assert_matches_type(SyncSkipLimitPage[TicketSale], ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Believe) -> None:
        with client.ticket_sales.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            ticket_sale = response.parse()
            assert_matches_type(SyncSkipLimitPage[TicketSale], ticket_sale, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Believe) -> None:
        ticket_sale = client.ticket_sales.delete(
            "ticket_sale_id",
        )
        assert ticket_sale is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Believe) -> None:

        response = client.ticket_sales.with_raw_response.delete(
            "ticket_sale_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        ticket_sale = response.parse()
        assert ticket_sale is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Believe) -> None:
        with client.ticket_sales.with_streaming_response.delete(
            "ticket_sale_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            ticket_sale = response.parse()
            assert ticket_sale is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Believe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_sale_id` but received ''"):
          client.ticket_sales.with_raw_response.delete(
              "",
          )
class TestAsyncTicketSales:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBelieve) -> None:
        ticket_sale = await async_client.ticket_sales.create(
            buyer_name="Mae Green",
            currency="GBP",
            discount="9.00",
            match_id="match-001",
            purchase_method="online",
            quantity=2,
            subtotal="90.00",
            tax="16.20",
            total="97.20",
            unit_price="45.00",
        )
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBelieve) -> None:
        ticket_sale = await async_client.ticket_sales.create(
            buyer_name="Mae Green",
            currency="GBP",
            discount="9.00",
            match_id="match-001",
            purchase_method="online",
            quantity=2,
            subtotal="90.00",
            tax="16.20",
            total="97.20",
            unit_price="45.00",
            buyer_email="mae.green@example.com",
            coupon_code="BELIEVE10",
        )
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBelieve) -> None:

        response = await async_client.ticket_sales.with_raw_response.create(
            buyer_name="Mae Green",
            currency="GBP",
            discount="9.00",
            match_id="match-001",
            purchase_method="online",
            quantity=2,
            subtotal="90.00",
            tax="16.20",
            total="97.20",
            unit_price="45.00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        ticket_sale = await response.parse()
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBelieve) -> None:
        async with async_client.ticket_sales.with_streaming_response.create(
            buyer_name="Mae Green",
            currency="GBP",
            discount="9.00",
            match_id="match-001",
            purchase_method="online",
            quantity=2,
            subtotal="90.00",
            tax="16.20",
            total="97.20",
            unit_price="45.00",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            ticket_sale = await response.parse()
            assert_matches_type(TicketSale, ticket_sale, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBelieve) -> None:
        ticket_sale = await async_client.ticket_sales.retrieve(
            "ticket_sale_id",
        )
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBelieve) -> None:

        response = await async_client.ticket_sales.with_raw_response.retrieve(
            "ticket_sale_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        ticket_sale = await response.parse()
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBelieve) -> None:
        async with async_client.ticket_sales.with_streaming_response.retrieve(
            "ticket_sale_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            ticket_sale = await response.parse()
            assert_matches_type(TicketSale, ticket_sale, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_sale_id` but received ''"):
          await async_client.ticket_sales.with_raw_response.retrieve(
              "",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBelieve) -> None:
        ticket_sale = await async_client.ticket_sales.update(
            ticket_sale_id="ticket_sale_id",
        )
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBelieve) -> None:
        ticket_sale = await async_client.ticket_sales.update(
            ticket_sale_id="ticket_sale_id",
            buyer_email="dev@stainless.com",
            buyer_name="buyer_name",
            coupon_code="coupon_code",
            currency="currency",
            discount="discount",
            match_id="match_id",
            purchase_method="online",
            quantity=1,
            subtotal="subtotal",
            tax="tax",
            total="total",
            unit_price="unit_price",
        )
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBelieve) -> None:

        response = await async_client.ticket_sales.with_raw_response.update(
            ticket_sale_id="ticket_sale_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        ticket_sale = await response.parse()
        assert_matches_type(TicketSale, ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBelieve) -> None:
        async with async_client.ticket_sales.with_streaming_response.update(
            ticket_sale_id="ticket_sale_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            ticket_sale = await response.parse()
            assert_matches_type(TicketSale, ticket_sale, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_sale_id` but received ''"):
          await async_client.ticket_sales.with_raw_response.update(
              ticket_sale_id="",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBelieve) -> None:
        ticket_sale = await async_client.ticket_sales.list()
        assert_matches_type(AsyncSkipLimitPage[TicketSale], ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBelieve) -> None:
        ticket_sale = await async_client.ticket_sales.list(
            coupon_code="coupon_code",
            currency="currency",
            limit=10,
            match_id="match_id",
            purchase_method="online",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimitPage[TicketSale], ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBelieve) -> None:

        response = await async_client.ticket_sales.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        ticket_sale = await response.parse()
        assert_matches_type(AsyncSkipLimitPage[TicketSale], ticket_sale, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBelieve) -> None:
        async with async_client.ticket_sales.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            ticket_sale = await response.parse()
            assert_matches_type(AsyncSkipLimitPage[TicketSale], ticket_sale, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBelieve) -> None:
        ticket_sale = await async_client.ticket_sales.delete(
            "ticket_sale_id",
        )
        assert ticket_sale is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBelieve) -> None:

        response = await async_client.ticket_sales.with_raw_response.delete(
            "ticket_sale_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        ticket_sale = await response.parse()
        assert ticket_sale is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBelieve) -> None:
        async with async_client.ticket_sales.with_streaming_response.delete(
            "ticket_sale_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            ticket_sale = await response.parse()
            assert ticket_sale is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBelieve) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_sale_id` but received ''"):
          await async_client.ticket_sales.with_raw_response.delete(
              "",
          )