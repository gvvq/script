
@bot.command()
async def nosebleed(ctx):
    mentioned_user = ctx.message.mentions[0] if ctx.message.mentions else None
    await ctx.message.delete()
    api_url = 'https://kawaii.red/api/gif/nosebleed?token=anonymous'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'response' in data:
            nosebleed_image_url = data['response']
            await ctx.send(f"{mentioned_user}")
            await ctx.send(nosebleed_image_url)
