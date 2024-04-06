@bot.command()
async def base85(ctx, mode: str, *, text):
    await ctx.message.delete()

    if mode.lower() == "encrypt":
        encoded_text = base64.b85encode(text.encode()).decode()
        action = "Encrypted"
    elif mode.lower() == "decrypt":
        try:
            decoded_text = base64.b85decode(text).decode()
            action = "Decrypted"
        except:
            await ctx.send("Invalid Base85 encoded text!")
            return
    else:
        await ctx.send("Invalid mode! Please use 'encrypt' or 'decrypt'.")
        return

    await ctx.send(f"```ini\n {action}: [{encoded_text if mode.lower() == 'encrypt' else decoded_text}]\n```")