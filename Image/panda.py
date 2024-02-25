@bot.command()
async def panda(ctx):
    await ctx.message.delete()
    api_url = 'https://some-random-api.com/animal/panda'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'image' in data:
            panda_image_url = data['image']
            await ctx.send(panda_image_url)
        else:
            await ctx.send("Image not found in the API response.")
    else:
        await ctx.send(f"Failed to fetch the panda image. API status code: {response.status_code}")