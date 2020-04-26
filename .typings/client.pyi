from typing import List, Any
from discord import Message, TextChannel
from discord.ext import commands
from crypex.localdata.localdata import LocalData
from crypex.cogs.utils.template_objects import TemplateObjects

cogs: List[str]

class Crypex(commands.Bot):
    ld_handle: LocalData = ...
    templates: TemplateObjects = ...
    def __init__(self) -> None: ...
    def run(self) -> None: ...
    async def close(self) -> None: ...
    async def on_ready(self) -> None: ...
    async def on_message(self, message: Message) -> None: ...
    async def on_command_error(self, context: commands.Context, exception: Any) -> None: ...
    async def send(self, channel: TextChannel, **kwargs: dict) -> None: