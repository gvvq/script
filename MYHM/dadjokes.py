@bot.command(name='dadjoke', description="Send a random Dad Joke")
async def dadjoke(ctx):
    await ctx.message.delete()
    dad_jokes = [
    "I'm afraid for the calendar. Its days are numbered.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "What did the ocean say to the beach? Nothing, it just waved.",
    "Why couldn't the bicycle stand up by itself? It was two tired.",
    "How does a penguin build its house? Igloos it together.",
    "Why does the Norwegian navy have bar codes on the side of their ships? So when they come back to port they can Scandinavian!",
    "I made a playlist for Hiking, It has music from Peanuts, The Cranberries, and Eminem. I call it my Trail Mix."
]
    dad_joke = random.choice(dad_jokes)
    await ctx.send(dad_joke)

#MYHM 398620861634183188