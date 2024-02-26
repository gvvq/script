@bot.command(aliases=["reloadscript", "rs"])
async def reloadscripts(ctx):
    await ctx.message.delete()
    ui.update()