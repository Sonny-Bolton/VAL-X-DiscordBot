import discord
from discord.ext import commands

FEEDBACK_CHANNEL_ID = 1435751220235997255


class FeedbackModal(discord.ui.Modal, title="Submit Feedback"):
    category = discord.ui.TextInput(label="Category", placeholder="Bug, feature, suggestion, etc.", required=True)
    message = discord.ui.TextInput(
        label="Feedback",
        style=discord.TextStyle.paragraph,
        placeholder="Enter your feedback or report here",
        required=True,
        max_length=1000
    )

    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    async def on_submit(self, interaction: discord.Interaction):
        channel = interaction.guild.get_channel(FEEDBACK_CHANNEL_ID)
        if not channel:
            await interaction.response.send_message("❌ Feedback channel not found.", ephemeral=True)
            return

        embed = discord.Embed(
            title="💬 New Feedback Submitted",
            color=0xF1C40F,
            description=f"**From:** {interaction.user.mention}\n**Category:** {self.category.value}\n\n**Feedback:**\n{self.message.value}"
        )
        embed.set_footer(text=f"User ID: {interaction.user.id}")
        await channel.send(embed=embed)
        await interaction.response.send_message("✅ Your feedback has been sent! Thank you!", ephemeral=True)
        print(f"[DEBUG] Feedback received from {interaction.user}")


class Feedback(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("✅ Feedback cog initialized")

    @discord.app_commands.command(name="feedback", description="Submit feedback or report an issue.")
    async def feedback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(FeedbackModal(self.bot))


async def setup(bot: commands.Bot):
    await bot.add_cog(Feedback(bot))
    print("[DEBUG] Feedback cog loaded")
