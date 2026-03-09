# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ws import (
    WsResource,
    AsyncWsResource,
    WsResourceWithRawResponse,
    AsyncWsResourceWithRawResponse,
    WsResourceWithStreamingResponse,
    AsyncWsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .ticket_sales import (
    TicketSalesResource,
    AsyncTicketSalesResource,
    TicketSalesResourceWithRawResponse,
    AsyncTicketSalesResourceWithRawResponse,
    TicketSalesResourceWithStreamingResponse,
    AsyncTicketSalesResourceWithStreamingResponse,
)

__all__ = ["ClientResource", "AsyncClientResource"]


class ClientResource(SyncAPIResource):
    @cached_property
    def ws(self) -> WsResource:
        """
        WebSocket endpoints for real-time bidirectional communication - Live match simulation
        """
        return WsResource(self._client)

    @cached_property
    def ticket_sales(self) -> TicketSalesResource:
        """
        Ticket sales with 300 records for practicing pagination, filtering, and financial data
        """
        return TicketSalesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ClientResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return ClientResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return ClientResourceWithStreamingResponse(self)


class AsyncClientResource(AsyncAPIResource):
    @cached_property
    def ws(self) -> AsyncWsResource:
        """
        WebSocket endpoints for real-time bidirectional communication - Live match simulation
        """
        return AsyncWsResource(self._client)

    @cached_property
    def ticket_sales(self) -> AsyncTicketSalesResource:
        """
        Ticket sales with 300 records for practicing pagination, filtering, and financial data
        """
        return AsyncTicketSalesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncClientResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClientResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return AsyncClientResourceWithStreamingResponse(self)


class ClientResourceWithRawResponse:
    def __init__(self, client: ClientResource) -> None:
        self._client = client

    @cached_property
    def ws(self) -> WsResourceWithRawResponse:
        """
        WebSocket endpoints for real-time bidirectional communication - Live match simulation
        """
        return WsResourceWithRawResponse(self._client.ws)

    @cached_property
    def ticket_sales(self) -> TicketSalesResourceWithRawResponse:
        """
        Ticket sales with 300 records for practicing pagination, filtering, and financial data
        """
        return TicketSalesResourceWithRawResponse(self._client.ticket_sales)


class AsyncClientResourceWithRawResponse:
    def __init__(self, client: AsyncClientResource) -> None:
        self._client = client

    @cached_property
    def ws(self) -> AsyncWsResourceWithRawResponse:
        """
        WebSocket endpoints for real-time bidirectional communication - Live match simulation
        """
        return AsyncWsResourceWithRawResponse(self._client.ws)

    @cached_property
    def ticket_sales(self) -> AsyncTicketSalesResourceWithRawResponse:
        """
        Ticket sales with 300 records for practicing pagination, filtering, and financial data
        """
        return AsyncTicketSalesResourceWithRawResponse(self._client.ticket_sales)


class ClientResourceWithStreamingResponse:
    def __init__(self, client: ClientResource) -> None:
        self._client = client

    @cached_property
    def ws(self) -> WsResourceWithStreamingResponse:
        """
        WebSocket endpoints for real-time bidirectional communication - Live match simulation
        """
        return WsResourceWithStreamingResponse(self._client.ws)

    @cached_property
    def ticket_sales(self) -> TicketSalesResourceWithStreamingResponse:
        """
        Ticket sales with 300 records for practicing pagination, filtering, and financial data
        """
        return TicketSalesResourceWithStreamingResponse(self._client.ticket_sales)


class AsyncClientResourceWithStreamingResponse:
    def __init__(self, client: AsyncClientResource) -> None:
        self._client = client

    @cached_property
    def ws(self) -> AsyncWsResourceWithStreamingResponse:
        """
        WebSocket endpoints for real-time bidirectional communication - Live match simulation
        """
        return AsyncWsResourceWithStreamingResponse(self._client.ws)

    @cached_property
    def ticket_sales(self) -> AsyncTicketSalesResourceWithStreamingResponse:
        """
        Ticket sales with 300 records for practicing pagination, filtering, and financial data
        """
        return AsyncTicketSalesResourceWithStreamingResponse(self._client.ticket_sales)
