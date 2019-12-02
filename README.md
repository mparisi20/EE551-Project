# EE-551: Engineering Python Final Project (Complete)

This is WeatherBot, a Discord Bot that provides daily weather forecasts for places all over the world. 

This Bot can connect to a Discord server and listen for particular commands:
- **!weather**: return today's forecast in Hoboken, NJ
- **!weather \<n\>**: return the n-day forecast for Hoboken, NJ. n's value must be between 1 and 7
- **!weather \<location\>**: return today's forecast for a given municipality
- **!weather \<n\> \<location\>**: return the n-day forecast for a given municipality. n's value must be between 1 and 7

This project demonstrates my knowledge of object-oriented and event-driven programming in Python. Discord's API, discord.py, 
has an object-oriented interface for instantiating both Clients and Bots. Once created, a Bot may respond to particular requests from human users through asynchronous
event handling. The Bot will respond to commands by retrieving weather data from [Dark Sky](https://darksky.net/dev), an advanced REST API that allows
for 1000 calls a day, free of charge.

By Max Parisi

Fall 2019
