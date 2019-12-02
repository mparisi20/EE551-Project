# Max Parisi
# EE 551 Python Project
# WeatherBot
# 12/2/19

import os
import random
import discord
from dotenv import load_dotenv

# using library from https://github.com/Detrous/darksky
from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather
from geopy.geocoders import Nominatim
from discord.ext import commands

# get environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
API_KEY = os.getend('API_KEY')

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
        
        
        
    await ctx.send('called !weather command')

def getNDayWeather(location, n):
    data = geolocator.geocode(location)
    lat = data.latitude
    long = data.longitude
    forecast = darksky.get_forecast(
        lat, long,
        extend=False,
        lang=languages.ENGLISH,
        units=units.AUTO,
        exclude=[weather.MINUTELY, weather.ALERTS]
    )
    
    # return a list of n DailyForecastItems
    
    for i in range(n):
        

    return dailyForecastItems

def weatherResponse(w):





"""
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
"""

bot.run(TOKEN)
