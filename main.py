import discord
from discord.ext import commands, tasks
from discord import embeds
import os
import random
import asyncio
from asyncio import gather

#Prefix to call the bot
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.playing, name="Rock, Paper Scissors!"))
  print('I have power!')


#Users must type "!play {choice} to play"
@client.command()
async def play(ctx, message):
    answer = message.lower()
    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)
    if answer not in choices:
        await ctx.send("Please enter a valid choice")
    else:
            if bot_choice == "rock" and answer == "paper":
                embedVar = discord.Embed(title="You win!", description=f"**mello's choice:** {bot_choice}\n **your choice:** {answer}.", color=discord.Color.blurple())
                await ctx.send(embed=embedVar)

            elif bot_choice == "rock" and answer == "scissors":
                embedVar = discord.Embed(title="mello wins!", description=f"**mello's choice:** {bot_choice}\n **your choice:** {answer}.", color=discord.Color.blurple())
                await ctx.send(embed=embedVar)

            elif bot_choice == "paper" and answer == "rock":
                embedVar = discord.Embed(title="mello wins!", description=f"**mello's choice:** {bot_choice}\n **your choice:** {answer}.", color=discord.Color.blurple())
                await ctx.send(embed=embedVar)
                
            elif bot_choice == "paper" and answer == "scissors":
                embedVar = discord.Embed(title="You win!", description=f"**mello's choice:** {bot_choice}\n **your choice:** {answer}.", color=discord.Color.blurple())
                await ctx.send(embed=embedVar)

            elif bot_choice == "scissors" and answer == "rock":
                embedVar = discord.Embed(title="You win!", description=f"**mello's choice:** {bot_choice}\n **your choice:** {answer}.", color=discord.Color.blurple())
                await ctx.send(embed=embedVar)

            elif bot_choice == "scissors" and answer == "paper":
                embedVar = discord.Embed(title="mello wins!", description=f"**mello's choice:** {bot_choice}\n **your choice:** {answer}.", color=discord.Color.blurple())
                await ctx.send(embed=embedVar)

            else:
                embedVar = discord.Embed(title="It's a draw!", description=f"**mello's choice:** {bot_choice}\n **your choice:** {answer}.", color=discord.Color.blurple())
                await ctx.send(embed=embedVar)


client.run('OTMwMjg4NTM3NDU3Mjk1NDAy.Ydzstw.dR9V2GCbM6FAH_6YFe0bjqYhYJc')

