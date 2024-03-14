@bot.command()
async def swebhook(ctx, webhook_url: str, *, message: str):
    await ctx.message.delete()
    data = {'content': message}
    requests.post(webhook_url, json=data)
    await asyncio.sleep(1)
