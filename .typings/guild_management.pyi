from discord import Member, User, VoiceChannel, TextChannel
from discord.ext import commands
from typing import Any, Union

class GuildManagement(commands.Cog):
    client: commands.Bot = ...
    def __init__(self, client: commands.Bot) -> None: ...
    async def create_channel(self, ctx: commands.Context) -> None: ...
    async def delete_channel(self, ctx: commands.Context, channel: Union[TextChannel,
                            VoiceChannel], *, reason: str=...) -> None: ...
    async def ban(self, ctx: commands.Context, user: Union[Member, User, int], *, reason: str=...) -> None: ...

def setup(client: commands.Bot) -> None: ...
