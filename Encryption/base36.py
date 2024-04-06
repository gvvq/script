@bot.command()
async def base36(ctx, mode: str, *, text):
    await ctx.message.delete()

    def base36encode(s):
        base36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if s == 0:
            return '0'
        neg = False
        if s < 0:
            neg = True
            s = -s
        encoded = ''
        while s > 0:
            s, i = divmod(s, 36)
            encoded = base36[i] + encoded
        if neg:
            encoded = '-' + encoded
        return encoded

    def base36decode(s):
        base36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s = s.upper()
        neg = False
        if s[0] == '-':
            neg = True
            s = s[1:]
        decoded = 0
        for char in s:
            try:
                i = base36.index(char)
            except ValueError:
                return None
            decoded = decoded * 36 + i
        if neg:
            decoded = -decoded
        return decoded

    if mode.lower() == "encrypt":
        try:
            encoded_text = base36encode(int(text))
            action = "Encoded"
        except ValueError:
            pass
            return
    elif mode.lower() == "decrypt":
        decoded_text = base36decode(text)
        if decoded_text is None:
            pass
            return
        else:
            action = "Decoded"
            encoded_text = decoded_text
    else:
        pass
        return

    await ctx.send(f"```ini\n {action}: [{encoded_text}]\n```")