@bot.command()
async def raccoon(ctx):
    await ctx.message.delete()
    api_url = 'https://some-random-api.com/animal/raccoon'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'image' in data:
            raccoon_image_url = data['image']
            await ctx.send(raccoon_image_url)
        else:
            await ctx.send("Image not found in the API response.")
    else:
        await ctx.send(f"Failed to fetch the raccoon image. API status code: {response.status_code}")