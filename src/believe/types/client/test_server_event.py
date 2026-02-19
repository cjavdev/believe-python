# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["TestServerEvent", "Welcome", "Echo"]


class Welcome(BaseModel):
    """Welcome message sent when connecting to the test WebSocket."""

    message: str
    """Welcome message"""

    ted_says: str
    """Ted's greeting"""

    type: Literal["welcome"]
    """Message type"""


class Echo(BaseModel):
    """Echo response from the test WebSocket."""

    message: str
    """The echoed message"""

    ted_says: str
    """Ted's response"""

    type: Literal["echo"]
    """Message type"""


TestServerEvent: TypeAlias = Annotated[Union[Welcome, Echo], PropertyInfo(discriminator="type")]
