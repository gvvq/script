@bot.command()
async def hex(ctx, color: str):
    await ctx.message.delete()
    api_url = f"https://api.popcat.xyz/color/{color}"
    response = requests.get(api_url)
    data = response.json()

    hex_code = data.get("hex", "Unknown")
    rgb_code = data.get("rgb", "Unknown")
    image_url = data.get("color_image", "")

    await ctx.send(f"```ini\n[ {hex_code} ]\n[ {rgb_code} ]```")
    await ctx.send(image_url)