import discord


class Page(discord.ui.View):

    def __init__(self, embeds: list[discord.Embed]):
        self.embeds = embeds
        self.now = 0
        super().__init__()

    @discord.ui.button(label="Back")
    async def _back(
        self, interaction: discord.Interaction,
        button: discord.ui.Button
    ) -> None:
        self.now -= 1
        await interaction.response.edit_message(
            embed=self.embeds[self.now], view=self
        )
    
    @discord.ui.button(label="Next")
    async def _next(
        self, interaction: discord.Interaction,
        button: discord.ui.Button
    ) -> None:
        self.now += 1
        await interaction.response.edit_message(
            embed=self.embeds[self.now], view=self
        )