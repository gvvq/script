@bot.command()
async def advice(ctx):
    await ctx.message.delete()
    response = requests.get('https://api.adviceslip.com/advice')
    data = response.json()
    advice = data['slip']['advice']
    await ctx.send(f'```Advice: {advice}```')