@bot.command(aliases=["gb", "gel"])
@commands.cooldown(1, 1, commands.BucketType.user)
async def gelbooru(ctx, *, query=None):
    if not ctx.channel.is_nsfw():
        await ctx.reply("This command can only be used in NSFW channels.", mention_author=False)
        return
    
    if query is None:
        query = ""

    api_url = f'https://gelbooru.com/index.php?page=dapi&s=post&q=index&tags={query}'
    response = requests.get(api_url)

    if response.status_code == 200:
        root = ET.fromstring(response.text)
        posts = root.findall('.//post')
        if posts:
            post = random.choice(posts)
            media_url = post.find('file_url').text
            file_extension = media_url.split('.')[-1].lower()
            if query == "":
                await ctx.reply(f"Random Gelbooru Image - Random\n{media_url}", mention_author=False)
                return
            elif query == "" and file_extension in ('gif', 'webm', 'mp4', 'mkv'):
                await ctx.reply(f"Random Gelbooru Video - Random\n{media_url}", mention_author=False)
                return
            if file_extension in ('gif', 'webm', 'mp4', 'mkv'):
                await ctx.reply(f"Random Gelbooru Video - {query}\n{media_url}", mention_author=False, allowed_mentions=discord.AllowedMentions.none())
            else:
                await ctx.reply(f"Random Gelbooru Image - {query}\n{media_url}", mention_author=False, allowed_mentions=discord.AllowedMentions.none())
        else:
            await ctx.reply(f"No results found.", mention_author=False)
    else:
        await ctx.reply("Failed to fetch response. Please try again later.", mention_author=False)
