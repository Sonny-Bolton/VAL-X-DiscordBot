import discord
from discord.ext import commands

EVENT_CHANNEL_ID = 1434598057785163927


class EventModal(discord.ui.Modal, title="Create Event"):
    title_field = discord.ui.TextInput(label="Event Title", placeholder="Enter the event name", required=True)
    description_field = discord.ui.TextInput(
        label="Event Description", style=discord.TextStyle.paragraph, required=True, placeholder="Describe the event details"
    )
    date_field = discord.ui.TextInput(label="Date & Time", placeholder="e.g. March 5th, 7 PM EST", required=True)

    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    async def on_submit(self, interaction: discord.Interaction):
        channel = interaction.guild.get_channel(EVENT_CHANNEL_ID)
        if not channel:
            await interaction.response.send_message("❌ Event announcement channel not found.", ephemeral=True)
            return

        embed = discord.Embed(
            title=f"📅 {self.title_field.value}",
            description=self.description_field.value,
            color=0x2ECC71,
        )
        embed.add_field(name="🕓 When", value=self.date_field.value, inline=False)
        embed.set_footer(text=f"Posted by {interaction.user.display_name}")
        await channel.send(embed=embed)
        await interaction.response.send_message("✅ Event created and posted!", ephemeral=True)
        print(f"[DEBUG] Event created by {interaction.user}: {self.title_field.value}")


class EventSystem(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("✅ EventSystem cog initialized")

    @discord.app_commands.command(name="event", description="Create and announce an event.")
    async def event(self, interaction: discord.Interaction):
        await interaction.response.send_modal(EventModal(self.bot))


async def setup(bot: commands.Bot):
    await bot.add_cog(EventSystem(bot))
    print("[DEBUG] EventSystem cog loaded")
