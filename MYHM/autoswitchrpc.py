@bot.command(name="autoswitchrpc", description="Auto switch between rpc profiles")
async def autoswitchrpc(ctx):
    global switch_rpc_profiles
    switch_rpc_profiles = True
    await ctx.message.delete()
    await ctx.nighty_send(title="Auto switch RPC profiles", content="Started cycling between rpc profiles every 15 minutes")
    while switch_rpc_profiles:
        rpc_data = json.load(open(getRPCPath(), 'r'))
        for profile in rpc_data['profiles']:
            profile_name = list(profile.keys())[0]
            rpc_data['active_profile'] = profile_name
            json.dump(rpc_data, open(getRPCPath(), "w"), indent=2)
            await asyncio.sleep(15*60)