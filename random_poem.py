import os
# from bs4 import BeautifulSoup, SoupStrainer
import lxml.html
import urllib.request
# import httplib2
import discord
from dotenv import load_dotenv
import random

def get_content(link):
    return str(link)

def get_poem(sort_by):
    poems = []

    with urllib.request.urlopen('https://www.poetryfoundation.org/poems/browse#page=1&sort_by=' + sort_by + '&preview=1') as url:
        page = lxml.html.fromstring(url.read())

        for link in page.xpath('//a/@href'):
            poems.append(link)
    
    # http = httplib2.Http()
    # status, response = http.request('https://www.poetryfoundation.org/poems/browse#page=1&sort_by=' + sort_by + '&preview=1')
    # for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    #     poems.append(link['href'])
        # if link.has_key('href'):
        #     poems.append(link['href'])
    return get_content(poems[random.randrange(len(poems) - 1)])


class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        # if message.content.startswith('!random_poem'):
        if message.content.startswith('a'):
            sort_by = 'name'
            await message.channel.send("Here's a poem for you!")
            await message.channel.send(get_poem(sort_by))

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    client = MyClient()
    client.run(TOKEN)

if __name__ == '__main__':
    main()