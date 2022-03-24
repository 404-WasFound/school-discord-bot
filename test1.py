import discord

class MyClient(discord.Client):

    async def on_ready(self):

        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):

        print("Message from {0.author}: {0.content}".format(message))

client = MyClient()
client.run("OTU2NDIyMDAzOTY1OTY0Mjk4.Yjv_Zw.3UZ5XhL4t59GSRTD08nhNSOm6N8")