import requests

@bot.command()
async def checkltc(ctx, txid):
    await ctx.message.delete()
    url_tx = f"https://api.blockcypher.com/v1/ltc/main/txs/{txid}"
    url_price = "https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd"
    
    response_tx = requests.get(url_tx)
    response_price = requests.get(url_price)
    if response_tx.status_code == 200 and response_price.status_code == 200:
        data_tx = response_tx.json()
        data_price = response_price.json()
        value_litoshi = int(data_tx['total'])
        fee_litoshi = int(data_tx['fees'])
        confirmations = data_tx['confirmations']
        inputs_count = len(data_tx['inputs'])
        outputs_count = len(data_tx['outputs'])
        value_ltc = value_litoshi / 100000000
        fee_ltc = fee_litoshi / 100000000
        ltc_usd_rate = data_price['litecoin']['usd']
        value_usd = value_ltc * ltc_usd_rate
        fee_usd = fee_ltc * ltc_usd_rate
        message = f"```ini\nLTC Transaction [{txid}]\n"
        message += f"Value: [{value_ltc:.8f} LTC] (${value_usd:.2f} USD)\n"
        message += f"Fees: [{fee_ltc:.8f} LTC] (${fee_usd:.4f} USD)\n"
        message += f"Confirmations: [{confirmations}]\n"
        message += f"{inputs_count} input consumed, {outputs_count} outputs created.```"
        await ctx.send(message)
    else:
        await ctx.send("Transaction not found or invalid TXID or error retrieving exchange rate")
