from dotenv import load_dotenv
import os
import discord
from discord.ext import 

class VatrasBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if self.user.mentioned_in(message) and "join" in message.content.lower():
            if message.author.voice and message.author.voice.channel:
                voice_channel = message.author.voice.channel
                await voice_channel.connect()
            else:
                await message.channel.send("You are not in a voice channel!")



intents = discord.Intents.default()
intents.message_content = True

bot = VatrasBot(intents=intents)

def main():
    load_dotenv()
    env = os.getenv('BOT_KAY')
    bot.run(f"{env}")

if __name__ == "__main__":
    main()
