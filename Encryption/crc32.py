@bot.command()
async def crc32(ctx, *, text):
    import zlib
    await ctx.message.delete()

    hashed_text = zlib.crc32(text.encode())

    await ctx.send(f"```ini\n CRC32 Hash: [{hashed_text}]\n```")
