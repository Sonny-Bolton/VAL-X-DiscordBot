import discord
from discord.ext import commands

PLAYTEST_CHANNEL_ID = playtest-channel


class PlaytestModal(discord.ui.Modal, title="Playtest Sign-Up"):
    game_name = discord.ui.TextInput(label="Game name", placeholder="Which game are you signing up to test?", required=True)
    notes = discord.ui.TextInput(
        label="Notes (optional)", style=discord.TextStyle.paragraph, required=False, placeholder="Any experience, availability, or comments?"
    )

    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    async def on_submit(self, interaction: discord.Interaction):
        channel = interaction.guild.get_channel(PLAYTEST_CHANNEL_ID)
        if not channel:
            await interaction.response.send_message("❌ Playtest log channel not found.", ephemeral=True)
            return

        embed = discord.Embed(
            title="🧪 New Playtest Sign-Up",
            color=0x5865F2,
            description=f"**User:** {interaction.user.mention}\n**Game:** {self.game_name.value}\n\n**Notes:**\n{self.notes.value or 'No additional notes.'}"
        )
        embed.set_footer(text=f"User ID: {interaction.user.id}")
        await channel.send(embed=embed)
        await interaction.response.send_message("✅ Your playtest sign-up has been submitted!", ephemeral=True)
        print(f"[DEBUG] Playtest sign-up submitted by {interaction.user}")


class PlaytestSignup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("✅ PlaytestSignup cog initialized")

    @discord.app_commands.command(name="playtest", description="Sign up to playtest a game.")
    async def playtest(self, interaction: discord.Interaction):
        await interaction.response.send_modal(PlaytestModal(self.bot))


async def setup(bot: commands.Bot):
    await bot.add_cog(PlaytestSignup(bot))
    print("[DEBUG] PlaytestSignup cog loaded")

