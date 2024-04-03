import requests

@bot.command()
async def checkbtc(ctx, txid):
    await ctx.message.delete()
    url_tx = f"https://api.blockcypher.com/v1/btc/main/txs/{txid}"
    url_price = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    
    response_tx = requests.get(url_tx)
    response_price = requests.get(url_price)
    
    if response_tx.status_code == 200 and response_price.status_code == 200:
        data_tx = response_tx.json()
        data_price = response_price.json()
        
        value_satoshis = int(data_tx['total'])
        fee_satoshis = int(data_tx['fees'])
        confirmations = data_tx['confirmations']
        inputs_count = len(data_tx['inputs'])
        outputs_count = len(data_tx['outputs'])
        value_btc = value_satoshis / 100000000
        fee_btc = fee_satoshis / 100000000
        btc_usd_rate = data_price['bitcoin']['usd']
        value_usd = value_btc * btc_usd_rate
        fee_usd = fee_btc * btc_usd_rate
        
        message = f"```ini\nBTC Transaction [{txid}]\n"
        message += f"Value: [{value_btc:.8f} BTC] (${value_usd:.2f} USD)\n"
        message += f"Fees: [{fee_btc:.8f} BTC] (${fee_usd:.2f} USD)\n"
        message += f"Confirmations: [{confirmations}]\n"
        message += f"{inputs_count} input consumed, {outputs_count} outputs created.```"
        await ctx.send(message)
    else:
        await ctx.send("Transaction not found or invalid TXID or error retrieving exchange rate")
