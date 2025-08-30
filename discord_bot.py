#imports
#-----------------------------------------------------------------------------------------------------------------------
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random
import asyncio
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
#-----------------------------------------------------------------------------------------------------------------------
#bot behaviour
#-----------------------------------------------------------------------------------------------------------------------
from keep_alive import keep_alive
keep_alive()
bot_prefs = ["!", ">_"] # bot prefixes are ! and >_ ; will respond to either
handler = logging.FileHandler(filename="discordbot.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True #enable ability to check message content
intents.members = True #enable ability to check member roles
bot = commands.Bot(command_prefix=bot_prefs, intents=intents)
# variable storage
#-----------------------------------------------------------------------------------------------------------------------
# Store user's points (resets on bot restart)
user_iq = {}
user_coin = {}
# snake role variable for custom commands
def change_iq(user_id, amount):
    user_iq[user_id] = user_iq.get(user_id, 0) + amount
    return user_iq[user_id]
def change_coin(user_id, amount):
    user_coin[user_id] = user_coin.get(user_id, 0) + amount
    return user_coin[user_id]
#-----------------------------------------------------------------------------------------------------------------------
#Terminal output signifying that the bot is ready to be used.
@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")

""" # join messages not needed
@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}.")
"""
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
# load cogs #BROKEN
#-----------------------------------------------------------------------------------------------------------------------
#bot.load_extension("cogs.general") #seems to be broken
#-----------------------------------------------------------------------------------------------------------------------
# bot commands
#-----------------------------------------------------------------------------------------------------------------------
@bot.command()
async def work(ctx):
    if random.random() < 0.05:
        iq = change_iq(ctx.author.id, 1)
        await ctx.send(
            f"✨ You had a sudden burst of intelligence and gained **+1 IQ**!\n"
            f"However, you then immediately googled \"how to boil water\" and forgot it again. Back to {iq - 1} IQ."
        )
        change_iq(ctx.author.id, -1)
        return

    loss = random.randint(1, 3)
    iq = change_iq(ctx.author.id, -loss)

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
    if random.random() < 0.05:
        iq = change_iq(ctx.author.id, 1)
        await ctx.send(f"🌟 You accidentally got away with crime and gained **+1 IQ**!\n"
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
        f"You hacked into the Pentagon, but forgot to turn off Caps Lock and gave yourself away. Lost **{loss} IQ points**.",
        f"You tried to pickpocket a police officer and got arrested. Lost **{loss} IQ points**.",
        f"You attempted a prison break, but tripped over your own shoelaces. Lost **{loss} IQ points**.",
        f"You counterfeited $100 bills, but printed them with Comic Sans. Lost **{loss} IQ points**.",
    ]

    await ctx.send(random.choice(crime_flavors) + f"\nCurrent IQ: {iq}")
    
@bot.command()
async def slut(ctx):
    if random.random() < 0.05:
        iq = change_iq(ctx.author.id, 1)
        await ctx.send(f"🌟 You got yourself a date, using Tinder, with a 9/10 masseuse **+1 IQ**!\n"
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
        f"You tried to pay your Uber driver with anothe currency... he gave you 1 star. Lost **{loss} IQ points**.",
        f"You tried to seduce a parking meter… but it fined you anyway. Lost **{loss} IQ points**.",
        f"You sent a suggestive selfie to the wrong group chat. Lost **{loss} IQ points**.",
    ]

    await ctx.send(random.choice(slut_flavors) + f"\nCurrent IQ: {iq}")

@bot.command()
async def balance(ctx):
    iq = user_iq.get(ctx.author.id, 0)
    await ctx.send(
        f"🧠 Your current IQ is **{iq}**."
    )

@bot.command()
async def leaderboard(ctx):
    if not user_iq:
        await ctx.send(
            "Nobody cared about UnbelievaBoat's :coin:'s enough to have lost Iq; very good."
            )
        return

    def get_iq(pair):
        return pair[1]

    sorted_users = sorted(user_iq.items(), key=get_iq)  # lowest IQ first
    top = []
    for i, (user_id, iq) in enumerate(sorted_users[:5], start=1):
        user = await bot.fetch_user(user_id)
        top.append(f"**{i}. {user.name}** {iq} IQ")
    await ctx.send(
        ":trophy: **Top 5 Dumbest Individuals** :trophy:\n" + "\n".join(top)
        )

''' # vestigial role assignment code
@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=snake_role)
     if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention}, you are now assigned to {snake_role}.")
    else:
        await ctx.send("Role does not exist yet.")
# role removal not needed
@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=snake_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention}, you have now had the {snake_role} removed from your account.")
    else:
        await ctx.send("Role does not exist yet.")
'''

@bot.command()
@commands.has_role("890370212002676766")
async def farmcoins(ctx):
    message = await ctx.send(
        "Okay, running coin_farm.py."
        )
    await asyncio.sleep(1)
    await message.edit(
    content="Okay, running coin_farm.py.."
    )
    await asyncio.sleep(1)
    await message.edit(
    content="Okay, running coin_farm.py..."
    )
    await asyncio.sleep(1)
    
    message = await ctx.send(
        "Downloading dependencies."
        )
    await message.edit(
    content="Downloading dependencies.."
    )
    await asyncio.sleep(1)
    await message.edit(
    content="Downloading dependencies..."
    )
    await asyncio.sleep(random.randint(1,3))
    await message.edit(
        content="bmuDerAsnioC.dll"
        )
    await asyncio.sleep(random.randint(1,5))
    await message.edit(
        content="tihslluBmodnar96.dll"
                       )
    await asyncio.sleep(random.randint(3,7))
    await message.edit(
        content="remraFnioCAsIsivarT.dll"
                       )
    await asyncio.sleep(random.randint(3,7))
    await message.edit(
        content="Downloads complete."
                       )
    await asyncio.sleep(2)
    await message.edit(
        content="Installing dependencies."
    )
    
    progress_message = await ctx.send("[░░░░░░░░░░] 0%")
    for i in range(1, 11):
        bar = "█" * i + "░" * (10 - i)
        await progress_message.edit(content=f"[{bar}] {i * 10}%")
        weighted_random_time = random.randint(1, 4)
        if weighted_random_time <= 3:
            await asyncio.sleep(random.uniform(0.01, 0.25))
        else:
            await asyncio.sleep(random.uniform(1.5, 3.5))
    message = await ctx.send(
        "Hijacking Bitcoin farms."
        )
    await asyncio.sleep(1)
    await message.edit(
        content="Hijacking Bitcoin farms.."
        )
    await asyncio.sleep(1)
    await message.edit(
        content="Hijacking Bitcoin farms..."
        )
    await asyncio.sleep(1)
    await message.edit(
        content="Injecting dll's."
        )
    await asyncio.sleep(1)
    await message.edit(
        content="Injecting dll's.."
        )
    await asyncio.sleep(1)
    await message.edit(
        content="Injecting dll's..."
        )
    await asyncio.sleep(1)
    await message.edit(
        content="Farming :coin:'s."
        )
    await asyncio.sleep(3)
    await message.edit(
        content="Farming :coin:'s.."
        )
    await asyncio.sleep(3)
    await message.edit(
        content="Farming :coin:'s..."
        )
    await asyncio.sleep(3)
    
    coin_change_amount = change_coin(ctx.author.id, random.randint(1337, 69696))
    
    await message.edit(
        content="Calculating total coins farmed."
        )
    await asyncio.sleep(1)
    await message.edit(
        content="Calculating total coins farmed.."
        )
    await asyncio.sleep(1)
    await message.edit(
        content="Calculating total coins farmed..."
        )
    await asyncio.sleep(1)
    await message.edit(
        content=f":chart_with_upwards_trend: coinFarm.py has farmed {coin_change_amount} :coin:'s."
        )
    await asyncio.sleep(5)
    await message.edit(
        content="Checking conversion rate between :coin:'s and UnbelievaBoat's :coin:'s."
        )
    await asyncio.sleep(5)
    await message.edit(
        content=f"You now have the equivalent of {coin_change_amount * (random.uniform(1.1, 2.2))} UnbelievaBoat :coin:'s."
        )
    await asyncio.sleep(3)
    
    message = await ctx.send(
        "Returning Hijacked Bitcoin farms."
        )
    await asyncio.sleep(random.randint(1,3))
    await message.edit(
        content="Eliminating digital footprint."
        )
    await asyncio.sleep(2)
    await message.edit(
        content="Closing coin_farm.py."
        )

@farmcoins.error
async def farm_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        message_taunt = await ctx.send(
            "Okay, running coin_farm.py."
            )
        await asyncio.sleep(1)
        await message_taunt.edit(
            content="Okay, running coin_farm.py.."
            )
        await asyncio.sleep(1)
        await message_taunt.edit(
            content="Okay, running coin_farm.py..."
            )
        await asyncio.sleep(1)
        await message_taunt.edit(
            content="JUST KIDDING BOZO!"
            )
        await asyncio.sleep(5)
        await message_taunt.edit(
            content="I CAN'T BELIEVE YOU FELL FOR THAT! :joy:"
            )
        await asyncio.sleep(5)
        await message_taunt.edit(
            content="NO COINS FOR YOU!!! :sob:"
            )
        await asyncio.sleep(5)
        await message_taunt.edit(
            content=":clown: <--- This is you right now! LMAO!!! :stuck_out_tongue_closed_eyes:"
            )
        await asyncio.sleep(5)
        await message_taunt.edit(
            content=":sunglasses: <--- You thought you were slick! :laughing:"
            )
        await asyncio.sleep(5)
        await message_taunt.edit(
            content=":zany_face: <--- Why do you look like this? :grimacing:"
            )
        await asyncio.sleep(5)
        await message_taunt.edit(
            content="Get a grip IDIOT!!! :rofl:"
            )
        await asyncio.sleep(5)
        await message_taunt.edit(
            content=":tired_face:"
            )
        await asyncio.sleep(5)
        await message_taunt.edit(
            content=":weary:"
            )
        await asyncio.sleep(5)
        await message_taunt.edit(
            content=":face_with_raised_eyebrow:"
            )
#-----------------------------------------------------------------------------------------------------------------------
#run bot and log errors
#-----------------------------------------------------------------------------------------------------------------------
bot.run(token, log_handler=handler, log_level=logging.DEBUG)




