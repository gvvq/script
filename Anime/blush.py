@bot.command()
async def blush(ctx):
    mentioned_user = ctx.message.mentions[0] if ctx.message.mentions else None
    await ctx.message.delete()
    api_url = 'https://kawaii.red/api/gif/blush?token=anonymous'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'response' in data:
            blush_image_url = data['response']
            await ctx.send(blush_image_url)
            await ctx.send(F"{mentioned_user}")