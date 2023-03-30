from discord.ext import commands
import discord

import aiohttp

import os


intents: discord.Intents = discord.Intents.all()
intents.typing = False


class Bot(commands.Bot):
    async def setup_hook(self) -> None:
        self.session = aiohttp.ClientSession()
        await self.load_extension("cogs.news")
        await self.load_extension("jishaku")

    async def on_ready(self) -> None:
        await self.tree.sync()


bot = Bot(
    command_prefix="!",
    intents=intents,
)


if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))