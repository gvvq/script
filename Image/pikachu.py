@bot.command()
async def pikachu(ctx):
    await ctx.message.delete()
    api_url = 'https://some-random-api.com/img/pikachu'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'image' in data:
            pickahu_image_url = data['link']
            await ctx.send(pikachu_image_url)
        else:
            await ctx.send("Image not found in the API response.")
    else:
        await ctx.send(f"Failed to fetch the pikachu. API status code: {response.status_code}")