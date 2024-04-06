@bot.command()
async def adler32(ctx, *, text):
    import zlib
    await ctx.message.delete()

    hashed_text = zlib.adler32(text.encode())

    await ctx.send(f"```ini\n Adler-32 Hash: [{hashed_text}]\n```")