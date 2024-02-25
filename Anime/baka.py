@bot.command()
async def baka(ctx):
    mentioned_user = ctx.message.mentions[0] if ctx.message.mentions else None
    await ctx.message.delete()
    api_url = 'https://kawaii.red/api/gif/baka?token=anonymous'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'response' in data:
            baka_image_url = data['response']
            await ctx.send(baka_image_url)
            await ctx.send(f"{mentioned_user}")