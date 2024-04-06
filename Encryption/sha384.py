@bot.command()
async def sha384(ctx, *, text):
    import hashlib
    await ctx.message.delete()

    hashed_text = hashlib.sha384(text.encode()).hexdigest()

    await ctx.send(f"```ini\n SHA-384 Hash: [{hashed_text}]\n```")
