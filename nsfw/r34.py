@bot.command(aliases=["r34"])
@commands.cooldown(1, 1, commands.BucketType.user)
async def rule34(ctx, *, query=None):
    if not ctx.channel.nsfw:
        await ctx.reply("This command can only be used in NSFW channels.", mention_author=False)
        return
    
    if query is None:
        query = ""

    api_url = f'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={query}'
    response = requests.get(api_url)

    if response.status_code == 200:
        root = ET.fromstring(response.text)
        if len(root) > 0:
            post = random.choice(root)
            media_url = post.attrib['file_url']
            file_extension = media_url.split('.')[-1].lower()
            if query == "":
                await ctx.reply(f"Random Rule34 Image - Random\n{media_url}", mention_author=False)
                return
            elif query == "" and file_extension in ('gif', 'webm', 'mp4', 'mkv'):
                await ctx.reply(f"Random Rule34 Video - Random\n{media_url}", mention_author=False)
                return
            if file_extension in ('gif', 'webm', 'mp4', 'mkv'):
                await ctx.reply(f"Random Rule34 Video - {query}\n{media_url}", mention_author=False, allowed_mentions=discord.AllowedMentions.none())
            else:
                await ctx.reply(f"Random Rule34 Image - {query}\n{media_url}", mention_author=False, allowed_mentions=discord.AllowedMentions.none())
        else:
            await ctx.reply(f"No results found.", mention_author=False)
    else:
        await ctx.reply("Failed to fetch response. Please try again later.", mention_author=False)
