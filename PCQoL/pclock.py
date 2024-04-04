@bot.command()
async def pclock(ctx):  
    os.system("rundll32.exe user32.dll,LockWorkStation")
    await ctx.send("```ini\nPC [ locked ] successfully\n```")


