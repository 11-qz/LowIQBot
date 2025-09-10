#---imports---
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

#---bot behaviour---
from keep_alive import keep_alive
keep_alive()
bot_prefs = ["!", ">_"] # bot prefixes are ! and >_ ; will respond to either
handler = logging.FileHandler(filename="discordbot.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True #enable ability to check message content
intents.members = True #enable ability to check member roles
bot = commands.Bot(command_prefix=bot_prefs, intents=intents)
bot.remove_command("help")  # remove default help command so I can make my own

#---Helpers and Data Management---
if not os.path.exists("discord_users.json"):                # check if discord_users.json exists, if not create it
    with open("discord_users.json", "w") as f:
        json.dump({"discord_data": []}, f, indent=4)
with open("discord_users.json", "r") as f:
    discord_user_data = json.load(f)


with open("bloons_tower_defense_6.json", "r") as f:         # load bloons tower defense 6 data
    bloons_data = json.load(f)

def normalize_bloon_name(raw: str) -> str:                  # normalize bloon names to match keys in json data
    parts = raw.split("-")
    return " ".join(
        [p.upper() if p in ["moab", "bfb", "zomg", "ddt", "bad"] else p.capitalize()
         for p in parts]
    )
        
def get_user(user_id, username):                            # get user data from json, if user does not exist create default user
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
                
def change_iq(user_id, amount):                             # change user iq by amount, positive or negative
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

def random_generator(discord_id, lowest_weight, highest_weight):
    if discord_id == 98556949745909760 or discord_id == 300447286801203210: # positively weighted random for users @11qz and @eightyonepoints ; chance to gain iq = 51.8181818%
        generated_random = random.randint(lowest_weight, highest_weight + 10)
        return generated_random 
    elif discord_id == 694286470365577258: # negatively weighted random for user @footballnut
        generated_random = random.randint(lowest_weight, highest_weight - 2)
        return generated_random
    else:
        generated_random = random.randint(lowest_weight, highest_weight)   
        return generated_random
                            
#---Bot Events---
@bot.event
async def on_message(message):
    if message.author == bot.user: # prevent bot from replying to itself
        return
    if "jews" in message.content.lower() and "fuck" in message.content.lower():
        await message.channel.send(f"{message.author.mention} not cool bro...")
    if "why" in message.content.lower():
        await message.channel.send(f"{message.author.mention} Why not?")

    await bot.process_commands(message)

@bot.event 
async def on_ready():                                     #Terminal output signifying that the bot is ready to be used.
    print(f"{bot.user.name} is online!")

#---Bot Commands---
#---Work Command---
@bot.command()
@commands.cooldown(1, 72000, commands.BucketType.user)  # 1 use per 72,000 seconds (20h) per user
async def work(ctx):
    discord_id = ctx.author.id
    user = get_user(ctx.author.id, ctx.author.name)
    if random_generator(discord_id, 1, 100) >= 52: 
        gain = random.randint(1, 3)
        iq = change_iq(discord_id, +gain)
        work_flavors_gain = [
        f"You completed a project ahead of schedule and impressed your boss. Gained **{gain} IQ points**.",
        f"You learned a new keyboard shortcut in Excel and saved hours of work. Gained **{gain} IQ points**.",
        f"You finally figured out how to fix the office printer without calling IT. Gained **{gain} IQ points**.",
        f"You streamlined a workflow and doubled team productivity. Gained **{gain} IQ points**.",
        f"You spotted an accounting error that saved the company money. Gained **{gain} IQ points**.",
        f"You mastered pivot tables and became the office **data wizard**. Gained **{gain} IQ points**.",
        f"You wrote clear meeting notes that everyone **actually** understood. Gained **{gain} IQ points**.",
        f"You solved a bug that had your coworkers stumped all week. Gained **{gain} IQ points**.",
        f"You discovered how to automate repetitive tasks with Python. Gained **{gain} IQ points**.",
        f"You organized your inbox and actually read all your incoming emails. Gained **{gain} IQ points**.",
        f"You gave a presentation without saying *\"um\"* even **once**. Gained **{gain} IQ points**.",
    ]
        await ctx.send(random.choice(work_flavors_gain) + f"\nCurrent IQ: {iq}")
    else:
        loss = random.randint(1, 3)
        iq = change_iq(discord_id, -loss)

        work_flavors_loss = [
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
        await ctx.send(random.choice(work_flavors_loss) + f"\nCurrent IQ: {iq}")

#---Slut Command---
@bot.command()
@commands.cooldown(1, 72000, commands.BucketType.user)  # 1 use per 72,000 seconds (20h) per user
async def slut(ctx):
    discord_id = ctx.author.id
    user = get_user(ctx.author.id, ctx.author.name)
    if random_generator(discord_id, 1, 100) >= 52: 
        gain = random.randint(1, 5)
        iq = change_iq(discord_id, +gain)
        slut_flavors_gain = [
        f"You sweet-talked your way into a VIP section and got free drinks all night. Gained **{gain} IQ points**.",
        f"You became \"friendly\" with the professor and were given a grade adjustment. Gained **{gain} IQ points**.",
        f"You turned a one-night stand into free breakfast and a cab home. Gained **{gain} IQ points**.",
        f"You sexted so poetically it was published in a romantic novel. Gained **{gain} IQ points**.",
        f"You went on three dates in one night and no one suspected a thing. Gained **{gain} IQ points**.",
        f"You seduced your way into skipping the line at the club. Gained **{gain} IQ points**.",
        f"Your dirty talk was so magnetically *salacious* that you were able to turn it into a TED Talk. Gained **{gain} IQ points**.",
        f"You took a nude so *perfectly* taken that it could hang in an art gallery without suspicion. Gained **{gain} IQ points**.",
        f"You scheduled hookups like back-to-back business meetings with zero overlap. Gained **{gain} IQ points**.",
        f"You convinced your hookup to do your homework and make you breakfast. Gained **{gain} IQ points**.",
        f"You turned a booty call into brunch reservations. Gained **{gain} IQ points**.",
    ]
        await ctx.send(random.choice(slut_flavors_gain) + f"\nCurrent IQ: {iq}")
    else:
        loss = random.randint(1, 5)
        iq = change_iq(ctx.author.id, -loss)

        slut_flavors_loss = [
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
        await ctx.send(random.choice(slut_flavors_loss) + f"\nCurrent IQ: {iq}")

#---Crime Command---
@bot.command()
@commands.cooldown(1, 72000, commands.BucketType.user)  # 1 use per 72,000 seconds (20h) per user
async def crime(ctx):
    discord_id = ctx.author.id
    user = get_user(ctx.author.id, ctx.author.name)
    if random_generator(discord_id, 1, 100) >= 52: 
        gain = random.randint(1, 10)
        iq = change_iq(discord_id, +gain)
        crime_flavors_gain = [
        f"You cracked a safe in world record time and with flawless precision. Gained **{gain} IQ points**.",
        f"You hacked into the OnlyFans framework, and now you can get free subscriptions without leaving a trace. Gained **{gain} IQ points**.",
        f"You forged a document so perfectly even the experts were fooled. Gained **{gain} IQ points**.",
        f"You planned a bank heist for months, and it went flawlessly. Gained **{gain} IQ points**.",
        f"You outsmarted a detective who was interrogating you. Gained **{gain} IQ points**.",
        f"You memorized a guard's schedule down to the most minute of details, and when he went to take a bathroom break, you stole **Ye's** gold-plated Lamborghini. Gained **{gain} IQ points**.",
        f"You hacked into the FBI database, released the Epstein files, and left zero evidence behind. Gained **{gain} IQ points**.",
        f"You picked a lock in under 30 seconds without leaving a scratch. Gained **{gain} IQ points**.",
        f"You tricked your rival into taking the fall for your scheme. Gained **{gain} IQ points**.",
        f"You disguised yourself and walked past security to \"relocate\" the Mona Lisa into a \"High-security vault\". Gained **{gain} IQ points**.",
        f"You got caught in a sting operation, but Alain Carlo Jayoma, using his words as a brush, masterfully painted the scene as **Entrapment**, and you got away without any charges.  Gained **{gain} IQ points**.",
    ]
        await ctx.send(random.choice(crime_flavors_gain) + f"\nCurrent IQ: {iq}")
    else:
        loss = random.randint(1, 10)
        iq = change_iq(ctx.author.id, -loss)

        crime_flavors_loss = [
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
        await ctx.send(random.choice(crime_flavors_loss) + f"\nCurrent IQ: {iq}")

#---Error Handler for Work, Slut, and Crime Commands---
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        hours, remainder = divmod(int(error.retry_after), 3600)
        minutes, _ = divmod(remainder, 60)
        await ctx.send(
            f"`{ctx.command.name.capitalize()}` has a cooldown of "
            f"{int(error.cooldown.per // 3600)} hours.\n"
            f"You need to wait **{hours}hours** **{minutes}minutes** before using this again."
        )
    else:
        raise error


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
    for i, user in enumerate(sorted_users[:10], start=1):
        discord_user = await bot.fetch_user(user["user_id"])
        top.append(f"**{i}. {discord_user.name}** {user['iqPoints']} IQ")

    await ctx.send(":trophy: **Top 10 Highest IQ Individuals** :trophy:\n" + "\n".join(top))

@bot.command()
async def rnumber(ctx, a: int, b: int):
    generated_random = random.randint(a, b)
    await ctx.send(f":game_die: Random number between {a} and {b}: **{generated_random}**")

@rnumber.error
async def rnumber_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Usage: \"!rnumber <min> <max>\"(You can also use >_ as the prefix)")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Usage: \"!rnumber <min> <max>\" both arguments <min> and <max> must be integers.")

@bot.command()
async def dice(ctx):
    die_random = random.randint(1, 6)
    await ctx.send(f"Your :game_die: landed on... **{die_random}**")

@bot.command()
async def d20(ctx):
    d20_random = random.randint(1, 20)
    await ctx.send(f"Your **Icosahedron** :game_die: landed on... **{d20_random}**")

@bot.command()
async def bloons(ctx, *args):
    if len(args) == 0:
        await ctx.send("Usage: \"!bloons [alt] <round|class|first> <argument>\"")
        return

    # detect mode
    if args[0].lower() == "alt":
        mode = "alternate"
        args = args[1:]
    else:
        mode = "standard"

    if len(args) == 0:
        await ctx.send("Usage: \"!bloons [alt] <round|class|first> <argument>\"")
        return

    subcommand = args[0].lower()
    arg = " ".join(args[1:]).lower() if len(args) > 1 else None

    # pick correct rounds
    if mode == "alternate":
        rounds = bloons_data["game_modes"]["alternate_bloon_rounds"]
    else:
        rounds = bloons_data["game_modes"]["standard_rounds"]

    # Round lookup
    if subcommand == "round":
        if arg and arg.isdigit():
            round_num = arg
            if round_num in rounds:
                bloons_in_round = rounds[round_num]
                formatted = ", ".join([f"{n} {b}'s" for b, n in bloons_in_round.items()])
                await ctx.send(f"{mode.capitalize()} round {round_num} has: {formatted}")
            else:
                await ctx.send(f"No data for {mode} round {round_num}.")
        else:
            await ctx.send(f"Usage: \"!bloons {mode} round <number>\"")

    # Class looukp
    elif subcommand == "class":
        if not arg:
            await ctx.send(f"Usage: \"!bloons {mode} class <bloon|property>\"")
            return

        bloon_name = normalize_bloon_name(arg)

        # Check if class property
        if arg in bloons_data["classes"]["class_properties"]:
            props = bloons_data["classes"]["class_properties"][arg]
            desc = props.get("description", "No description available.")
            note = props.get("note", "")
            await ctx.send(f"**{arg.capitalize()} property**\n{desc}\n{note}")
            return

        # Check if balloon
        if bloon_name in bloons_data["bloons"]:
            bloon_info = bloons_data["bloons"][bloon_name]
            rbe_info = bloon_info.get("RBE", "RBE data not available")

            msg = f"**{bloon_name}**\nRBE: {rbe_info}"

            if "spawns" in bloon_info:
                msg += f"\nSpawns on death: {bloon_info['spawns']}"
            if "properties" in bloon_info and bloon_info["properties"]:
                msg += f"\nProperties: {', '.join(bloon_info['properties'])}"
            if "note" in bloon_info and bloon_info["note"]:
                msg += f"\nNote: {bloon_info['note']}"

            await ctx.send(msg)
        else:
            await ctx.send(f"No class info for \"{arg}\"")

            # Check first appearance
    elif subcommand == "first":
        if not arg:
            await ctx.send(f"Usage: \"!bloons {mode} first <bloon>\"")
            return

        bloon_name = normalize_bloon_name(arg)

        found_round = None
        for rnd, bloon_dict in rounds.items():
            for name in bloon_dict.keys():
                
                if bloon_name == name or bloon_name in name:
                    found_round = rnd
                    break
            if found_round:
                break

        if found_round:
            await ctx.send(f"The **{bloon_name}** first appears on round {found_round} in the {mode} mode.")
        else:
            await ctx.send(f"No {bloon_name} found in {mode} mode.")



    else:
        await ctx.send("Unknown subcommand. Use **round**, **class**, or **first**.")

@bot.command(name="help", aliases=["commands"])
async def custom_help(ctx):
    help_text = (
        "Command prefixes `!` or `>_`\n"
        "**Available Commands:**\n"
        "**work** - Low risk and reward gamble for your IQ points by working.\n"
        "**slut** - Medium risk and reward gamble for your IQ points by partaking in promiscuous activities.\n"
        "**crime** - High risk and reward gamble for your IQ points by committing crimes.\n"
        "**balance** - Check your current IQ.\n"
        "**leaderboard** - Leader board of the top 10 highest IQ individuals.\n"
        "**rnumber <min> <max>** - Generate a random number between min and max.\n"
        "**dice** - Roll a standard 6-sided die.\n"
        "**d20** - Roll a 20-sided die.\n"
        "- **bloons [alt] <round|class|first> <argument>** - Get information about Bloons Tower Defense 6 rounds and balloons.\n"
        "   - **alt** is optional but tells the bot to show the balloons that appear within the alternate rounds mode.\n"
        "   - **round <number>**: Lists balloons in the specified round.\n"
        "   - **class <bloon|property>**: Provides details about a specific balloon or class property.\n"
        "   - **first <bloon>**: Shows the first round a specific balloon appears in.\n"
    )
    await ctx.send(help_text)

#run bot and log errors
bot.run(token, log_handler=handler, log_level=logging.DEBUG)




