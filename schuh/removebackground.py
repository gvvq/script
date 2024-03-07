@bot.command(aliases=['rbg', 'removebackground'])
@commands.cooldown(1, 1, commands.BucketType.user)
async def removebg(ctx, *args):
    await ctx.message.delete()
    if len(ctx.message.attachments) == 0 and len(args) == 0:
        await ctx.send("Please attach an image or provide an image URL.", mention_author=False)
        return

    if len(ctx.message.attachments) > 0:
        attachment_url = ctx.message.attachments[0].url
    elif len(args) == 1:
        attachment_url = args[0]
    else:
        await ctx.send("Please attach only one image or provide a single image URL.", mention_author=False)
        return

    headers = {"X-Api-Key": 'qHujCg2mAtoUBPhsxZJe6akH'}
    data = {"image_url": attachment_url}
    response = requests.post("https://api.remove.bg/v1.0/removebg", headers=headers, data=data)

    if response.status_code == 200:
        with open("silky_rbg.png", "wb") as f:
            f.write(response.content)

        await ctx.send("Background Removed", file=discord.File("silky_rbg.png"), mention_author=False)
        os.remove('silky_rbg.png')
    else:
        await ctx.send("Failed to remove background. Try another image or try again later.", mention_author=False)
