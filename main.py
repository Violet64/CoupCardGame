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
    description="Start a new game",
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
    if str(ctx.author.id) not in player_list:
        await ctx.send(f"{ctx.author.user.mention} joined")
        player_list.append(str(ctx.author.id))
    else:
        await ctx.send("You are already in the game")


@bot.command(
    name="income",
    description="Gain 1 coin",
)
async def gain_income(ctx: interactions.CommandContext):
    if game.check_turn(ctx.author.id):
        await ctx.send(f"{ctx.author.user.mention} gained 1 coin")
        game.income()
        game.next_turn()
    else:
        await ctx.send("It is not your turn yet")


@bot.command(
    type=interactions.ApplicationCommandType.USER,
    name="balance",
)
async def check_balance(ctx: interactions.CommandContext):
    await ctx.send(f"{ctx.target.user.username} has {game.get_balance(ctx.target.id)} coins")


bot.start()


