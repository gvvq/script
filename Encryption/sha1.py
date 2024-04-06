@bot.command()
async def sha1(ctx, *, text):
    import hashlib
    await ctx.message.delete()

    hashed_text = hashlib.sha1(text.encode()).hexdigest()

    await ctx.send(f"```ini\n SHA-1 Hash: [{hashed_text}]\n```")
