import base64
@bot.command()
async def ascii85(ctx, mode: str, *, text):
    await ctx.message.delete()

    if mode.lower() == "encode":
        encoded_text = base64.a85encode(text.encode()).decode()
        action = "Encoded"
    elif mode.lower() == "decode":
        try:
            decoded_text = base64.a85decode(text).decode()
            action = "Decoded"
        except:
            await ctx.send("Invalid ASCII85 encoded text!")
            return
    else:
        await ctx.send("Invalid mode! Please use 'encode' or 'decode'.")
        return

    await ctx.send(f"```ini\n {action}: [{encoded_text if mode.lower() == 'encode' else decoded_text}]\n```")