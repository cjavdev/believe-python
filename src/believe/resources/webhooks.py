# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import webhook_create_params, webhook_trigger_event_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.registered_webhook import RegisteredWebhook
from ..types.webhook_list_response import WebhookListResponse
from ..types.webhook_create_response import WebhookCreateResponse
from ..types.webhook_delete_response import WebhookDeleteResponse
from ..types.webhook_trigger_event_response import WebhookTriggerEventResponse

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        url: str,
        description: Optional[str] | Omit = omit,
        event_types: Optional[List[Literal["match.completed", "team_member.transferred"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookCreateResponse:
        """
        Register a new webhook endpoint to receive event notifications.

        ## Event Types

        Available event types to subscribe to:

        - `match.completed` - Fired when a football match ends
        - `team_member.transferred` - Fired when a player/coach joins or leaves a team

        If no event types are specified, the webhook will receive all event types.

        ## Webhook Signatures

        All webhook deliveries include Standard Webhooks signature headers:

        - `webhook-id` - Unique message identifier
        - `webhook-timestamp` - Unix timestamp of when the webhook was sent
        - `webhook-signature` - HMAC-SHA256 signature in format `v1,{base64_signature}`

        Store the returned `secret` securely - you'll need it to verify webhook
        signatures.

        Args:
          url: The URL to send webhook events to

          description: Optional description for this webhook

          event_types: List of event types to subscribe to. If not provided, subscribes to all events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/webhooks",
            body=maybe_transform(
                {
                    "url": url,
                    "description": description,
                    "event_types": event_types,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookCreateResponse,
        )

    def retrieve(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegisteredWebhook:
        """
        Get details of a specific webhook endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._get(
            f"/webhooks/{webhook_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegisteredWebhook,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListResponse:
        """Get a list of all registered webhook endpoints."""
        return self._get(
            "/webhooks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookListResponse,
        )

    def delete(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDeleteResponse:
        """Unregister a webhook endpoint.

        It will no longer receive events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._delete(
            f"/webhooks/{webhook_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteResponse,
        )

    def trigger_event(
        self,
        *,
        event_type: Literal["match.completed", "team_member.transferred"],
        payload: Optional[webhook_trigger_event_params.Payload] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookTriggerEventResponse:
        """
        Trigger a webhook event and deliver it to all subscribed endpoints.

        This endpoint is useful for testing your webhook integration. It will:

        1. Generate an event with the specified type and payload
        2. Find all webhooks subscribed to that event type
        3. Send a POST request to each webhook URL with signature headers
        4. Return the delivery results

        ## Event Payload

        You can provide a custom payload, or leave it empty to use a sample payload.

        ## Webhook Signature Headers

        Each webhook delivery includes:

        - `webhook-id` - Unique event identifier (e.g., `evt_abc123...`)
        - `webhook-timestamp` - Unix timestamp
        - `webhook-signature` - HMAC-SHA256 signature (`v1,{base64}`)

        To verify signatures, compute:

        ```
        signature = HMAC - SHA256(key=base64_decode(secret_without_prefix), message="{timestamp}.{raw_json_payload}")
        ```

        Args:
          event_type: The type of event to trigger

          payload: Optional event payload. If not provided, a sample payload will be generated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/webhooks/trigger",
            body=maybe_transform(
                {
                    "event_type": event_type,
                    "payload": payload,
                },
                webhook_trigger_event_params.WebhookTriggerEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookTriggerEventResponse,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        url: str,
        description: Optional[str] | Omit = omit,
        event_types: Optional[List[Literal["match.completed", "team_member.transferred"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookCreateResponse:
        """
        Register a new webhook endpoint to receive event notifications.

        ## Event Types

        Available event types to subscribe to:

        - `match.completed` - Fired when a football match ends
        - `team_member.transferred` - Fired when a player/coach joins or leaves a team

        If no event types are specified, the webhook will receive all event types.

        ## Webhook Signatures

        All webhook deliveries include Standard Webhooks signature headers:

        - `webhook-id` - Unique message identifier
        - `webhook-timestamp` - Unix timestamp of when the webhook was sent
        - `webhook-signature` - HMAC-SHA256 signature in format `v1,{base64_signature}`

        Store the returned `secret` securely - you'll need it to verify webhook
        signatures.

        Args:
          url: The URL to send webhook events to

          description: Optional description for this webhook

          event_types: List of event types to subscribe to. If not provided, subscribes to all events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/webhooks",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "description": description,
                    "event_types": event_types,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookCreateResponse,
        )

    async def retrieve(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegisteredWebhook:
        """
        Get details of a specific webhook endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._get(
            f"/webhooks/{webhook_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegisteredWebhook,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListResponse:
        """Get a list of all registered webhook endpoints."""
        return await self._get(
            "/webhooks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookListResponse,
        )

    async def delete(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDeleteResponse:
        """Unregister a webhook endpoint.

        It will no longer receive events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._delete(
            f"/webhooks/{webhook_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteResponse,
        )

    async def trigger_event(
        self,
        *,
        event_type: Literal["match.completed", "team_member.transferred"],
        payload: Optional[webhook_trigger_event_params.Payload] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookTriggerEventResponse:
        """
        Trigger a webhook event and deliver it to all subscribed endpoints.

        This endpoint is useful for testing your webhook integration. It will:

        1. Generate an event with the specified type and payload
        2. Find all webhooks subscribed to that event type
        3. Send a POST request to each webhook URL with signature headers
        4. Return the delivery results

        ## Event Payload

        You can provide a custom payload, or leave it empty to use a sample payload.

        ## Webhook Signature Headers

        Each webhook delivery includes:

        - `webhook-id` - Unique event identifier (e.g., `evt_abc123...`)
        - `webhook-timestamp` - Unix timestamp
        - `webhook-signature` - HMAC-SHA256 signature (`v1,{base64}`)

        To verify signatures, compute:

        ```
        signature = HMAC - SHA256(key=base64_decode(secret_without_prefix), message="{timestamp}.{raw_json_payload}")
        ```

        Args:
          event_type: The type of event to trigger

          payload: Optional event payload. If not provided, a sample payload will be generated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/webhooks/trigger",
            body=await async_maybe_transform(
                {
                    "event_type": event_type,
                    "payload": payload,
                },
                webhook_trigger_event_params.WebhookTriggerEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookTriggerEventResponse,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_raw_response_wrapper(
            webhooks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            webhooks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = to_raw_response_wrapper(
            webhooks.delete,
        )
        self.trigger_event = to_raw_response_wrapper(
            webhooks.trigger_event,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_raw_response_wrapper(
            webhooks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            webhooks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            webhooks.delete,
        )
        self.trigger_event = async_to_raw_response_wrapper(
            webhooks.trigger_event,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_streamed_response_wrapper(
            webhooks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            webhooks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.trigger_event = to_streamed_response_wrapper(
            webhooks.trigger_event,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_streamed_response_wrapper(
            webhooks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            webhooks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.trigger_event = async_to_streamed_response_wrapper(
            webhooks.trigger_event,
        )
