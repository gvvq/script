import requests

@bot.command()
async def imdb(ctx, *, movie_title: str):
    await ctx.message.delete()
    api_url = f"https://api.popcat.xyz/imdb?q={movie_title}"
    response = requests.get(api_url)
    data = response.json()

    if "title" in data:
        title = data.get("title", "Unknown")
        year = data.get("year", "Unknown")
        runtime = data.get("runtime", "Unknown")
        genres = data.get("genres", "Unknown")
        languages = data.get("languages", "Unknown")
        rated = data.get("rated", "Unknown")
        plot = data.get("plot", "Unknown")
        imdburl = data.get("imdburl", "Unknown")

        message = f"```ini\nTitle: [ {title} ]\nYear: [ {year} ]\nRuntime: [ {runtime} ]\nGenres: [ {genres} ]\nLanguages: [ {languages} ]\nRated: [ {rated} ]\nIMDB URL [ {imdburl} ]\nPlot: [ {plot} ]```"
    else:
        message = "No movie found with that title."

    await ctx.send(message)
