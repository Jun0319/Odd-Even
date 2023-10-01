import discord

import config

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        activity = discord.Game("쭌 홀짝 ㄱㄱㄱ")
        await self.change_presence(status=discord.Status.online, activity=activity)

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content == "ㅎㅇ":
            await message.channel.send('나도 반가워!')



client = MyClient(intents=intents)
client.run(config.TOKEN)
