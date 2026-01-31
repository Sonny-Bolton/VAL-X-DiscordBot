import discord
from discord.ext import commands

# Replace with your channel ID
WELCOME_CHANNEL_ID = welcome-channel
class Welcome(commands.Cog):
    """Welcome messages and test command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("✅ Welcome cog initialized")

    # Listener for new members
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        print(f"[DEBUG] on_member_join triggered for: {member} ({member.id}) in guild: {member.guild.name}")

        channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
        if not channel:
            print(f"[DEBUG] ❌ Could not find channel with ID {WELCOME_CHANNEL_ID}")
            return

        # Normal embed welcome message (kept exactly as you wanted)
        embed = discord.Embed(
            title=f"🎮 Welcome to {member.guild.name}!",
            description=(
                f"Hey {member.mention}! 👋\n\n"
                "Welcome to D3VALEXSTUDIOS!\n\n"
                "Here you will be able to learn about the team inside of our forums\n"
                "You will also be able to keep up to date with uploads and streams using our socials channel\n"
                "You may also get the chance to be apart of future playtesting\n"
                "Feel free to share any suggestions for game design or mechanics over in our suggestions channel\n\n"
                "We hope you enjoy your stay here at D3VALEXSTUDIOS"
            ),
            color=0x5865F2
        )
        embed.set_footer(text="A Warm Welcome From The Staff 💜")

        try:
            await channel.send(embed=embed)
            print(f"[DEBUG] Sent welcome embed to {channel.name} for {member}")
        except discord.Forbidden:
            print(f"[DEBUG] ❌ Cannot send messages to {channel.name} (missing permissions)")
        except Exception as e:
            print(f"[DEBUG] ❌ Error sending welcome: {e}")

   

# Async setup for your async loader
async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))

    print("[DEBUG] Welcome cog loaded")
