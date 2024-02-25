@bot.command()
async def car(ctx):
    await ctx.message.delete()
    api_url = 'https://api.popcat.xyz/car'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'image' in data:
            car_image_url = data['image']
            await ctx.send(car_image_url)
        else:
            await ctx.send("Image not found in the API response.")
    else:
        await ctx.send(f"Failed to fetch the car image. API status code: {response.status_code}")