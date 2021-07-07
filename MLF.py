import tweepy
import discord
from discord.ext import commands
from datetime import datetime
import pytz
import io
from auth import *


client = commands.Bot(command_prefix=".")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
# Auth from auth.py

image = False


def tweet(message, im=False):
    if im:
        api.update_with_media(
            "image.png", str(message)
        )  # Sends message and attachemnt as tweet
    else:
        try:
            api.update_status(str(message))  # Sends message as tweet
        except:
            print("error lol")

    with io.open("tweets.txt", "a", encoding="utf-8") as f:
        f.write(f"{message}\n")  # Logs message to file (tweets.txt)
    print(f"Tweetade: '{message}'\n")  # Logs message to console


@client.event
async def on_message(message):
    global image

    date = datetime.now(pytz.timezone("Etc/GMT-2")).strftime(
        "%Y-%m-%d %H:%M:%S"
    )  # Time read by bot, in GMT-2 time zone

    mes = f"[{date}]\n*{str(message.author.roles[-1])}* {message.author}: ❝{message.content}❞"
    # [Time read by bot]
    # *\Highest Role\* \Message Author\: ❝\Message\❝

    for attachment in message.attachments:
        await attachment.save("image.png")
        image = True

    link_length = 51  # len("twitter.com/TemeroldFeed/status/xxxxxxxxxxxxxxxxxxx") = 51
    max_length = (
        280 - link_length
    )  # Max length of actual message, as the referred tweet takes link_length extra chars.

    if len(mes) >= max_length:  # The message (mes) doesn't fit in one tweet
        parts = []  # Empty to-be spliced up message (mes) array

        while mes != "":
            # Appends message (mes) to parts array, until it's entirely spliced up (with a length of max_length) into the array
            parts.append(mes[:max_length])
            mes = mes[max_length:]

        tweet(
            parts[0], image
        )  # Tweets first part without referring to latest item in timeline, including potential image
        del parts[
            0
        ]  # Deletes already tweeted part of message (mes) (first part, with no reffering)

        for i in parts:
            # Tweets every part of the message (mes) individually and refers to last post (of multiple tweet spliced-up message) (latest item in timeline)
            timeline = api.home_timeline()
            tweet(
                f"{i} https://twitter.com/TemeroldFeed/status/{timeline[0].id}", image
            )

    else:
        tweet(mes, image)  # Calls tweet function, including potential image

    image = False


client.run(discord_token)  # Runs Discord bot client
