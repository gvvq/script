@bot.command()
async def raccoon(ctx):
    await ctx.message.delete()
    api_url = 'https://some-random-api.com/animal/koala'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'image' in data:
            koala_image_url = data['image']
            await ctx.send(koala_image_url)
        else:
            await ctx.send("Image not found in the API response.")
    else:
        await ctx.send(f"Failed to fetch the koala image. API status code: {response.status_code}")