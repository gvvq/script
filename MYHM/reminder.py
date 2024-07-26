@bot.command(name="reminder", usage='<minutes> <"text">', description="Send a reminder in the current channel")
async def reminder(ctx, minutes: int, text: str):
    await ctx.message.delete()
    await ctx.nighty_send(title="Reminder", content=f'Reminder set! I will remind you about `{text}` in `{minutes}` minutes!')
    await asyncio.sleep(minutes*60)
    await ctx.nighty_send(title="Reminder", content=text)