@bot.command()
async def devmode(ctx, mode: str):
    if mode.lower() == "on":
        settings = await bot.user.fetch_settings()
        await ctx.message.delete()
        await settings.edit(developer_mode=True)
        await ctx.send("```ini\nEnabled [ Developer ] Mode```")
    elif mode.lower() == "off":
        settings = await bot.user.fetch_settings()
        await ctx.message.delete()
        await settings.edit(developer_mode=False)
        await ctx.send("```ini\nDisabled [ Developer ] Mode```")
    else:
        pass
