import os
from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
import discord
from dotenv import load_dotenv
import random

def extract_poem(link):
    return str(link)

def get_all_links():
    poems = []
    url = 'https://rpo.library.utoronto.ca/poems'

    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(req.text, 'html.parser')

    for res in soup.findAll("a"):

        link = res.attrs.get("href")
        if link and '/poems/' in link:
            poems.append("https://rpo.library.utoronto.ca" + link)
    
    return extract_poem(poems[random.randrange(len(poems))])


class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!poem'):
            await message.channel.send("Here's a poem for you! <" + get_all_links() + ">")

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    client = MyClient()
    client.run(TOKEN)

if __name__ == '__main__':
    main()