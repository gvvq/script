import psutil

@bot.command()
async def pckill(ctx, process_name):
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            proc.kill()
            await ctx.send(f"```ini\nProcess [ {process_name} ] killed successfully\n```")
            return
        pass