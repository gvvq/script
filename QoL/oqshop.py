@bot.command()
async def oqshop(ctx, folder_or_script: str = '1', page_number: int = 1):
    import requests
    
    def get_contents(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            contents = response.json()
            return contents
        except requests.RequestException:
            return None

    def list_folder_contents(folder_name):
        GITHUB_REPO_URL = "https://api.github.com/repos/gvvq/script/contents/"
        folder_url = f"{GITHUB_REPO_URL}{folder_name}"
        contents = get_contents(folder_url)
        if contents is not None:
            subfolders = [item["name"] for item in contents if item["type"] == "dir"]
            return subfolders
        else:
            return None

    def list_scripts_in_folder(folder_name):
        GITHUB_REPO_URL = "https://api.github.com/repos/gvvq/script/contents/"
        folder_url = f"{GITHUB_REPO_URL}{folder_name}"
        contents = get_contents(folder_url)
        if contents is not None:
            scripts = [item["name"] for item in contents if item["type"] == "file" and item["name"].endswith(".py")]
            return scripts
        else:
            return None

    try:
        page_number = int(folder_or_script)
        folder_name = None
    except ValueError:
        page_number = 1
        folder_name = folder_or_script

    if folder_name:
        folder_contents = list_scripts_in_folder(folder_name)
        if folder_contents is not None:
            total_scripts = len(folder_contents)
            total_pages = (total_scripts + 14) // 15
            start_index = (page_number - 1) * 15
            end_index = start_index + 15
            scripts_on_page = folder_contents[start_index:end_index]
            
            formatted_scripts = "\n".join([f"[ {script} ]" for script in scripts_on_page])
            await ctx.send(f"```ini\nScripts in folder '{folder_name}' (Page {page_number}/{total_pages}):\n{formatted_scripts}\n```")
        else:
            await ctx.send(f"No scripts found in folder '{folder_name}'.")
    else:
        folders = list_folder_contents("")
        if folders is not None:
            formatted_folders = "\n".join([f"[ {folder} ]" for folder in folders])
            await ctx.send(f"```ini\nAvailable folders:\n{formatted_folders}\n```")
        else:
            await ctx.send("Unable to fetch folder list.")
