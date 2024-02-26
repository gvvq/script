@bot.command()
async def calculate(ctx, *, equation):
        await ctx.message.delete()
        import math
        equation = equation.replace('pi', str(math.pi))
        equation = equation.replace('sqrt', 'math.sqrt')
        equation = equation.replace('^', '**')
        result = eval(equation)
        await ctx.send(f"```ansi\n[1;2m[2;31m{equation} = {result}```")
