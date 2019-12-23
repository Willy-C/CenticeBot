import twitchio
from twitchio.ext import commands

from config import IRC_TOKEN, NICK, INIT_CHANNELS

bot = commands.Bot(
    irc_token=IRC_TOKEN,
    prefix='!',
    nick=NICK,
    initial_channels=INIT_CHANNELS
)

@bot.event
async def event_ready():
    print(f'Ready | {bot.nick}')

@bot.command(name='test')
async def test(ctx: twitchio.dataclasses.Context):
    await ctx.send('test success')


bot.run()
