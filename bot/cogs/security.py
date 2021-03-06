import logging

from discord.ext.commands import Bot, Cog, Context, NoPrivateMessage

log = logging.getLogger(__name__)


class Security(Cog):
    """Security-related helpers."""

    def __init__(self, bot: Bot):
        self.bot = bot
        self.bot.check(self.check_not_bot)  # Global commands check - no bots can run any commands at all
        self.bot.check(self.check_on_guild)  # Global commands check - commands can't be run in a DM

    def check_not_bot(self, ctx: Context) -> bool:
        """Check if the context is a bot user."""
        return not ctx.author.bot

    def check_on_guild(self, ctx: Context) -> bool:
        """Check if the context is in a guild."""
        if ctx.guild is None:
            raise NoPrivateMessage("This command cannot be used in private messages.")
        return True


def setup(bot: Bot) -> None:
    """Security cog load."""
    bot.add_cog(Security(bot))
    log.info("Cog loaded: Security")
