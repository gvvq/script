@bot.command()
async def base32(ctx, mode: str, *, text):
    await ctx.message.delete()
    
    if mode.lower() == "encrypt":
        encoded_text = base64.b32encode(text.encode()).decode()
        action = "Encoded"
    elif mode.lower() == "decrypt":
        try:
            decoded_text = base64.b32decode(text.encode()).decode()
            action = "Decoded"
        except:
            await ctx.send("Invalid Base32 encoded text!")
            return
    else:
        await ctx.send("Invalid mode! Please use 'encrypt' or 'decrypt'.")
        return

    await ctx.send(f"```ini\n {action}: [{encoded_text if mode.lower() == 'encrypt' else decoded_text}]\n```")