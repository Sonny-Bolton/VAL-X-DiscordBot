import discord
from discord.ext import commands

LOG_CHANNEL_ID = 1435752521892364391


class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("✅ Logging cog initialized")

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if message.author.bot:
            return

        guild = message.guild
        log_channel = guild.get_channel(LOG_CHANNEL_ID)
        if not log_channel:
            print("[DEBUG] Log channel not found.")
            return

        deleter = "Unknown (no audit log entry found)"
        try:
            async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.message_delete):
                if entry.target.id == message.author.id:
                    deleter = f"{entry.user} ({entry.user.id})"
                    break
        except discord.Forbidden:
            print("[DEBUG] Missing audit log permissions.")

        embed = discord.Embed(
            title="🗑️ Message Deleted",
            color=0xE74C3C,
            description=f"**Author:** {message.author.mention}\n**Deleted by:** {deleter}\n**Channel:** {message.channel.mention}"
        )
        if message.content:
            embed.add_field(name="Message Content", value=message.content[:1024], inline=False)
        embed.set_footer(text=f"Author ID: {message.author.id}")
        await log_channel.send(embed=embed)
        print(f"[DEBUG] Logged deleted message from {message.author}")


async def setup(bot):
    await bot.add_cog(Logging(bot))
    print("[DEBUG] Logging cog loaded")
