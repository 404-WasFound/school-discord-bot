# Imports
import discord, PyPDF2
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix="LBC ", description="Bot", intents=intents)
ids = [956399961279447090]

print("Loading💀")
@client.event
async def on_ready():
    print(f"Done🥳🥳")


@client.slash_command(guild_ids=ids, name="among", description="Have you ever played the hit game Among Us🤨🤨")
async def among(ctx):
	await ctx.respond("Among Us takes place in a space-themed setting where players look like colorful armless cartoon astronauts; however, since the release of 'The Skeld' spaceship, three other maps have been added in later years: the skyscraper 'MIRA HQ', the 'Polus' planetary station, and 'The Airship' (based on Infiltrating the Airship from the Henry Stickmin series, also developed by Innersloth). Each player takes on one of two roles—most are Crewmates, but a small number play Impostors—which does not alter their appearance. The goal of the Crewmates is to either identify and vote out the Impostors, or to complete all the tasks around the map; the goal of the Impostors is to covertly sabotage the mission either by killing the Crewmates before they complete all their tasks or by triggering a disaster that cannot be resolved.")


@client.slash_command(guild_ids=ids, name="dailynotices", description="Get the daily notices")
async def dailyNotices(ctx):

	#TODO: Make it so that you can get the PDF from a HTTP request then turn it into a file
	pdf = open("pdf.pdf", "rb")
	pdf_reader = PyPDF2.PdfFileReader(pdf)

	embed = discord.Embed(title="Daily Notices - Thursday, 24th March", description="Daily notices\nsome sports garbage\nmore sports garbage\nfree iphone16 pro max xl rose godld limited edition giveaway\nsports garbage", color=0x00577c)
	image1 = discord.File("./Long Bay Wavelength.png", filename="image.png")
	image2 = discord.File("./Long Bay Logo Small.png", filename="thumbnail.png")
	embed.set_image(url="attachment://image.png")
	embed.set_thumbnail(url="attachment://thumbnail.png")
	await ctx.send(file=image1, embed=embed)



#client.run("")