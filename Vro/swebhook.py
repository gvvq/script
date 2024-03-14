@bot.command()
async def swebhook(ctx, webhook_url: str, *, message: str):
    data = {'content': message}
    response = requests.post(webhook_url, json=data)
    if response.status_code == 200:
        await ctx.send('Message sent successfully!')
    else:
        await ctx.send('Failed to send message.')
