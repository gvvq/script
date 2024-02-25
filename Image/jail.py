@bot.command()
async def jail(ctx):
    # Check if there are mentioned members in the message
    if not ctx.message.mentions:
        await ctx.send("You need to mention a user.")
        return

    # Get the first mentioned member
    mentioned_member = ctx.message.mentions[0]

    # Get the user's profile picture URL from the Member object
    user_pfp_url = mentioned_member.avatar if mentioned_member.avatar else mentioned_member.default_avatar

    # Construct the API URL
    api_url = f'https://api.popcat.xyz/jail?image={user_pfp_url}'

    # Make a request to the Popcat API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Send the modified image to the Discord channel
        await ctx.send(file=discord.File(io.BytesIO(response.content), 'jail_image.png'))
    else:
        await ctx.send(f"Failed to process the image. API status code: {response.status_code}")
