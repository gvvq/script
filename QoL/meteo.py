@bot.command()
async def meteo(ctx, location: str, days: int = 1):
    await ctx.message.delete()
    try:
        response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=8214f5a2223c42a084e233902240603&q={location}&days={days}")
        data = response.json()
        forecast_days = data['forecast']['forecastday']
        if len(forecast_days) < days: return await ctx.send("Error: Forecast data not available for all specified days.")
        weather_message = f"Weather forecast for {location} for the next {days} days:\n\n"
        for day in range(days):
            forecast_day = forecast_days[day]
            date, condition, current_temp_f, current_temp_c, max_temp_c, max_temp_f, min_temp_c, min_temp_f, humidity = forecast_day['date'], forecast_day['day']['condition']['text'], data['current']['temp_f'], data['current']['temp_c'], forecast_day['day']['maxtemp_c'], forecast_day['day']['maxtemp_f'], forecast_day['day']['mintemp_c'], forecast_day['day']['mintemp_f'], forecast_day['day']['avghumidity']
            wind_speed = forecast_day['day']['maxwind_kph'] * (1000 / 3600)
            day_message = (f"```ini\nDay [ {day+1} ] ({date}):\n"f"Condition: [{condition}]\n"f"Current Temp: [{current_temp_c}°C/{current_temp_f}°F]\n"f"Max Temp: [{max_temp_c}°C/{max_temp_f}°F]\n"f"Min Temp: [{min_temp_c}°C/{min_temp_f}°F]\n"f"Humidity: [{humidity}%]\n"f"Wind speed: [{wind_speed:.2f}m/s]\n```\n")
            weather_message += day_message
        await ctx.send(weather_message)
    except: pass