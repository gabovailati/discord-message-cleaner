import discord
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

# Define your bot's token here
TOKEN = os.getenv('DISCORD_TOKEN')

print(TOKEN)

# Define your input parameters
SERVER_NAME = 'mt5 server'
CHANNEL_NAME = 'general'

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
        
        # Find the server (guild) by name
        print(f'Getting server details: {SERVER_NAME}')
        guild = discord.utils.get(self.guilds, name=SERVER_NAME)
        if guild is None:
            print(f'Guild "{SERVER_NAME}" not found.')
            await self.close()
            return
        print(f'Server found: {guild}')
        
        print(f'Getting channel details: {CHANNEL_NAME}')
        # Find the channel by name
        channel = discord.utils.get(guild.text_channels, name=CHANNEL_NAME)
        if channel is None:
            print(f'Channel "{CHANNEL_NAME}" not found in guild "{SERVER_NAME}".')
            await self.close()
            return
        print(f'Server found: {CHANNEL_NAME}')
        
        # Fetch messages from the channel
        print(f'Fetching channel history')
        messages = [message async for message in channel.history(limit=None)]
        #messages = channel.history(limit=None)
        print(f'Fetching done: {messages}')
        
        # If there are messages, delete all except the latest one
        print(f'Iterating through messages')
        if messages:
            print(f'Total messages found: {len(messages)}')
            
            #print(f'Message id: {messages[0].id}')

            i = len(messages) - 1
            while (i > 0):
                await messages[i].delete()
                i -= 1

            print(f'Keeping message: {messages[0]}')
            print(f'Deleted {len(messages) - 1} messages, keeping the latest one.')
        else:
            print('No messages found in the channel.')
        
        # Close the bot connection
        await self.close()

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

# Run the client
client.run(TOKEN)
