@bot.command()
async def duck(ctx):
    await ctx.message.delete()
    api_url = 'https://random-d.uk/api/v2/random'

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        image_url = data.get('url', 'Image not found')

        await ctx.send(image_url)
    else:
        await ctx.send(f"Failed to fetch the duck image. API status code: {response.status_code}")
