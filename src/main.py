from dotenv import load_dotenv
import os
import discord

class VatrasBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.author == self.user:
            return

        await message.channel.send(f'You said: {message.content}')


def main():
    load_dotenv()
    env = os.getenv('BOT_KAY')

    intents = discord.Intents.default()
    intents.message_content = True

    client = VatrasBot(intents=intents)
    client.run(f"{env}")
    
if __name__ == "__main__":
    main()
