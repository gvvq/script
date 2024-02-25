@bot.command()
async def rpanda(ctx):
    await ctx.message.delete()
    api_url = 'https://some-random-api.com/img/red_panda'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'image' in data:
            red_panda_image_url = data['image']
            await ctx.send(red_panda_image_url)
        else:
            await ctx.send("Image not found in the API response.")
    else:
        await ctx.send(f"Failed to fetch the red panda image. API status code: {response.status_code}")