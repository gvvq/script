@bot.command(name="downloader", usage='<url> <script or theme>', description="Download a theme or script file")
async def download(ctx, url: str, loc: str = 'scripts'):
    await ctx.message.delete()
    filename = url.split('/')[-1].replace(" ", "_")
    if loc == 'script':
        fileloc = 'scripts'
    elif loc == 'theme':
        fileloc = 'themes'
    else:
        await ctx.nighty_send("Invalid folder")
    data_path = getDataPath()
    file_path = os.path.join(data_path, fileloc , filename)

    r = requests.get(url, stream=True)
    if r.ok:
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
        if loc == 'theme':
            zip = ZipFile(filename)
            zip.extractall()
            await ctx.nighty_send(f"Downloaded file {filename}")
        else:
            await ctx.nighty_send(f"Downloaded file {filename}")
    else:
        await ctx.nighty_send("Downloaded failed!")

#MYHM 398620861634183188