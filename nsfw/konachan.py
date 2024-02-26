@bot.command(aliases=["kona"])
@commands.cooldown(1, 1, commands.BucketType.user)
async def konachan(ctx, *, query=None):
    if not ctx.channel.nsfw:
        await ctx.reply("This command can only be used in NSFW channels.", mention_author=False)
        return

    if query is None:
        query = ""

    api_url = f'https://konachan.com/post.json?limit=200&tags={query}'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        if data:
            random_post = random.choice(data)
            image_url = random_post['file_url']
            file_extension = image_url.split('.')[-1].lower()

            if query == "":
                await ctx.reply(f"Random Konachan Image - Random\n{image_url}", mention_author=False)
            elif query == "" and file_extension in ('gif', 'webm', 'mp4', 'mkv'):
                await ctx.reply(f"Random Gelbooru Video - Random\n{image_url}", mention_author=False)
                return
            else:
                if file_extension in ('gif', 'webm', 'mp4', 'mkv'):
                    await ctx.reply(f"Random Konachan Video - {query}\n{image_url}", mention_author=False, allowed_mentions=discord.AllowedMentions.none())
                else:
                    await ctx.reply(f"Random Konachan Image - {query}\n{image_url}", mention_author=False, allowed_mentions=discord.AllowedMentions.none())
        else:
            await ctx.reply("No results found.", mention_author=False)
    else:
        await ctx.reply("Failed to fetch response. Please try again later.", mention_author=False)
