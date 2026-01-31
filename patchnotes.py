import discord
from discord.ext import commands

PATCHNOTES_CHANNEL_ID = patchnotes-channel


class PatchNotesModal(discord.ui.Modal, title="Post Patch Notes"):
    title_field = discord.ui.TextInput(label="Patch Title", placeholder="e.g. Version 1.2.3", required=True)
    notes_field = discord.ui.TextInput(
        label="Changelog",
        style=discord.TextStyle.paragraph,
        placeholder="- Fixed crashes\n- Improved performance\n- Added new features",
        required=True
    )

    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    async def on_submit(self, interaction: discord.Interaction):
        channel = interaction.guild.get_channel(PATCHNOTES_CHANNEL_ID)
        if not channel:
            await interaction.response.send_message("❌ Updates channel not found.", ephemeral=True)
            return

        embed = discord.Embed(
            title=f"🧾 {self.title_field.value}",
            description=self.notes_field.value,
            color=0x3498DB
        )
        embed.set_footer(text=f"Posted by {interaction.user.display_name}")
        await channel.send(embed=embed)
        await interaction.response.send_message("✅ Patch notes posted successfully!", ephemeral=True)
        print(f"[DEBUG] Patch notes posted by {interaction.user}: {self.title_field.value}")


class PatchNotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("✅ PatchNotes cog initialized")

    @discord.app_commands.command(name="patchnotes", description="Post a set of patch notes to the updates channel.")
    async def patchnotes(self, interaction: discord.Interaction):
        await interaction.response.send_modal(PatchNotesModal(self.bot))


async def setup(bot):
    await bot.add_cog(PatchNotes(bot))
    print("[DEBUG] PatchNotes cog loaded")

