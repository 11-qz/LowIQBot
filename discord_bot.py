#imports
#-----------------------------------------------------------------------------------------------------------------------
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random
import asyncio
import json
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

#bot behaviour

from keep_alive import keep_alive
keep_alive()
bot_prefs = ["!", ">_"] # bot prefixes are ! and >_ ; will respond to either
handler = logging.FileHandler(filename="discordbot.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True #enable ability to check message content
intents.members = True #enable ability to check member roles
bot = commands.Bot(command_prefix=bot_prefs, intents=intents)
# variable storage
# check if discord_users.json exists, if not create it
if not os.path.exists("discord_users.json"):
    with open("discord_users.json", "w") as f:
        json.dump({"discord_data": []}, f, indent=4)
with open("discord_users.json", "r") as f:
    discord_user_data = json.load(f)
    
# load data and parse from or write to json file
def get_user(user_id, username):
    with open("discord_users.json", "r") as f:
        discord_user_data = json.load(f)
        
    for user in discord_user_data["discord_data"]:        
        if user["user_id"] == user_id:
            return user    
                
    default_user = {
            "user_id": user_id,
            "username": username,
            "iqPoints": 100,           
    }
    discord_user_data["discord_data"].append(default_user)
    with open("discord_users.json", "w") as f:
        json.dump(discord_user_data, f, indent=4)
        return default_user
        
        
def change_iq(user_id, amount):
    with open("discord_users.json", "r") as f:
        discord_user_data = json.load(f)
    for user in discord_user_data["discord_data"]:        
        if user["user_id"] == user_id:
            found_user = user
            found_user["iqPoints"] += amount
            break    
    with open("discord_users.json", "w") as f:
        json.dump(discord_user_data, f, indent=4)
    return found_user["iqPoints"]                    

#-----------------------------------------------------------------------------------------------------------------------
#Terminal output signifying that the bot is ready to be used.
@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")


#-----------------------------------------------------------------------------------------------------------------------
# bot events
#-----------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_message(message):
    if message.author == bot.user: # prevents bot replying to itself
        return
    if "jews" in message.content.lower() and "fuck" in message.content.lower():
        await message.channel.send(f"{message.author.mention} not cool bro...")
    if "why" in message.content.lower():
        await message.channel.send(f"{message.author.mention} Why not?")

    await bot.process_commands(message)
#-----------------------------------------------------------------------------------------------------------------------
# bot commands
#-----------------------------------------------------------------------------------------------------------------------
@bot.command()
async def work(ctx):
    discord_id = ctx.author.id
    user = get_user(ctx.author.id, ctx.author.name)
    if random.random() < 0.05:
        iq = change_iq(discord_id, 1)
        await ctx.send(
            f":sparkles: You had a sudden burst of intelligence and gained **+1 IQ**!\n"
            f"However, you then immediately googled \"how to boil water\" and forgot it again. Back to {iq - 1} IQ."
        )
        change_iq(discord_id, -1)
        return

    loss = random.randint(1, 3)
    iq = change_iq(discord_id, -loss)

    work_flavors = [
        f"You tried to staple together paperwork but stapled your hand instead. Lost **{loss} IQ points**.",
        f"You worked for so long without food that you had no choice but to eat your own hand to avoid starvation. Lost **{loss} IQ points**.",
        f"You dropped coffee on the only computer that holds the company backups. Lost **{loss} IQ points**.",
        f"You tried to focus on your work, but got distracted by Tik Tok. Lost **{loss} IQ points**.",
        f"You tried to write an important email, but spent 20 minutes deciding between 'Kind regards' and 'Best regards.' Lost **{loss} IQ points**.",
        f"You opened Excel to be productive, but ended up just coloring the cells like a digital art project. Lost **{loss} IQ points**.",
        f"You joined a Zoom call but forgot to mute your mic while yelling at your cat. Lost **{loss} IQ points**.",
        f"You tried to finish your report, but Microsoft Word auto-corrected 'their' to 'they're' and you didn't notice. Lost **{loss} IQ points**.",
        f"You meant to do actual work, but spent an hour reorganizing your desktop icons instead. Lost **{loss} IQ points**.",
        f"You tried to fix the printer jam and somehow installed a virus onto the thermostat. Lost **{loss} IQ points**.",
        f"You spent 30 minutes looking for a pen, then realized you were holding it the entire time. Lost **{loss} IQ points**.",
    ]

    await ctx.send(random.choice(work_flavors) + f"\nCurrent IQ: {iq}")


@bot.command()
async def crime(ctx):
    discord_id = ctx.author.id
    user = get_user(ctx.author.id, ctx.author.name)
    if random.random() < 0.05:
        iq = change_iq(ctx.author.id, 1)
        await ctx.send(f":detective: You accidentally got away with crime and gained **+1 IQ**!\n"
                       f"Then you bragged about it on Facebook... Back to {iq - 1} IQ.")
        change_iq(ctx.author.id, -1)  # immediately take it away
        return

    loss = random.randint(1, 5)
    iq = change_iq(ctx.author.id, -loss)

    crime_flavors = [
        f"You tried to make a deposit to your bank--with Monopoly money. Lost **{loss} IQ points**.",
        f"You committed tax fraud--against yourself. Lost **{loss} IQ points**.",
        f"You tried to steal an energy drink from a corner store, but you forgot to wear a mask. Lost **{loss} IQ points**.",
        f"You successfully commited a heist on a bank, but then you took selfies with the money... Lost **{loss} IQ points**.",
        f"You tried to rob a jewelry store, but got stuck in the revolving door. Lost **{loss} IQ points**.",
        f"You robbed a house committed arson to hide the evidence, but turns out it was your own house... Lost **{loss} IQ points**.",
        f"You stole a car, but couldn't drive stick shift. Lost **{loss} IQ points**.",
        f"You hacked into the Pentagon, but forgot to turn on your VPN and gave yourself away. Lost **{loss} IQ points**.",
        f"You tried to pickpocket a police officer and got arrested. Lost **{loss} IQ points**.",
        f"You attempted a prison break, but tripped over your own shoelaces. Lost **{loss} IQ points**.",
        f"You counterfeited $100 bills, but printed them with Comic Sans. Lost **{loss} IQ points**.",
    ]

    await ctx.send(random.choice(crime_flavors) + f"\nCurrent IQ: {iq}")
    
@bot.command()
async def slut(ctx):
    discord_id = ctx.author.id
    user = get_user(ctx.author.id, ctx.author.name)
    if random.random() < 0.05:
        iq = change_iq(ctx.author.id, 1)
        await ctx.send(f":sparkles: You got yourself a date, using Tinder, with a 9/10 masseuse **+1 IQ**!\n"
                       f"Then you bragged about it to your friends--and they told you it was a chat bot. Back to {iq - 1} IQ.")
        change_iq(ctx.author.id, -1)  # immediately take it away
        return

    loss = random.randint(1, 5)
    iq = change_iq(ctx.author.id, -loss)

    slut_flavors = [
        f"You flirted with a vending machine… it took your money and gave you nothing back. Lost **{loss} IQ points**.",
        f"You winked at a stop sign… traffic didn't stop for you. Lost **{loss} IQ points**.",
        f"You tried to convince a police officer to hire you for prostitution… Lost **{loss} IQ points**.",
        f"You gave your phone number to a telemarketer… Lost **{loss} IQ points**.",
        f"You tried to flirt with the pizza delivery guy, but he only wanted the payment for the pizza. Lost **{loss} IQ points**.",
        f"You blew a kiss at a mannequin in the mall… people stared, but the mannequin didn't. Lost **{loss} IQ points**.",
        f"You slid into a scammer's DMs… and sent them gas money. Lost **{loss} IQ points**.",
        f"You flirted with Siri… but she just said 'I don't understand.' Lost **{loss} IQ points**.",
        f"You gave your OnlyFans link to the IT help desk… now your account is suspended. Lost **{loss} IQ points**.",
        f"You tried to pay your Uber driver with another currency... he gave you 1 star. Lost **{loss} IQ points**.",
        f"You tried to seduce a parking meter… but it fined you anyway. Lost **{loss} IQ points**.",
        f"You sent a suggestive selfie to the wrong group chat. Lost **{loss} IQ points**.",
    ]

    await ctx.send(random.choice(slut_flavors) + f"\nCurrent IQ: {iq}")

@bot.command()
async def balance(ctx):
    user = get_user(ctx.author.id, ctx.author.name)
    await ctx.send(f":brain: Your current IQ is **{user['iqPoints']}**.")

@bot.command()
async def leaderboard(ctx):
    with open("discord_users.json", "r") as f:
        discord_user_data = json.load(f)

    if not discord_user_data["discord_data"]:
        await ctx.send("No IQ data.")
        return


    sorted_users = sorted(discord_user_data["discord_data"], key=lambda u: u["iqPoints"], reverse=True)

    top = []
    for i, user in enumerate(sorted_users[:5], start=1):
        discord_user = await bot.fetch_user(user["user_id"])
        top.append(f"**{i}. {discord_user.name}** {user['iqPoints']} IQ")

    await ctx.send(":trophy: **Top 5 Highest IQ Individuals** :trophy:\n" + "\n".join(top))

@bot.command()
async def rnumber(ctx, a: int, b: int):
    generated_random = random.randint(a, b)
    await ctx.send(f":game_die: Random number between {a} and {b}: **{generated_random}**")

@rnumber.error
async def randnum_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Usage: \"!randnum <min> <max>\"(You can also use >_ as the prefix)")

#-----------------------------------------------------------------------------------------------------------------------
#run bot and log errors
#-----------------------------------------------------------------------------------------------------------------------
bot.run(token, log_handler=handler, log_level=logging.DEBUG)




