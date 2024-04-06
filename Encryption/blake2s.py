@bot.command()
async def blake2s(ctx, *, text):
    import hashlib
    await ctx.message.delete()
    
    hashed_text = hashlib.blake2s(text.encode()).hexdigest()

    await ctx.send(f"```ini\n BLAKE2s Hash: [{hashed_text}]\n```")