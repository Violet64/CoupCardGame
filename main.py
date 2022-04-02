#This file is for handling interaction with the discord API through the interactions module
import interactions
from getpass import getuser

with open(f"C:\\Users\\{getuser()}\\Documents\\bot_token.txt", "r") as file:
    for line in file:
        token = line

bot = interactions.Client(token=token)


bot.start()
