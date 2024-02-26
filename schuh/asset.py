@bot.command(aliases=["as"])
@commands.cooldown(1, 1, commands.BucketType.user)
async def asset(ctx, asset_id):
    if not asset_id.isdigit():
        await ctx.reply("Invalid asset ID. Please provide a valid asset ID.", mention_author=False)
        return
    try:
        response = requests.get(f"https://assetdelivery.roblox.com/v1/asset/?id={asset_id}")
        root = ET.fromstring(response.content)
        url_element = root.find(".//url")
        class_element = root.find(".//Item[@class]")

        if url_element is not None and class_element is not None:
            url = url_element.text
            new_id = url.split("=")[-1]
            asset_class = class_element.get("class")

            if new_id.startswith("rbxassetid://"):
                new_id = new_id[len("rbxassetid://"):]

            asset_link = f"https://www.roblox.com/catalog/{asset_id}/silky"

            catalog_page = requests.get(asset_link)
            catalog_soup = BeautifulSoup(catalog_page.text, 'html.parser')
            asset_name = catalog_soup.title.string
            asset_name = asset_name.replace(" - Roblox", "")

            response = requests.get(f"https://assetdelivery.roblox.com/v1/asset/?id={new_id}")
            with open(f"{asset_id}.png", "wb") as f:
                f.write(response.content)

            await ctx.reply(f"**Asset Name:** {asset_name}\n**Asset ID:** {asset_id}\n**Image ID:** {new_id}\n**Asset Type:** {asset_class}\n<{asset_link}>", file=discord.File(f"{asset_id}.png"), mention_author=False)
            os.remove(f"{asset_id}.png")
    except:
        await ctx.reply("An error occurred during asset retrieval, please check the ID and try again.", mention_author=False)