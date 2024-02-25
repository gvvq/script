@bot.command()
async def kangaroo(ctx):
    await ctx.message.delete()
    api_url = 'https://some-random-api.com/animal/kangaroo'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'image' in data:
            kangaroo_image_url = data['image']
            await ctx.send(kangaroo_image_url)
        else:
            await ctx.send("Image not found in the API response.")
    else:
        await ctx.send(f"Failed to fetch the kangaroo image. API status code: {response.status_code}")