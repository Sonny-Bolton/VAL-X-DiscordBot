import discord
from discord.ext import commands
import asyncio
import traceback

TOKEN = "bot-token"

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)

# -----------------------------
# Async cog loader
# -----------------------------
async def load_cogs():
    cogs = [
        "cogs.welcome",
        "cogs.playtest_signup",
        "cogs.event_system",
        "cogs.feedback",
        "cogs.patchnotes",
        "cogs.logging",
        "cogs.studioinfo",
        "cogs.spotlight",
        "cogs.featureidea"
        
    ]
    for ext in cogs:
        try:
            await bot.load_extension(ext)
            print(f"✅ Loaded {ext}")
        except Exception as e:
            print(f"❌ Failed to load {ext}")
            traceback.print_exc()

# -----------------------------
# On ready event
# -----------------------------
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        await bot.tree.sync()
        print("✅ Slash commands synced!")
    except Exception as e:
        print(f"❌ Failed to sync slash commands: {e}")

# -----------------------------
# Async main to run the bot
# -----------------------------
async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

# -----------------------------
# Run the bot
# -----------------------------
asyncio.run(main())











