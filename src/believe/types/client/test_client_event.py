# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "TestClientEvent",
    "WebSocketClientPingMessage",
    "WebSocketClientPauseMessage",
    "WebSocketClientResumeMessage",
    "WebSocketClientSetSpeedMessage",
    "WebSocketClientGetStatusMessage",
]


class WebSocketClientPingMessage(BaseModel):
    """Ping message for keep-alive."""

    action: Literal["ping"]
    """Action to perform"""


class WebSocketClientPauseMessage(BaseModel):
    """Pause the match simulation."""

    action: Literal["pause"]
    """Action to perform"""


class WebSocketClientResumeMessage(BaseModel):
    """Resume a paused match simulation."""

    action: Literal["resume"]
    """Action to perform"""


class WebSocketClientSetSpeedMessage(BaseModel):
    """Change the simulation playback speed."""

    action: Literal["set_speed"]
    """Action to perform"""

    speed: float
    """Simulation speed multiplier (0.1 = slow motion, 10.0 = 10x faster)"""


class WebSocketClientGetStatusMessage(BaseModel):
    """Request current match status."""

    action: Literal["get_status"]
    """Action to perform"""


TestClientEvent: TypeAlias = Annotated[
    Union[
        WebSocketClientPingMessage,
        WebSocketClientPauseMessage,
        WebSocketClientResumeMessage,
        WebSocketClientSetSpeedMessage,
        WebSocketClientGetStatusMessage,
    ],
    PropertyInfo(discriminator="action"),
]
