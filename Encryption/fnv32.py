@bot.command()
async def fnv32(ctx, *, text):
    import hashlib
    await ctx.message.delete()

    fnv_hash = hashlib.new('fnv1a_32')
    fnv_hash.update(text.encode())

    hashed_text = fnv_hash.hexdigest()

    await ctx.send(f"```ini\n FNV32 Hash: [{hashed_text}]\n```")