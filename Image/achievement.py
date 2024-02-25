@bot.command()
async def achievement(ctx, *, text):
    await ctx.message.delete()
    api_url = f'https://api.alexflipnote.dev/achievement?text={text}'
    response = requests.get(api_url)
    if response.status_code == 200:
        await ctx.send(file=discord.File(io.BytesIO(response.content), 'achievement_image.png'))
    else:
        await ctx.send(f"Failed to generate achievement image. API status code: {response.status_code}")