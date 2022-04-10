# This file is for handling interaction with the discord API through the interactions module
import interactions
from Coup import Coup
from asyncio import sleep

with open(f"bot_token.txt", "r") as file:
    for line in file:
        token = line

bot = interactions.Client(token=token)
game: Coup
player_list = []

@bot.command(
    name="start_game",
    description="fun for the whole familia",
    options=[
        interactions.Option(
            name="players",
            description="Number of players",
            type=interactions.OptionType.INTEGER,
            required=True,
            min_value=1,
            max_value=4
        ),
        interactions.Option(
            name="inquisitor",
            description="Add inquisitor y/n",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="ambassador",
            description="Use modified Ambassador y/n",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="contessa",
            description="Use modified Contessa y/n",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def new_game(ctx: interactions.CommandContext, players, inquisitor, ambassador, contessa):
    global game
    joined = 0
    join = interactions.Button(
        style=interactions.ButtonStyle.PRIMARY,
        label="Join game",
        custom_id="joined"
    )
    await ctx.send("", components=join)
    await sleep(10)
    game = Coup(players, inquisitor, ambassador, contessa, player_list)


@bot.component("joined")
async def join_game(ctx: interactions.CommandContext):
    await ctx.send(f"{ctx.author.user.mention} joined")
    player_list.append(ctx.author)

bot.start()


