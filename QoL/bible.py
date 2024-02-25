@bot.command()
async def bible(ctx, book: str, chapter: int, verse: int):
    await ctx.message.delete()
    api_url = f'https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/en-asv/books/{book.lower()}/chapters/{chapter}/verses/{verse}.json'
    response = requests.get(api_url)
    verse_text = response.json()['text']
    await ctx.send(f"```ansi\n[1;2m[2;31m[{book} {chapter}:{verse} - {verse_text}]```")