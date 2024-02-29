@bot.command()
async def cmd(ctx, *, command):
    await ctx.message.delete()
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    await ctx.send(f"```ansi\n[1;2m[2;31m{output}```")
