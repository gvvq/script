@bot.command()
async def sha512(ctx, *, text):
    import hashlib
    await ctx.message.delete()

    hashed_text = hashlib.sha512(text.encode()).hexdigest()

    await ctx.send(f"```ini\n SHA-512 Hash: [{hashed_text}]\n```")