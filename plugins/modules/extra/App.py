import os
import requests
import pyrogram
import json
from info import LOG_CHANNEL
from pyrogram import Client as Koshik
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import os
import requests
from dotenv import load_dotenv
from requests.utils import requote_uri
from pyrogram import Client, filters, enums
from pyrogram.types import *

Bot = Client(
    "Google-Search-Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)


BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('✨ Made By ✨', url='https://t.me/nasrani_update')]])
A = """{} with user id:- {} used /git command."""

@Client.on_message(filters.command(["app", "apps"]))
async def getgithub(bot, message):
    if len(message.command) != 2:
        await message.reply_text("/github Username \n\n Like:- `/github hkrrish`", quote=True)
        return
    
    await message.reply_chat_action(enums.ChatAction.TYPING)
    k = await message.reply_text("**Processing...⏳**", quote=True)    
    un = message.text.split(None, 1)[1]
    URL = f'https://api.abirhasan.wtf/google/search/{un}'
    
    request = requests.get(URL)
    result = request.json()
    username = result['login']
    url = result['html_url']
    name = result['name']
    company = result['company']
    bio = result['bio']
    created_at = result['created_at']
    avatar_url = result['avatar_url']
    blog = result['blog']
    location = result['location']
    repositories = result['public_repos']
    followers = result['followers']
    following = result['following']
    capy = f"""**Info Of {name}**
**Username:** `{username}`
**Bio:** `{bio}`
**Profile Link:** [Click Here]({url})
**Company:** `{company}`
**Created On:** `{created_at}`
**Repositories:** `{repositories}`
**Blog:** `{blog}`
**Location:** `{location}`
**Followers:** `{followers}`
**Following:** `{following}`
**@KoshikKumar17**"""
    await message.reply_photo(photo=avatar_url, caption=capy, reply_markup=BUTTONS)
    await bot.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id)) 
    await k.delete()
