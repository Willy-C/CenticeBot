import twitchio
from twitchio.dataclasses import Context
from twitchio.ext import commands

import platform
from datetime import datetime

from config import IRC_TOKEN, NICK, INIT_CHANNELS


class CenticeBot(commands.Bot):
    def __init__(self):
        super().__init__(
            irc_token=IRC_TOKEN,
            nick=NICK,
            prefix='!',
            initial_channels=INIT_CHANNELS
        )

    async def event_ready(self):
        print(f'\nLogged in as: {self.nick}\n\n'
              f'Python Version: {platform.python_version()}\n'
              f'Library Version: {twitchio.__version__}')

        print(f'Ready! {datetime.utcnow()}\n')

    @commands.command(name='test')
    async def test(self, ctx: Context):
        await ctx.send('test success')


bot = CenticeBot()
bot.run()
