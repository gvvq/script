import typing
@bot.command()
async def cname(ctx, channel_id: typing.Optional[int] = None, *, new_name):
    await ctx.message.delete()
    channel = ctx.channel if channel_id is None else ctx.guild.get_channel(channel_id)
    if channel:
        await channel.edit(name=new_name)
