@bot.command()
async def swebhook(ctx, webhook_url: str, *, message: str):
    data = {'content': message}
    requests.post(webhook_url, json=data)
    await asyncio.sleep(1)
    await ctx.message.delete()
