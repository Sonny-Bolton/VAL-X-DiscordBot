import discord
from discord.ext import commands

SPOTLIGHT_CHANNEL_ID = 1434598280662089860


class SpotlightModal(discord.ui.Modal, title="Submit a Community Spotlight"):
    name_field = discord.ui.TextInput(label="Creator / Featured Name", placeholder="Who or what are you spotlighting?", required=True)
    description_field = discord.ui.TextInput(
        label="Description",
        style=discord.TextStyle.paragraph,
        placeholder="Describe what makes this creation or person special.",
        required=True
    )
    link_field = discord.ui.TextInput(label="Link (optional)", placeholder="URL to image, post, or video", required=False)

    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    async def on_submit(self, interaction: discord.Interaction):
        channel = interaction.guild.get_channel(SPOTLIGHT_CHANNEL_ID)
        if not channel:
            await interaction.response.send_message("❌ Spotlight channel not found.", ephemeral=True)
            return

        embed = discord.Embed(
            title=f"🌟 Community Spotlight: {self.name_field.value}",
            description=self.description_field.value,
            color=0xF39C12
        )
        if self.link_field.value:
            embed.add_field(name="🔗 Link", value=self.link_field.value, inline=False)
        embed.set_footer(text=f"Submitted by {interaction.user.display_name}")
        await channel.send(embed=embed)
        await interaction.response.send_message("✅ Spotlight submitted successfully!", ephemeral=True)
        print(f"[DEBUG] Spotlight posted by {interaction.user}: {self.name_field.value}")


class Spotlight(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("✅ Spotlight cog initialized")

    @discord.app_commands.command(name="spotlight", description="Highlight a community creation or member.")
    async def spotlight(self, interaction: discord.Interaction):
        await interaction.response.send_modal(SpotlightModal(self.bot))


async def setup(bot):
    await bot.add_cog(Spotlight(bot))
    print("[DEBUG] Spotlight cog loaded")
