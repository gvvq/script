import random, discord
from typing import Union

@bot.command(aliases=["df"])
async def dadfinder(ctx, target: Union[discord.Member, int] = None):
    if target is None:
        target = ctx.author
    else:
        target = target

    if random.random() < 0.5:
        await ctx.reply(f"**{str(target).strip('#0')}**'s dad could not be found..", mention_author=False)
    else:
        a = random.uniform(-180, 180); b = random.uniform(-90, 90); c = "E" if a >= 0 else "W"; d = "N" if b >= 0 else "S"; e = abs(a); f = abs(b); g = int(e); h = int((e - g) * 60); i = (e - g - h / 60) * 3600; j = int(f); k = int((f - j) * 60); l = (f - j - k / 60) * 3600
        await ctx.reply(f"**{str(target).strip('#0')}**'s dad found at {g}°{h}'{i:.2f}\"{c}, {j}°{k}'{l:.2f}\"{d}\nhttps://www.google.com/maps/place/{b},{a}", mention_author=False)
