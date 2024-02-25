@bot.command()
async def whale(ctx):
    await ctx.message.delete()
    api_url = 'https://some-random-api.com/img/whale'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'link' in data:
            whale_image_url = data['link']
            await ctx.send(whale_image_url)
        else:
            await ctx.send("Image not found in the API response.")
    else:
        await ctx.send(f"Failed to fetch the Whale image. API status code: {response.status_code}")