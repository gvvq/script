@bot.command()
async def pcrestart(ctx):
    await ctx.send("```ini\nAre you sure you want to restart the PC? [ (yes/no) ]\n```")
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["yes", "no"]
    try:
        msg = await bot.wait_for("message", timeout=30, check=check)
    except asyncio.TimeoutError:
        return await ctx.send("```ini\n[ Response timed out Restart cancelled ]\n```")

    if msg.content.lower() == "no":
        return await ctx.send("```ini\n[ Restart cancelled ]\n```")
    elif msg.content.lower() == "yes":
        os.system("shutdown /r /t 1")
        await ctx.send("```ini\n [ Restarting the PC... ]\n```")
