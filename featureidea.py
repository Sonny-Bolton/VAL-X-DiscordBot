import discord
from discord.ext import commands

FEATURE_IDEA_CHANNEL_ID = Feature-Idea

class FeatureIdeaModal(discord.ui.Modal, title="Submit a Feature Idea"):
    game_field = discord.ui.TextInput(
        label="Game Title",
        placeholder="Which game is this idea for?",
        required=True
    )
    idea_field = discord.ui.TextInput(
        label="Your Idea",
        style=discord.TextStyle.paragraph,
        placeholder="Describe your idea in detail...",
        required=True
    )
    motivation_field = discord.ui.TextInput(
        label="Why is this idea useful?",
        style=discord.TextStyle.short,
        placeholder="Optional: Explain the benefit to the player or game",
        required=False
    )

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    async def on_submit(self, interaction: discord.Interaction):
        channel = interaction.guild.get_channel(FEATURE_IDEA_CHANNEL_ID)
        if not channel:
            await interaction.response.send_message("❌ Feature ideas channel not found.", ephemeral=True)
            return

        embed = discord.Embed(
            title=f"💡 Feature Idea: {self.game_field.value}",
            color=0xF1C40F,
            description=(
                f"**Suggested by:** {interaction.user.mention}\n\n"
                f"**Idea:** {self.idea_field.value}\n\n"
                f"**Motivation:** {self.motivation_field.value or '*No motivation provided*'}"
            )
        )
        embed.set_footer(text=f"User ID: {interaction.user.id}")
        await channel.send(embed=embed)
        await interaction.response.send_message("✅ Feature idea submitted successfully!", ephemeral=True)
        print(f"[DEBUG] Feature idea submitted by {interaction.user}: {self.game_field.value}")

class FeatureIdea(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("✅ FeatureIdea cog initialized")

    @discord.app_commands.command(name="featureidea", description="Submit a new feature idea for a game.")
    async def featureidea(self, interaction: discord.Interaction):
        await interaction.response.send_modal(FeatureIdeaModal(self.bot))

async def setup(bot):
    await bot.add_cog(FeatureIdea(bot))
    print("[DEBUG] FeatureIdea cog loaded")

