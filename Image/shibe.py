@bot.command()
async def shibe(ctx):
    await ctx.message.delete()
    api_url = 'https://shibe.online/api/shibes?'

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and data:
            image_url = data[0]
            await ctx.send(image_url)
        else:
            await ctx.send("Image not found")
    else:
        await ctx.send(f"Failed to fetch the shibe image. API status code: {response.status_code}")
