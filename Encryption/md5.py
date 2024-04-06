@bot.command()
async def md5(ctx, *, text):
    import hashlib
    await ctx.message.delete()

    hashed_text = hashlib.md5(text.encode()).hexdigest()

    await ctx.send(f"```ini\n MD5 Hash: [{hashed_text}]\n```")