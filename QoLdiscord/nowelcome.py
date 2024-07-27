@bot.listen("on_message")
async def noWelcome(message:discord.Message):
    if message.author.bot:
        if isinstance(message.channel, discord.DMChannel):
            messages = [msg async for msg in message.channel.history(limit=123)]
            if len(messages) == 1:
                await message.channel.ack()
                await message.channel.close()

#yRemo 609703131747450880