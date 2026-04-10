# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._resource import SyncAPIResource, AsyncAPIResource

from .._compat import cached_property

from ..types.ticket_sale import TicketSale

from .._utils import maybe_transform, path_template, async_maybe_transform

from .._base_client import make_request_options, AsyncPaginator

from ..types.purchase_method import PurchaseMethod

from typing import Optional

from .._types import Omit, omit, NotGiven

from ..pagination import SyncSkipLimitPage, AsyncSkipLimitPage

from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from .._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ..types import ticket_sale_create_params
from ..types import ticket_sale_update_params
from ..types import ticket_sale_list_params
from ..types import PurchaseMethod
from ..types import PurchaseMethod
from ..types import PurchaseMethod

__all__ = ["TicketSalesResource", "AsyncTicketSalesResource"]

class TicketSalesResource(SyncAPIResource):
    """
    Ticket sales with 300 records for practicing pagination, filtering, and financial data
    """
    @cached_property
    def with_raw_response(self) -> TicketSalesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return TicketSalesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TicketSalesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return TicketSalesResourceWithStreamingResponse(self)

    def create(self,
    *,
    buyer_name: str,
    currency: str,
    discount: str,
    match_id: str,
    purchase_method: PurchaseMethod,
    quantity: int,
    subtotal: str,
    tax: str,
    total: str,
    unit_price: str,
    buyer_email: Optional[str] | Omit = omit,
    coupon_code: Optional[str] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> TicketSale:
        """
        Record a new ticket sale.

        Args:
          buyer_name: Name of the ticket buyer

          currency: Currency code (GBP, USD, or EUR)

          discount: Discount amount applied from coupon

          match_id: ID of the match

          purchase_method: How the ticket was purchased

          quantity: Number of tickets purchased

          subtotal: Subtotal before discount and tax (unit_price \\** quantity)

          tax: Tax amount (20% UK VAT on discounted subtotal)

          total: Final total (subtotal - discount + tax)

          unit_price: Price per ticket (decimal string)

          buyer_email: Email of the ticket buyer

          coupon_code: Coupon code applied, if any

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ticket-sales",
            body=maybe_transform({
                "buyer_name": buyer_name,
                "currency": currency,
                "discount": discount,
                "match_id": match_id,
                "purchase_method": purchase_method,
                "quantity": quantity,
                "subtotal": subtotal,
                "tax": tax,
                "total": total,
                "unit_price": unit_price,
                "buyer_email": buyer_email,
                "coupon_code": coupon_code,
            }, ticket_sale_create_params.TicketSaleCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TicketSale,
        )

    def retrieve(self,
    ticket_sale_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> TicketSale:
        """
        Retrieve detailed information about a specific ticket sale.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticket_sale_id:
          raise ValueError(
            f'Expected a non-empty value for `ticket_sale_id` but received {ticket_sale_id!r}'
          )
        return self._get(
            path_template("/ticket-sales/{ticket_sale_id}", ticket_sale_id=ticket_sale_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TicketSale,
        )

    def update(self,
    ticket_sale_id: str,
    *,
    buyer_email: Optional[str] | Omit = omit,
    buyer_name: Optional[str] | Omit = omit,
    coupon_code: Optional[str] | Omit = omit,
    currency: Optional[str] | Omit = omit,
    discount: Optional[str] | Omit = omit,
    match_id: Optional[str] | Omit = omit,
    purchase_method: Optional[PurchaseMethod] | Omit = omit,
    quantity: Optional[int] | Omit = omit,
    subtotal: Optional[str] | Omit = omit,
    tax: Optional[str] | Omit = omit,
    total: Optional[str] | Omit = omit,
    unit_price: Optional[str] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> TicketSale:
        """
        Update specific fields of an existing ticket sale.

        Args:
          purchase_method: How the ticket was purchased.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticket_sale_id:
          raise ValueError(
            f'Expected a non-empty value for `ticket_sale_id` but received {ticket_sale_id!r}'
          )
        return self._patch(
            path_template("/ticket-sales/{ticket_sale_id}", ticket_sale_id=ticket_sale_id),
            body=maybe_transform({
                "buyer_email": buyer_email,
                "buyer_name": buyer_name,
                "coupon_code": coupon_code,
                "currency": currency,
                "discount": discount,
                "match_id": match_id,
                "purchase_method": purchase_method,
                "quantity": quantity,
                "subtotal": subtotal,
                "tax": tax,
                "total": total,
                "unit_price": unit_price,
            }, ticket_sale_update_params.TicketSaleUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TicketSale,
        )

    def list(self,
    *,
    coupon_code: Optional[str] | Omit = omit,
    currency: Optional[str] | Omit = omit,
    limit: int | Omit = omit,
    match_id: Optional[str] | Omit = omit,
    purchase_method: Optional[PurchaseMethod] | Omit = omit,
    skip: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> SyncSkipLimitPage[TicketSale]:
        """Get a paginated list of all ticket sales with optional filtering.

        With 300
        records, this endpoint is ideal for practicing pagination.

        Args:
          coupon_code: Filter by coupon code (use 'none' for sales without coupons)

          currency: Filter by currency (GBP, USD, EUR)

          limit: Maximum number of items to return (max: 100)

          match_id: Filter by match ID

          purchase_method: Filter by purchase method

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ticket-sales",
            page = SyncSkipLimitPage[TicketSale],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "coupon_code": coupon_code,
                "currency": currency,
                "limit": limit,
                "match_id": match_id,
                "purchase_method": purchase_method,
                "skip": skip,
            }, ticket_sale_list_params.TicketSaleListParams)),
            model=TicketSale,
        )

    def delete(self,
    ticket_sale_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Remove a ticket sale from the database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticket_sale_id:
          raise ValueError(
            f'Expected a non-empty value for `ticket_sale_id` but received {ticket_sale_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/ticket-sales/{ticket_sale_id}", ticket_sale_id=ticket_sale_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

class AsyncTicketSalesResource(AsyncAPIResource):
    """
    Ticket sales with 300 records for practicing pagination, filtering, and financial data
    """
    @cached_property
    def with_raw_response(self) -> AsyncTicketSalesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTicketSalesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTicketSalesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return AsyncTicketSalesResourceWithStreamingResponse(self)

    async def create(self,
    *,
    buyer_name: str,
    currency: str,
    discount: str,
    match_id: str,
    purchase_method: PurchaseMethod,
    quantity: int,
    subtotal: str,
    tax: str,
    total: str,
    unit_price: str,
    buyer_email: Optional[str] | Omit = omit,
    coupon_code: Optional[str] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> TicketSale:
        """
        Record a new ticket sale.

        Args:
          buyer_name: Name of the ticket buyer

          currency: Currency code (GBP, USD, or EUR)

          discount: Discount amount applied from coupon

          match_id: ID of the match

          purchase_method: How the ticket was purchased

          quantity: Number of tickets purchased

          subtotal: Subtotal before discount and tax (unit_price \\** quantity)

          tax: Tax amount (20% UK VAT on discounted subtotal)

          total: Final total (subtotal - discount + tax)

          unit_price: Price per ticket (decimal string)

          buyer_email: Email of the ticket buyer

          coupon_code: Coupon code applied, if any

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ticket-sales",
            body=await async_maybe_transform({
                "buyer_name": buyer_name,
                "currency": currency,
                "discount": discount,
                "match_id": match_id,
                "purchase_method": purchase_method,
                "quantity": quantity,
                "subtotal": subtotal,
                "tax": tax,
                "total": total,
                "unit_price": unit_price,
                "buyer_email": buyer_email,
                "coupon_code": coupon_code,
            }, ticket_sale_create_params.TicketSaleCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TicketSale,
        )

    async def retrieve(self,
    ticket_sale_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> TicketSale:
        """
        Retrieve detailed information about a specific ticket sale.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticket_sale_id:
          raise ValueError(
            f'Expected a non-empty value for `ticket_sale_id` but received {ticket_sale_id!r}'
          )
        return await self._get(
            path_template("/ticket-sales/{ticket_sale_id}", ticket_sale_id=ticket_sale_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TicketSale,
        )

    async def update(self,
    ticket_sale_id: str,
    *,
    buyer_email: Optional[str] | Omit = omit,
    buyer_name: Optional[str] | Omit = omit,
    coupon_code: Optional[str] | Omit = omit,
    currency: Optional[str] | Omit = omit,
    discount: Optional[str] | Omit = omit,
    match_id: Optional[str] | Omit = omit,
    purchase_method: Optional[PurchaseMethod] | Omit = omit,
    quantity: Optional[int] | Omit = omit,
    subtotal: Optional[str] | Omit = omit,
    tax: Optional[str] | Omit = omit,
    total: Optional[str] | Omit = omit,
    unit_price: Optional[str] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> TicketSale:
        """
        Update specific fields of an existing ticket sale.

        Args:
          purchase_method: How the ticket was purchased.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticket_sale_id:
          raise ValueError(
            f'Expected a non-empty value for `ticket_sale_id` but received {ticket_sale_id!r}'
          )
        return await self._patch(
            path_template("/ticket-sales/{ticket_sale_id}", ticket_sale_id=ticket_sale_id),
            body=await async_maybe_transform({
                "buyer_email": buyer_email,
                "buyer_name": buyer_name,
                "coupon_code": coupon_code,
                "currency": currency,
                "discount": discount,
                "match_id": match_id,
                "purchase_method": purchase_method,
                "quantity": quantity,
                "subtotal": subtotal,
                "tax": tax,
                "total": total,
                "unit_price": unit_price,
            }, ticket_sale_update_params.TicketSaleUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TicketSale,
        )

    def list(self,
    *,
    coupon_code: Optional[str] | Omit = omit,
    currency: Optional[str] | Omit = omit,
    limit: int | Omit = omit,
    match_id: Optional[str] | Omit = omit,
    purchase_method: Optional[PurchaseMethod] | Omit = omit,
    skip: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> AsyncPaginator[TicketSale, AsyncSkipLimitPage[TicketSale]]:
        """Get a paginated list of all ticket sales with optional filtering.

        With 300
        records, this endpoint is ideal for practicing pagination.

        Args:
          coupon_code: Filter by coupon code (use 'none' for sales without coupons)

          currency: Filter by currency (GBP, USD, EUR)

          limit: Maximum number of items to return (max: 100)

          match_id: Filter by match ID

          purchase_method: Filter by purchase method

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ticket-sales",
            page = AsyncSkipLimitPage[TicketSale],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "coupon_code": coupon_code,
                "currency": currency,
                "limit": limit,
                "match_id": match_id,
                "purchase_method": purchase_method,
                "skip": skip,
            }, ticket_sale_list_params.TicketSaleListParams)),
            model=TicketSale,
        )

    async def delete(self,
    ticket_sale_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Remove a ticket sale from the database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticket_sale_id:
          raise ValueError(
            f'Expected a non-empty value for `ticket_sale_id` but received {ticket_sale_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/ticket-sales/{ticket_sale_id}", ticket_sale_id=ticket_sale_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

class TicketSalesResourceWithRawResponse:
    def __init__(self, ticket_sales: TicketSalesResource) -> None:
        self._ticket_sales = ticket_sales

        self.create = to_raw_response_wrapper(
            ticket_sales.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ticket_sales.retrieve,
        )
        self.update = to_raw_response_wrapper(
            ticket_sales.update,
        )
        self.list = to_raw_response_wrapper(
            ticket_sales.list,
        )
        self.delete = to_raw_response_wrapper(
            ticket_sales.delete,
        )

class AsyncTicketSalesResourceWithRawResponse:
    def __init__(self, ticket_sales: AsyncTicketSalesResource) -> None:
        self._ticket_sales = ticket_sales

        self.create = async_to_raw_response_wrapper(
            ticket_sales.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ticket_sales.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            ticket_sales.update,
        )
        self.list = async_to_raw_response_wrapper(
            ticket_sales.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ticket_sales.delete,
        )

class TicketSalesResourceWithStreamingResponse:
    def __init__(self, ticket_sales: TicketSalesResource) -> None:
        self._ticket_sales = ticket_sales

        self.create = to_streamed_response_wrapper(
            ticket_sales.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ticket_sales.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ticket_sales.update,
        )
        self.list = to_streamed_response_wrapper(
            ticket_sales.list,
        )
        self.delete = to_streamed_response_wrapper(
            ticket_sales.delete,
        )

class AsyncTicketSalesResourceWithStreamingResponse:
    def __init__(self, ticket_sales: AsyncTicketSalesResource) -> None:
        self._ticket_sales = ticket_sales

        self.create = async_to_streamed_response_wrapper(
            ticket_sales.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ticket_sales.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ticket_sales.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ticket_sales.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ticket_sales.delete,
        )