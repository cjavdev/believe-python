# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import BelieveError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)

if TYPE_CHECKING:
    from .resources import (
        press,
        teams,
        client,
        health,
        quotes,
        stream,
        believe,
        matches,
        reframe,
        version,
        biscuits,
        coaching,
        episodes,
        pep_talk,
        webhooks,
        conflicts,
        characters,
        team_members,
    )
    from .resources.press import PressResource, AsyncPressResource
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.quotes import QuotesResource, AsyncQuotesResource
    from .resources.stream import StreamResource, AsyncStreamResource
    from .resources.believe import BelieveResource, AsyncBelieveResource
    from .resources.reframe import ReframeResource, AsyncReframeResource
    from .resources.version import VersionResource, AsyncVersionResource
    from .resources.biscuits import BiscuitsResource, AsyncBiscuitsResource
    from .resources.episodes import EpisodesResource, AsyncEpisodesResource
    from .resources.pep_talk import PepTalkResource, AsyncPepTalkResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.conflicts import ConflictsResource, AsyncConflictsResource
    from .resources.characters import CharactersResource, AsyncCharactersResource
    from .resources.teams.teams import TeamsResource, AsyncTeamsResource
    from .resources.team_members import TeamMembersResource, AsyncTeamMembersResource
    from .resources.client.client import ClientResource, AsyncClientResource
    from .resources.matches.matches import MatchesResource, AsyncMatchesResource
    from .resources.coaching.coaching import CoachingResource, AsyncCoachingResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Believe", "AsyncBelieve", "Client", "AsyncClient"]


