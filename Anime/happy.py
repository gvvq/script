
@bot.command()
async def happy(ctx):
    mentioned_user = ctx.message.mentions[0] if ctx.message.mentions else None
    await ctx.message.delete()
    api_url = 'https://kawaii.red/api/gif/happy?token=anonymous'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'response' in data:
            happy_image_url = data['response']
            await ctx.send(f"{mentioned_user}")
            await ctx.send(happy_image_url)
