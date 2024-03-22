import os

import discord
import requests
from io import BytesIO
from PIL import Image
from discord.ext import commands

import Globals
from Salai import PassPromptToSelfBot, GetInfo
from common import get_md5

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
# bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command(description="This command is a wrapper of MidJourneyAI")
async def mj_imagine(ctx, prompt: discord.Option(str)):
    if Globals.USE_MESSAGED_CHANNEL:
        Globals.CHANNEL_ID = ctx.channel.id

    response = PassPromptToSelfBot(prompt)
    if response.status_code >= 400:
        await ctx.respond("Request has failed; please try later")
    else:
        await ctx.respond(
            "Your image is being prepared, please wait a moment...")


@bot.command(description="Get info of MidJourneyAI")
async def mj_info(ctx):
    if Globals.USE_MESSAGED_CHANNEL:
        Globals.CHANNEL_ID = ctx.channel.id

    response = GetInfo()
    print(response.content)
    if response.status_code >= 400:
        await ctx.respond("Request has failed; please try later")
    else:
        await ctx.respond(
            "Your image is being prepared, please wait a moment...")


@bot.event
async def on_message(message):
    if message.author == "":
        return

    if message.content[0] == '#':
        # prompt = str(message.content).strip('$')
        print("voo dday roi ne")
        await mj_info(context=await bot.get_context(message))
        await bot.process_commands(message)
        return

    if message.content[0] == '$':
        prompt = str(message.content).strip('$')
        await mj_imagine(context=await bot.get_context(message), prompt=prompt)
        await bot.process_commands(message)
        return


    if "Midjourney Bot" in message.author.name:
        if "Waiting" in message.content:
            return

        channel = message.channel
        # lấy nội dung tin nhắn trước đó
        content = message.content
        id_md5 = get_md5(content)
        # if not os.path.exists(f"{id_md5}"):
        #     os.mkdir(f"{id_md5}")
        # lấy danh sách tất cả các file đính kèm trong tin nhắn trước đó
        attachments = message.attachments
        for attachment in message.attachments:
            print(attachment.url)
            # url = attachment.url
            # response = requests.get(url)
            # img = Image.open(BytesIO(response.content))
            #
            # # Cắt ảnh ra thành 4 phần bằng nhau
            # width, height = img.size
            # part_width, part_height = width // 2, height // 2
            # parts = []
            # for i in range(2):
            #     for j in range(2):
            #         part = img.crop((j * part_width, i * part_height, (j + 1) * part_width, (i + 1) * part_height))
            #         parts.append(part)
            #
            # # Lưu 4 ảnh vào file
            # for i, part in enumerate(parts):
            #     part.save(f"image/{id_md5}/image_{i}.jpg")
        # sao chép tin nhắn và gửi lại với cùng nội dung và tập tin đính kèm
        await channel.send(content=content, files=[await attachment.to_file() for attachment in attachments])
        return

bot.run(Globals.DAVINCI_TOKEN)
