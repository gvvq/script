@bot.command()
async def sha256(ctx, *, text):
    import hashlib
    await ctx.message.delete()

    hashed_text = hashlib.sha256(text.encode()).hexdigest()

    await ctx.send(f"```ini\n SHA-256 Hash: [{hashed_text}]\n```")