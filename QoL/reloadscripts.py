@bot.command(aliases=["reloadscript", "rs"])
async def reloadscripts(ctx):
    try:
        await ctx.message.delete()
        ui.update()
        await ctx.send("```ini\n [ Nighty ] has Restarted!```", delete_after=5)
        await ctx.message.delete()  
    except discord.NotFound:
        pass
