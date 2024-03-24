@bot.command()
async def hex(ctx, color: str):
    await ctx.message.delete()
    api_url = f"https://api.popcat.xyz/color/{color}"
    response = requests.get(api_url)
    data = response.json()
    image_url = data.get("color_image", "")
    
    await ctx.send(image_url)
