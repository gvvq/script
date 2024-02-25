@bot.command()
async def speechbubble(ctx, image_link: str, text: str = ""):
    # Handle Discord's CDN links
    if image_link.startswith("https://cdn.discordapp.com/"):
        # Extract the filename from the CDN link
        filename = image_link.split("/")[-1]
        # Construct a direct link to the image
        image_link = f"https://cdn.discordapp.com/attachments/{filename}"

    try:
        # Open the image from the link
        response = requests.get(image_link)
        response.raise_for_status()  # Raise an error for invalid response status
        image_bytes = BytesIO(response.content)
        base_image = Image.open(image_bytes).convert("RGBA")

        # Open the speech bubble image
        speech_bubble_url = "https://i.imgflip.com/6wb7ea.png"
        response = requests.get(speech_bubble_url)
        response.raise_for_status()  # Raise an error for invalid response status
        bubble_bytes = BytesIO(response.content)
        bubble_image = Image.open(bubble_bytes).convert("RGBA")

        # Resize the speech bubble image to fit the base image
        bubble_image = bubble_image.resize((base_image.width, base_image.height))

        # Composite the speech bubble image onto the base image
        final_image = Image.alpha_composite(base_image, bubble_image)

        # Convert image to bytes for sending
        final_image_bytes = BytesIO()
        final_image.save(final_image_bytes, format="PNG")
        final_image_bytes.seek(0)

        # Send the modified image as a file
        await ctx.send(file=discord.File(final_image_bytes, filename="speech_bubble.png"))

    except requests.exceptions.RequestException as e:
        await ctx.send(f"Failed to fetch the image: {e}")