@bot.command(aliases=['eval', 'exec'])
async def execute(ctx, *, code):
    try:
        local_vars = {'ctx': ctx}
        global_vars = {'bot': bot}
        exec(f'async def __temp_func(ctx): \n {code}', global_vars, local_vars)
        await asyncio.gather(local_vars['__temp_func'](ctx))
    except Exception as e:
        await ctx.reply(str(e), allowed_mentions=discord.AllowedMentions.none(), mention_author=False)