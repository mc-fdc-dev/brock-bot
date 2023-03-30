from discord.ext import commands
import discord
from discord import app_commands

from cogs.utils import news, page

from datetime import datetime


class News(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.news = news.News(bot.session)

    @app_commands.command(name="news", description="Send news")
    async def news(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer()
        news_items = await self.news.fetch_news()
        embeds = []
        for news_item in news_items:
            embeds.append(discord.Embed(
                title=news_item["title"],
                timestamp=datetime.strptime(
                    news_item["date"], "%Y.%m.%d"
                ),
                description=self.news.URL
            ))
        await interaction.followup.send(
            embed=embeds[0], view=page.Page(embeds)
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(News(bot))