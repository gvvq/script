@bot.command()
async def ask(ctx):
    mentioned_user = ctx.message.mentions[0] if ctx.message.mentions else None
    await ctx.message.delete()
    api_url = 'https://kawaii.red/api/gif/ask?token=anonymous'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'response' in data:
            ask_image_url = data['response']
            await ctx.send(f"{mentioned_user}")
            await ctx.send(ask_image_url)
