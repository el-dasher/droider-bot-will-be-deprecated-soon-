from random import choice

import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext import commands

from lib.db.data.pydata.pydata import bot_presences
from src.lib.utils.basic_utils import ready_up_cog


class Funny(commands.Cog):
    def __init__(self, bot: discord.ext.commands.Bot):
        self.bot = bot
        self.scheduler = AsyncIOScheduler()

    @commands.Cog.listener()
    async def on_ready(self):
        self.scheduler.add_job(self.presences, CronTrigger(second=0))
        self.scheduler.start()

        ready_up_cog(self.bot, __name__)

    @commands.command()
    async def owo(self, ctx):
        await ctx.reply("UwU")

    async def presences(self):
        await self.bot.change_presence(activity=(choice(bot_presences)))

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f"Pingo, tô levando {self.bot.latency:.3f} milissegundos pra responder a api do Discord.")


def setup(bot):
    bot.add_cog(Funny(bot))
