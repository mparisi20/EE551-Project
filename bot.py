# Max Parisi
# EE 551 Python Project
# WeatherBot
# 12/2/19

import os
import discord
from dotenv import load_dotenv

# using library from https://github.com/Detrous/darksky
from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units
from darksky.types import weather as ds_weather

from geopy.geocoders import Nominatim
from discord.ext import commands

# get environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
API_KEY = os.getenv('API_KEY')

# used to convert municipality names into longitude/latitude
geolocator = Nominatim(user_agent='WeatherBot')
# DarkSky Python wrapper
darksky = DarkSky(API_KEY)

# instantiate WeatherBot
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
   
@bot.command(name='weather', help='get the weather')
@commands.cooldown(1.0, 2.0, commands.BucketType.default)
async def weather(ctx, n=None, location=None):
    w = None # weather response object from Dark Sky
    if n is None and location is None:
        w = getNDayWeather('Hoboken', 1)
        await ctx.send(weatherResponse(w))
        return
    
    try:
        n = int(n)
    except:
        if location is not None:
            await ctx.send('n must be an integer')
            return
        else: # first parameter is the <location>
            location = n
            try:
                w = getNDayWeather(location, 1)
            except:
                await ctx.send('invalid location')
                return
            await ctx.send(weatherResponse(w))
            return
    if not (n >= 1 and n <= 7):
        await ctx.send('improper bound on n')
        return
    try:
        if location is None:
            w = getNDayWeather('Hoboken', n)
        else:
            w = getNDayWeather(location, n)
    except:
        await ctx.send('invalid location')
        return
    await ctx.send(weatherResponse(w))

def getNDayWeather(location, n):
    loc_data = geolocator.geocode(location)
    lat = loc_data.latitude
    long = loc_data.longitude
    forecast = darksky.get_forecast(
        lat, long,
        extend=False,
        lang=languages.ENGLISH,
        units=units.AUTO,
        exclude=[ds_weather.MINUTELY, 
                 ds_weather.ALERTS, 
                 ds_weather.HOURLY]
    )
    return {'loc': loc_data, 'days': n, 'data': forecast.daily.data[0:n]}

# expects the dictionary returned from getNDayWeather
def weatherResponse(w):
    response = f'Here is the **{w["days"]}-Day** forecast for **{w["loc"].address}**:\n\n'
    for item in w["data"]:
        response += 'Date: ' + item.time.strftime("%Y-%m-%d") + '\n'
        response += 'High: ' + "{:5.1f}".format(item.temperature_high) + '\n'
        response += 'Low: ' + "{:5.1f}".format(item.temperature_low) + '\n'
        response += "{:.0f}".format(item.precip_probability*100.0) + '% chance of ' + item.precip_type + '\n'
        response += '\n'
    return response

bot.run(TOKEN)
