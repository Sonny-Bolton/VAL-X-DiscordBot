import discord
from discord.ext import commands

class StudioInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("✅ StudioInfo cog initialized")

    @discord.app_commands.command(name="studioinfo", description="Show information about the studio.")
    async def studioinfo(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🎮 [D3VALEXSTUDIOS]",
            description="We’re an indie game development studio focused on creating immersive, story-driven experiences.",
            color=0x9B59B6
        )
        embed.add_field(name="🌐 Website", value="[Coming Soon]", inline=False)
        embed.add_field(name="🐦 Tiktok", value="[Follow Us](https://www.tiktok.com/@devalexstudio)", inline=True)
        embed.add_field(name="📺 YouTube", value="[Subscribe](https://www.youtube.com/@D3VALEXSTUDIO)", inline=True)
        embed.set_footer(text="© 2025 D3VALEXSTUDIOS")
        await interaction.response.send_message(embed=embed)
        print(f"[DEBUG] Studio info command used by {interaction.user}")


async def setup(bot):
    await bot.add_cog(StudioInfo(bot))
    print("[DEBUG] StudioInfo cog loaded")
