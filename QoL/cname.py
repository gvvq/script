@bot.command()
async def cname(ctx, channel_id: int, new_name):
    await ctx.message.delete()
    channel = ctx.guild.get_channel(channel_id)
    await channel.edit(name=new_name)
