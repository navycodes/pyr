#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class UpdateReadChannelDiscussionOutbox(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``166``
        - ID: ``695C9E7C``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

        top_msg_id (``int`` ``32-bit``):
            N/A

        read_max_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["channel_id", "top_msg_id", "read_max_id"]

    ID = 0x695c9e7c
    QUALNAME = "types.UpdateReadChannelDiscussionOutbox"

    def __init__(self, *, channel_id: int, top_msg_id: int, read_max_id: int) -> None:
        self.channel_id = channel_id  # long
        self.top_msg_id = top_msg_id  # int
        self.read_max_id = read_max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateReadChannelDiscussionOutbox":
        # No flags
        
        channel_id = Long.read(b)
        
        top_msg_id = Int.read(b)
        
        read_max_id = Int.read(b)
        
        return UpdateReadChannelDiscussionOutbox(channel_id=channel_id, top_msg_id=top_msg_id, read_max_id=read_max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.top_msg_id))
        
        b.write(Int(self.read_max_id))
        
        return b.getvalue()
