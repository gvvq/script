import requests

@bot.command()
async def pokemon(ctx, name):
    await ctx.message.delete()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
    data = response.json()

    name = data['name']
    pokemon_id = data['id']
    base_experience = data['base_experience']
    types = [t['type']['name'] for t in data['types']]
    stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    sprite_url = data['sprites']['front_default']

    message = f"**Name:** {name.capitalize()}\n"
    message += f"**ID:** {pokemon_id}\n"
    message += f"**Base Experience:** {base_experience}\n"
    message += f"**Types:** {', '.join(types)}\n"
    message += "- **Stats:**\n"
    for stat, value in stats.items():
        message += f"- {stat.capitalize()}: {value}\n"

    await ctx.send(message)
    await ctx.send(sprite_url)
