@bot.command(aliases=["hp"])
async def hostping(ctx, target):
    try:
        result = subprocess.Popen(['ping', target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = result.communicate(timeout=15)
        if output:
            await ctx.reply(f"```bat\n{output.decode('utf-8')}\n```", mention_author=False)
            result.terminate()
        elif error:
            await ctx.reply(f"```bat\n{error.decode('utf-8')}\n```", mention_author=False)
            result.terminate()
    except Exception as e:
        await ctx.reply(f"{str(e)}", allowed_mentions=discord.AllowedMentions.none(),mention_author=False)
        result.terminate()