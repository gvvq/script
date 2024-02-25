@bot.command()
async def apod(ctx):
    await ctx.message.delete()
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
    data = response.json()
    image_url = data['url']
    explanation = data['explanation']
    await ctx.send(f"**Astronomy Picture of the Day**\n{explanation}")
    await ctx.send(f"{image_url}")