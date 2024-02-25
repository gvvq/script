@bot.command()
async def nokia(ctx):
    await ctx.message.delete()
    if not ctx.message.mentions:
        await ctx.send("You need to mention a user.")
        return
    
    mentioned_member = ctx.message.mentions[0]
    user_pfp_url = mentioned_member.avatar if mentioned_member.avatar else mentioned_member.default_avatar
    api_url = f'https://api.popcat.xyz/nokia?image={user_pfp_url}'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        await ctx.send(file=discord.File(io.BytesIO(response.content), 'nokia_image.png'))
    else:
        await ctx.send(f"Failed to process the image. API status code: {response.status_code}")
