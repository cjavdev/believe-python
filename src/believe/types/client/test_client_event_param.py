# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "TestClientEventParam",
    "WebSocketClientPingMessage",
    "WebSocketClientPauseMessage",
    "WebSocketClientResumeMessage",
    "WebSocketClientSetSpeedMessage",
    "WebSocketClientGetStatusMessage",
]


class WebSocketClientPingMessage(TypedDict, total=False):
    """Ping message for keep-alive."""

    action: Required[Literal["ping"]]
    """Action to perform"""


class WebSocketClientPauseMessage(TypedDict, total=False):
    """Pause the match simulation."""

    action: Required[Literal["pause"]]
    """Action to perform"""


class WebSocketClientResumeMessage(TypedDict, total=False):
    """Resume a paused match simulation."""

    action: Required[Literal["resume"]]
    """Action to perform"""


class WebSocketClientSetSpeedMessage(TypedDict, total=False):
    """Change the simulation playback speed."""

    action: Required[Literal["set_speed"]]
    """Action to perform"""

    speed: Required[float]
    """Simulation speed multiplier (0.1 = slow motion, 10.0 = 10x faster)"""


class WebSocketClientGetStatusMessage(TypedDict, total=False):
    """Request current match status."""

    action: Required[Literal["get_status"]]
    """Action to perform"""


TestClientEventParam: TypeAlias = Union[
    WebSocketClientPingMessage,
    WebSocketClientPauseMessage,
    WebSocketClientResumeMessage,
    WebSocketClientSetSpeedMessage,
    WebSocketClientGetStatusMessage,
]
