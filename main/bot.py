from discord.ext import commands
# from datetime import datetime as dt
# from datetime import date as d
from file_getter import get_data

bot = commands.Bot(command_prefix="!")
split_char = "ƒ"

@bot.event
async def on_ready():

    print("Bot online")


@bot.command()
async def register(ctx, url):

    name = str(ctx.message.author)

    if "/" not in name and "\\" not in name:
    
        with open("users.txt", "r+") as file:

            full_data = file.read()
            data = full_data.splitlines()

            if name not in full_data:

                file.write(f"{name}{split_char}{url}\n")

                await ctx.send(f"`{name}` successfully registered")

@bot.command()
async def unregister(ctx):

    name = str(ctx.message.author)

    with open("users.txt", "r+") as file:

        full_data = file.read()
        data = full_data.splitlines()

        if name in full_data:

            file.truncate()

            for info in data:

                if name not in info:

                    file.write(f"{info}\n")

            await ctx.send(f"`{name}` successfully unregistered")

        else:

            await ctx.send(f"`{name}` failed to unregister")
            

@bot.command()
async def userlist(ctx):

    if str(ctx.message.author) == "404 Found#0744":

        with open("users.txt", "r") as file:

            data = file.read()

            await ctx.send(f"`{data}`")

@bot.command()
async def timetable(ctx):

    name = str(ctx.message.author)
    
    with open("users.txt", "r") as file:

        data = file.read().splitlines()

    tof = []

    for line in data:

        if name in line:

            link = line.split(split_char)[1]

            table = get_data(link, name)

            tof.append(True)

            await ctx.send(f"`{table}`")

        else: tof.append(False)

    if True not in tof:

        await ctx.send("Please register first")

bot.run("")