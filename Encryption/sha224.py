@bot.command()
async def sha224(ctx, *, text):
    import hashlib
    await ctx.message.delete()

    hashed_text = hashlib.sha224(text.encode()).hexdigest()

    await ctx.send(f"```ini\n SHA-224 Hash: [{hashed_text}]\n```")