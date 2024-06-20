@bot.command()
async def cchannel(ctx, channel_name):
    try:
        new_channel = await ctx.guild.create_text_channel(name=channel_name)
        await ctx.send(f"Channel {new_channel.mention} created successfully!")
    except discord.errors.HTTPException as e:
        pass