class Believe(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Believe client instance.

        This automatically infers the `api_key` argument from the `BELIEVE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BELIEVE_API_KEY")
        if api_key is None:
            raise BelieveError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BELIEVE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BELIEVE_BASE_URL")
        if base_url is None:
            base_url = f"https://believe.cjav.dev"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def characters(self) -> CharactersResource:
        from .resources.characters import CharactersResource

        return CharactersResource(self)

    @cached_property
    def teams(self) -> TeamsResource:
        from .resources.teams import TeamsResource

        return TeamsResource(self)

    @cached_property
    def matches(self) -> MatchesResource:
        from .resources.matches import MatchesResource

        return MatchesResource(self)

    @cached_property
    def episodes(self) -> EpisodesResource:
        from .resources.episodes import EpisodesResource

        return EpisodesResource(self)

    @cached_property
    def quotes(self) -> QuotesResource:
        from .resources.quotes import QuotesResource

        return QuotesResource(self)

    @cached_property
    def believe(self) -> BelieveResource:
        from .resources.believe import BelieveResource

        return BelieveResource(self)

    @cached_property
    def conflicts(self) -> ConflictsResource:
        from .resources.conflicts import ConflictsResource

        return ConflictsResource(self)

    @cached_property
    def reframe(self) -> ReframeResource:
        from .resources.reframe import ReframeResource

        return ReframeResource(self)

    @cached_property
    def press(self) -> PressResource:
        from .resources.press import PressResource

        return PressResource(self)

    @cached_property
    def coaching(self) -> CoachingResource:
        from .resources.coaching import CoachingResource

        return CoachingResource(self)

    @cached_property
    def biscuits(self) -> BiscuitsResource:
        from .resources.biscuits import BiscuitsResource

        return BiscuitsResource(self)

    @cached_property
    def pep_talk(self) -> PepTalkResource:
        from .resources.pep_talk import PepTalkResource

        return PepTalkResource(self)

    @cached_property
    def stream(self) -> StreamResource:
        from .resources.stream import StreamResource

        return StreamResource(self)

    @cached_property
    def team_members(self) -> TeamMembersResource:
        from .resources.team_members import TeamMembersResource

        return TeamMembersResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def health(self) -> HealthResource:
        from .resources.health import HealthResource

        return HealthResource(self)

    @cached_property
    def version(self) -> VersionResource:
        from .resources.version import VersionResource

        return VersionResource(self)

    @cached_property
    def client(self) -> ClientResource:
        from .resources.client import ClientResource

        return ClientResource(self)

    @cached_property
    def with_raw_response(self) -> BelieveWithRawResponse:
        return BelieveWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BelieveWithStreamedResponse:
        return BelieveWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def get_welcome(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Get a warm welcome and overview of available endpoints."""
        return self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncBelieve(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncBelieve client instance.

        This automatically infers the `api_key` argument from the `BELIEVE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BELIEVE_API_KEY")
        if api_key is None:
            raise BelieveError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BELIEVE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BELIEVE_BASE_URL")
        if base_url is None:
            base_url = f"https://believe.cjav.dev"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def characters(self) -> AsyncCharactersResource:
        from .resources.characters import AsyncCharactersResource

        return AsyncCharactersResource(self)

    @cached_property
    def teams(self) -> AsyncTeamsResource:
        from .resources.teams import AsyncTeamsResource

        return AsyncTeamsResource(self)

    @cached_property
    def matches(self) -> AsyncMatchesResource:
        from .resources.matches import AsyncMatchesResource

        return AsyncMatchesResource(self)

    @cached_property
    def episodes(self) -> AsyncEpisodesResource:
        from .resources.episodes import AsyncEpisodesResource

        return AsyncEpisodesResource(self)

    @cached_property
    def quotes(self) -> AsyncQuotesResource:
        from .resources.quotes import AsyncQuotesResource

        return AsyncQuotesResource(self)

    @cached_property
    def believe(self) -> AsyncBelieveResource:
        from .resources.believe import AsyncBelieveResource

        return AsyncBelieveResource(self)

    @cached_property
    def conflicts(self) -> AsyncConflictsResource:
        from .resources.conflicts import AsyncConflictsResource

        return AsyncConflictsResource(self)

    @cached_property
    def reframe(self) -> AsyncReframeResource:
        from .resources.reframe import AsyncReframeResource

        return AsyncReframeResource(self)

    @cached_property
    def press(self) -> AsyncPressResource:
        from .resources.press import AsyncPressResource

        return AsyncPressResource(self)

    @cached_property
    def coaching(self) -> AsyncCoachingResource:
        from .resources.coaching import AsyncCoachingResource

        return AsyncCoachingResource(self)

    @cached_property
    def biscuits(self) -> AsyncBiscuitsResource:
        from .resources.biscuits import AsyncBiscuitsResource

        return AsyncBiscuitsResource(self)

    @cached_property
    def pep_talk(self) -> AsyncPepTalkResource:
        from .resources.pep_talk import AsyncPepTalkResource

        return AsyncPepTalkResource(self)

    @cached_property
    def stream(self) -> AsyncStreamResource:
        from .resources.stream import AsyncStreamResource

        return AsyncStreamResource(self)

    @cached_property
    def team_members(self) -> AsyncTeamMembersResource:
        from .resources.team_members import AsyncTeamMembersResource

        return AsyncTeamMembersResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def health(self) -> AsyncHealthResource:
        from .resources.health import AsyncHealthResource

        return AsyncHealthResource(self)

    @cached_property
    def version(self) -> AsyncVersionResource:
        from .resources.version import AsyncVersionResource

        return AsyncVersionResource(self)

    @cached_property
    def client(self) -> AsyncClientResource:
        from .resources.client import AsyncClientResource

        return AsyncClientResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncBelieveWithRawResponse:
        return AsyncBelieveWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBelieveWithStreamedResponse:
        return AsyncBelieveWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def get_welcome(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Get a warm welcome and overview of available endpoints."""
        return await self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class BelieveWithRawResponse:
    _client: Believe

    def __init__(self, client: Believe) -> None:
        self._client = client

        self.get_welcome = to_raw_response_wrapper(
            client.get_welcome,
        )

    @cached_property
    def characters(self) -> characters.CharactersResourceWithRawResponse:
        from .resources.characters import CharactersResourceWithRawResponse

        return CharactersResourceWithRawResponse(self._client.characters)

    @cached_property
    def teams(self) -> teams.TeamsResourceWithRawResponse:
        from .resources.teams import TeamsResourceWithRawResponse

        return TeamsResourceWithRawResponse(self._client.teams)

    @cached_property
    def matches(self) -> matches.MatchesResourceWithRawResponse:
        from .resources.matches import MatchesResourceWithRawResponse

        return MatchesResourceWithRawResponse(self._client.matches)

    @cached_property
    def episodes(self) -> episodes.EpisodesResourceWithRawResponse:
        from .resources.episodes import EpisodesResourceWithRawResponse

        return EpisodesResourceWithRawResponse(self._client.episodes)

    @cached_property
    def quotes(self) -> quotes.QuotesResourceWithRawResponse:
        from .resources.quotes import QuotesResourceWithRawResponse

        return QuotesResourceWithRawResponse(self._client.quotes)

    @cached_property
    def believe(self) -> believe.BelieveResourceWithRawResponse:
        from .resources.believe import BelieveResourceWithRawResponse

        return BelieveResourceWithRawResponse(self._client.believe)

    @cached_property
    def conflicts(self) -> conflicts.ConflictsResourceWithRawResponse:
        from .resources.conflicts import ConflictsResourceWithRawResponse

        return ConflictsResourceWithRawResponse(self._client.conflicts)

    @cached_property
    def reframe(self) -> reframe.ReframeResourceWithRawResponse:
        from .resources.reframe import ReframeResourceWithRawResponse

        return ReframeResourceWithRawResponse(self._client.reframe)

    @cached_property
    def press(self) -> press.PressResourceWithRawResponse:
        from .resources.press import PressResourceWithRawResponse

        return PressResourceWithRawResponse(self._client.press)

    @cached_property
    def coaching(self) -> coaching.CoachingResourceWithRawResponse:
        from .resources.coaching import CoachingResourceWithRawResponse

        return CoachingResourceWithRawResponse(self._client.coaching)

    @cached_property
    def biscuits(self) -> biscuits.BiscuitsResourceWithRawResponse:
        from .resources.biscuits import BiscuitsResourceWithRawResponse

        return BiscuitsResourceWithRawResponse(self._client.biscuits)

    @cached_property
    def pep_talk(self) -> pep_talk.PepTalkResourceWithRawResponse:
        from .resources.pep_talk import PepTalkResourceWithRawResponse

        return PepTalkResourceWithRawResponse(self._client.pep_talk)

    @cached_property
    def stream(self) -> stream.StreamResourceWithRawResponse:
        from .resources.stream import StreamResourceWithRawResponse

        return StreamResourceWithRawResponse(self._client.stream)

    @cached_property
    def team_members(self) -> team_members.TeamMembersResourceWithRawResponse:
        from .resources.team_members import TeamMembersResourceWithRawResponse

        return TeamMembersResourceWithRawResponse(self._client.team_members)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def health(self) -> health.HealthResourceWithRawResponse:
        from .resources.health import HealthResourceWithRawResponse

        return HealthResourceWithRawResponse(self._client.health)

    @cached_property
    def version(self) -> version.VersionResourceWithRawResponse:
        from .resources.version import VersionResourceWithRawResponse

        return VersionResourceWithRawResponse(self._client.version)

    @cached_property
    def client(self) -> client.ClientResourceWithRawResponse:
        from .resources.client import ClientResourceWithRawResponse

        return ClientResourceWithRawResponse(self._client.client)


class AsyncBelieveWithRawResponse:
    _client: AsyncBelieve

    def __init__(self, client: AsyncBelieve) -> None:
        self._client = client

        self.get_welcome = async_to_raw_response_wrapper(
            client.get_welcome,
        )

    @cached_property
    def characters(self) -> characters.AsyncCharactersResourceWithRawResponse:
        from .resources.characters import AsyncCharactersResourceWithRawResponse

        return AsyncCharactersResourceWithRawResponse(self._client.characters)

    @cached_property
    def teams(self) -> teams.AsyncTeamsResourceWithRawResponse:
        from .resources.teams import AsyncTeamsResourceWithRawResponse

        return AsyncTeamsResourceWithRawResponse(self._client.teams)

    @cached_property
    def matches(self) -> matches.AsyncMatchesResourceWithRawResponse:
        from .resources.matches import AsyncMatchesResourceWithRawResponse

        return AsyncMatchesResourceWithRawResponse(self._client.matches)

    @cached_property
    def episodes(self) -> episodes.AsyncEpisodesResourceWithRawResponse:
        from .resources.episodes import AsyncEpisodesResourceWithRawResponse

        return AsyncEpisodesResourceWithRawResponse(self._client.episodes)

    @cached_property
    def quotes(self) -> quotes.AsyncQuotesResourceWithRawResponse:
        from .resources.quotes import AsyncQuotesResourceWithRawResponse

        return AsyncQuotesResourceWithRawResponse(self._client.quotes)

    @cached_property
    def believe(self) -> believe.AsyncBelieveResourceWithRawResponse:
        from .resources.believe import AsyncBelieveResourceWithRawResponse

        return AsyncBelieveResourceWithRawResponse(self._client.believe)

    @cached_property
    def conflicts(self) -> conflicts.AsyncConflictsResourceWithRawResponse:
        from .resources.conflicts import AsyncConflictsResourceWithRawResponse

        return AsyncConflictsResourceWithRawResponse(self._client.conflicts)

    @cached_property
    def reframe(self) -> reframe.AsyncReframeResourceWithRawResponse:
        from .resources.reframe import AsyncReframeResourceWithRawResponse

        return AsyncReframeResourceWithRawResponse(self._client.reframe)

    @cached_property
    def press(self) -> press.AsyncPressResourceWithRawResponse:
        from .resources.press import AsyncPressResourceWithRawResponse

        return AsyncPressResourceWithRawResponse(self._client.press)

    @cached_property
    def coaching(self) -> coaching.AsyncCoachingResourceWithRawResponse:
        from .resources.coaching import AsyncCoachingResourceWithRawResponse

        return AsyncCoachingResourceWithRawResponse(self._client.coaching)

    @cached_property
    def biscuits(self) -> biscuits.AsyncBiscuitsResourceWithRawResponse:
        from .resources.biscuits import AsyncBiscuitsResourceWithRawResponse

        return AsyncBiscuitsResourceWithRawResponse(self._client.biscuits)

    @cached_property
    def pep_talk(self) -> pep_talk.AsyncPepTalkResourceWithRawResponse:
        from .resources.pep_talk import AsyncPepTalkResourceWithRawResponse

        return AsyncPepTalkResourceWithRawResponse(self._client.pep_talk)

    @cached_property
    def stream(self) -> stream.AsyncStreamResourceWithRawResponse:
        from .resources.stream import AsyncStreamResourceWithRawResponse

        return AsyncStreamResourceWithRawResponse(self._client.stream)

    @cached_property
    def team_members(self) -> team_members.AsyncTeamMembersResourceWithRawResponse:
        from .resources.team_members import AsyncTeamMembersResourceWithRawResponse

        return AsyncTeamMembersResourceWithRawResponse(self._client.team_members)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def version(self) -> version.AsyncVersionResourceWithRawResponse:
        from .resources.version import AsyncVersionResourceWithRawResponse

        return AsyncVersionResourceWithRawResponse(self._client.version)

    @cached_property
    def client(self) -> client.AsyncClientResourceWithRawResponse:
        from .resources.client import AsyncClientResourceWithRawResponse

        return AsyncClientResourceWithRawResponse(self._client.client)


class BelieveWithStreamedResponse:
    _client: Believe

    def __init__(self, client: Believe) -> None:
        self._client = client

        self.get_welcome = to_streamed_response_wrapper(
            client.get_welcome,
        )

    @cached_property
    def characters(self) -> characters.CharactersResourceWithStreamingResponse:
        from .resources.characters import CharactersResourceWithStreamingResponse

        return CharactersResourceWithStreamingResponse(self._client.characters)

    @cached_property
    def teams(self) -> teams.TeamsResourceWithStreamingResponse:
        from .resources.teams import TeamsResourceWithStreamingResponse

        return TeamsResourceWithStreamingResponse(self._client.teams)

    @cached_property
    def matches(self) -> matches.MatchesResourceWithStreamingResponse:
        from .resources.matches import MatchesResourceWithStreamingResponse

        return MatchesResourceWithStreamingResponse(self._client.matches)

    @cached_property
    def episodes(self) -> episodes.EpisodesResourceWithStreamingResponse:
        from .resources.episodes import EpisodesResourceWithStreamingResponse

        return EpisodesResourceWithStreamingResponse(self._client.episodes)

    @cached_property
    def quotes(self) -> quotes.QuotesResourceWithStreamingResponse:
        from .resources.quotes import QuotesResourceWithStreamingResponse

        return QuotesResourceWithStreamingResponse(self._client.quotes)

    @cached_property
    def believe(self) -> believe.BelieveResourceWithStreamingResponse:
        from .resources.believe import BelieveResourceWithStreamingResponse

        return BelieveResourceWithStreamingResponse(self._client.believe)

    @cached_property
    def conflicts(self) -> conflicts.ConflictsResourceWithStreamingResponse:
        from .resources.conflicts import ConflictsResourceWithStreamingResponse

        return ConflictsResourceWithStreamingResponse(self._client.conflicts)

    @cached_property
    def reframe(self) -> reframe.ReframeResourceWithStreamingResponse:
        from .resources.reframe import ReframeResourceWithStreamingResponse

        return ReframeResourceWithStreamingResponse(self._client.reframe)

    @cached_property
    def press(self) -> press.PressResourceWithStreamingResponse:
        from .resources.press import PressResourceWithStreamingResponse

        return PressResourceWithStreamingResponse(self._client.press)

    @cached_property
    def coaching(self) -> coaching.CoachingResourceWithStreamingResponse:
        from .resources.coaching import CoachingResourceWithStreamingResponse

        return CoachingResourceWithStreamingResponse(self._client.coaching)

    @cached_property
    def biscuits(self) -> biscuits.BiscuitsResourceWithStreamingResponse:
        from .resources.biscuits import BiscuitsResourceWithStreamingResponse

        return BiscuitsResourceWithStreamingResponse(self._client.biscuits)

    @cached_property
    def pep_talk(self) -> pep_talk.PepTalkResourceWithStreamingResponse:
        from .resources.pep_talk import PepTalkResourceWithStreamingResponse

        return PepTalkResourceWithStreamingResponse(self._client.pep_talk)

    @cached_property
    def stream(self) -> stream.StreamResourceWithStreamingResponse:
        from .resources.stream import StreamResourceWithStreamingResponse

        return StreamResourceWithStreamingResponse(self._client.stream)

    @cached_property
    def team_members(self) -> team_members.TeamMembersResourceWithStreamingResponse:
        from .resources.team_members import TeamMembersResourceWithStreamingResponse

        return TeamMembersResourceWithStreamingResponse(self._client.team_members)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def version(self) -> version.VersionResourceWithStreamingResponse:
        from .resources.version import VersionResourceWithStreamingResponse

        return VersionResourceWithStreamingResponse(self._client.version)

    @cached_property
    def client(self) -> client.ClientResourceWithStreamingResponse:
        from .resources.client import ClientResourceWithStreamingResponse

        return ClientResourceWithStreamingResponse(self._client.client)


class AsyncBelieveWithStreamedResponse:
    _client: AsyncBelieve

    def __init__(self, client: AsyncBelieve) -> None:
        self._client = client

        self.get_welcome = async_to_streamed_response_wrapper(
            client.get_welcome,
        )

    @cached_property
    def characters(self) -> characters.AsyncCharactersResourceWithStreamingResponse:
        from .resources.characters import AsyncCharactersResourceWithStreamingResponse

        return AsyncCharactersResourceWithStreamingResponse(self._client.characters)

    @cached_property
    def teams(self) -> teams.AsyncTeamsResourceWithStreamingResponse:
        from .resources.teams import AsyncTeamsResourceWithStreamingResponse

        return AsyncTeamsResourceWithStreamingResponse(self._client.teams)

    @cached_property
    def matches(self) -> matches.AsyncMatchesResourceWithStreamingResponse:
        from .resources.matches import AsyncMatchesResourceWithStreamingResponse

        return AsyncMatchesResourceWithStreamingResponse(self._client.matches)

    @cached_property
    def episodes(self) -> episodes.AsyncEpisodesResourceWithStreamingResponse:
        from .resources.episodes import AsyncEpisodesResourceWithStreamingResponse

        return AsyncEpisodesResourceWithStreamingResponse(self._client.episodes)

    @cached_property
    def quotes(self) -> quotes.AsyncQuotesResourceWithStreamingResponse:
        from .resources.quotes import AsyncQuotesResourceWithStreamingResponse

        return AsyncQuotesResourceWithStreamingResponse(self._client.quotes)

    @cached_property
    def believe(self) -> believe.AsyncBelieveResourceWithStreamingResponse:
        from .resources.believe import AsyncBelieveResourceWithStreamingResponse

        return AsyncBelieveResourceWithStreamingResponse(self._client.believe)

    @cached_property
    def conflicts(self) -> conflicts.AsyncConflictsResourceWithStreamingResponse:
        from .resources.conflicts import AsyncConflictsResourceWithStreamingResponse

        return AsyncConflictsResourceWithStreamingResponse(self._client.conflicts)

    @cached_property
    def reframe(self) -> reframe.AsyncReframeResourceWithStreamingResponse:
        from .resources.reframe import AsyncReframeResourceWithStreamingResponse

        return AsyncReframeResourceWithStreamingResponse(self._client.reframe)

    @cached_property
    def press(self) -> press.AsyncPressResourceWithStreamingResponse:
        from .resources.press import AsyncPressResourceWithStreamingResponse

        return AsyncPressResourceWithStreamingResponse(self._client.press)

    @cached_property
    def coaching(self) -> coaching.AsyncCoachingResourceWithStreamingResponse:
        from .resources.coaching import AsyncCoachingResourceWithStreamingResponse

        return AsyncCoachingResourceWithStreamingResponse(self._client.coaching)

    @cached_property
    def biscuits(self) -> biscuits.AsyncBiscuitsResourceWithStreamingResponse:
        from .resources.biscuits import AsyncBiscuitsResourceWithStreamingResponse

        return AsyncBiscuitsResourceWithStreamingResponse(self._client.biscuits)

    @cached_property
    def pep_talk(self) -> pep_talk.AsyncPepTalkResourceWithStreamingResponse:
        from .resources.pep_talk import AsyncPepTalkResourceWithStreamingResponse

        return AsyncPepTalkResourceWithStreamingResponse(self._client.pep_talk)

    @cached_property
    def stream(self) -> stream.AsyncStreamResourceWithStreamingResponse:
        from .resources.stream import AsyncStreamResourceWithStreamingResponse

        return AsyncStreamResourceWithStreamingResponse(self._client.stream)

    @cached_property
    def team_members(self) -> team_members.AsyncTeamMembersResourceWithStreamingResponse:
        from .resources.team_members import AsyncTeamMembersResourceWithStreamingResponse

        return AsyncTeamMembersResourceWithStreamingResponse(self._client.team_members)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def version(self) -> version.AsyncVersionResourceWithStreamingResponse:
        from .resources.version import AsyncVersionResourceWithStreamingResponse

        return AsyncVersionResourceWithStreamingResponse(self._client.version)

    @cached_property
    def client(self) -> client.AsyncClientResourceWithStreamingResponse:
        from .resources.client import AsyncClientResourceWithStreamingResponse

        return AsyncClientResourceWithStreamingResponse(self._client.client)


Client = Believe

AsyncClient = AsyncBelieve
