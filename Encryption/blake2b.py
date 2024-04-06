@bot.command()
async def blake2b(ctx, *, text):
    import hashlib
    await ctx.message.delete()

    hashed_text = hashlib.blake2b(text.encode()).hexdigest()

    await ctx.send(f"```ini\n BLAKE2b Hash: [{hashed_text}]\n```")