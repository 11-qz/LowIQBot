import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random
import asyncio
load_dotenv()

@farmcoins.error
async def farm_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        message_taunt = await ctx.send(
        "Okay, running coinFarm.py."
        )
        await asyncio.sleep(1)
        await message_taunt.edit(
        content="Okay, running coinFarm.py.."
        )
        await asyncio.sleep(1)
        await message_taunt.edit(
        content="Okay, running coinFarm.py..."
        )
        await asyncio.sleep(1)
        
        #repeated periods new message function
        base_message2 = await ctx.send(
        "Hijacking Bitcoin farms"
        )
        for i in range(1, 3):
            new_message1 = f"{base_message2}{'.' * i}"
            await base_message2.edit(
            content=f"{new_message1}"
            )
            await asyncio.sleep(1)
            
    
        #repeated periods edit message function
        base_message4 = progress_message.edit(
        content="Calculating total coins farmed"
        )
        for i in range(1, 3):
            new_message1 = f"{base_message4}{'.' * i}"
            await base_message4.edit(
            content=f"{new_message1}"
            )
            await asyncio.sleep(1)
        
        
        
        