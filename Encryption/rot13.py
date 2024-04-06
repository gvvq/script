@bot.command()
async def rot13(ctx, mode: str, *, text):
    await ctx.message.delete()
    def rot13_encrypt(text):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    encrypted_text += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
                else:
                    encrypted_text += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                encrypted_text += char
        return encrypted_text

    rot13_decrypt = rot13_encrypt

    if mode.lower() == "encrypt":
        result = rot13_encrypt(text)
        action = "Encrypted"
    elif mode.lower() == "decrypt":
        result = rot13_decrypt(text)
        action = "Decrypted"
    else:
        pass

    await ctx.send(f"```ini\n {action}: [{result}]\n```")