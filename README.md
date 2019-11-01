# EE-551: Engineering Python Final Project

The goal of this project is to make a Discord Weather Bot. 

This Bot will be able to connect to a Discord server and listen for particular commands:
- **!weather**: return today's forecast in Hoboken, NJ
- **!weather \<n\>**: return the n-day forecast for Hoboken, NJ. n's value must be between 1 and 7
- **!weather \<location\>**: return today's forecast for a given municipality

In addition, the last two options above may be combined in one line to retrieve the n-day forecast for a given municipality.  

Also, I am hoping to add even more commands to the Weather Bot as I design the project, if I can think of more useful functionality.

This project will demonstrate my knowledge of object-oriented and event-driven programming in Python. Discord's API, discord.py, 
has an object-oriented interface for instantiating both Clients and Bots. Once created, a Bot may respond to particular requests from human users through asynchronous
event handling. The Bot will respond to commands by retrieving weather data from [Dark Sky](https://darksky.net/dev), an advanced REST API that allows
for 1000 calls a day, free of charge.



By Max Parisi

Fall 2019
