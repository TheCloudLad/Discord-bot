# Import Libary in to a discord bot 
import discord
from aiohttp import request
from discord.ext import commands
from colorama import Fore, Style, Back
import random
import datetime
#the body of code commands and code 
client = commands.Bot(command_prefix='!',intents = discord.Intents.all())



#on redy event in discord server!!!
@client.event
async def on_ready():
    print(Fore.CYAN+"""    
  _____  _                   _                 
 |  __ \(_)                 | |                
 | |  | |_ ___  ___ ___  ___| |__   ___  _ __  
 | |  | | / __|/ __/ _ \/ __| '_ \ / _ \| '_ \ 
 | |__| | \__ \ (_| (_) \__ \ | | | (_) | |_) |
 |_____/|_|___/\___\___/|___/_| |_|\___/| .__/ 
                                        | |    
                                        |_|    
""")
    print("Login as : " +Fore.RED + client.user.name)
    print(Fore.CYAN+"Bot id :"+Fore.RED +str(client.user.id))
    print()
    print("redy")
    print()
    synced = await client.tree.sync()
    print(synced)


#the Header Commands
@client.tree.command(name="header",description="Give you ifno about bot develober")
async def header(interaction:discord.Interaction):
    await interaction.response.send_message(content="```This bot is develop by Another#9999 you can join our discoshop community right now have fun! \n link :N/a ```")

# User ifno command 
@client.tree.command()
async def userinfo(interaction:discord.Interaction,member:discord.Member=None):
    if member == None:
        member = interaction.user
        roles = [role for role in member.roles]
    embed = discord.Embed(title="User info",description=f"User information of {member.name}",color=discord.Colour.green(),timestamp= datetime.datetime.utcnow())
    embed.set_thumbnail(url=member.avatar)
    embed.add_field(name ="ID",value=member.id)
    embed.add_field(name= "Name",value=f"{member.name}#{member.discriminator}")
    embed.add_field(name= "NickName",value=member.display_name)
    embed.add_field(name= "Status",value=member.status)
    embed.add_field(name= "Created At",value=member.created_at.strftime("%a, %d %b %Y %H:%M:%S"))
    embed.add_field(name= "Top Role",value=member.top_role)
    embed.add_field(name= "Messages",value="0")
    embed.add_field(name= "Is It bot?",value=member.bot)
    await interaction.response.send_message(embed=embed, ephemeral=True)
# Server info
@client.tree.command()
async def serverinfo(interaction:discord.Interaction):
    embed = discord.Embed(title="Server Info",description=f'Know more about {interaction.guild.name} Server💥',color=discord.Colour.blue(),timestamp= datetime.datetime.utcnow())
    embed.set_thumbnail(url=interaction.guild.icon)
    embed.add_field(name="Members",value=interaction.guild.member_count)
    embed.add_field(name="Channel",value=f'{len(interaction.guild.text_channels)} Text Channel || {len(interaction.guild.voice_channels)} Voice Channel')
    embed.add_field(name="Owner",value= interaction.guild.owner.mention)
    embed.add_field(name="Description",value= interaction.guild.description)
    embed.add_field(name="Server Create in ",value= interaction.guild.created_at.strftime("%a, %d %b %Y %H:%M:%S"))
    embed.add_field(name="Server Stickers",value= len(interaction.guild.stickers))
    embed.add_field(name="Server Bost bar" , value=interaction.guild.premium_progress_bar_enabled)
    embed.add_field(name="premium Level" , value=interaction.guild.premium_tier)
    embed.add_field(name="Subscription",value=interaction.guild.premium_subscription_count)
    await interaction.response.send_message(embed=embed)
#Invite
# Removed because cant find way to invite with / commands



# dice command take a random number of 1 to 6 
@client.tree.command(name="dice",description="picks a random number of dice")
async def dice(interaction:discord.Interaction,max:int):
    author = client.user.name
    number = random.randint(1,max)
    embed = discord.Embed(title="Dice", description="dice a number" ,color=discord.Colour.purple(),timestamp =  datetime.datetime.utcnow())
    embed.add_field(name="Value", value=number)
    embed.set_author(name=author)
    embed.set_thumbnail(url="https://nationaltoday.com/wp-content/uploads/2021/10/National-Dice-Day.jpg")
    await interaction.response.send_message(embed=embed)

#Random name for username
@client.tree.command(name="name",description="random shit")
async def name(interaction:discord.Interaction):
    uril = "https://api.codebazan.ir/name/?type=json"
    async with request("GET",uril, headers=[])as response:
        author = client.user.name
        data = await response.json()
        embed = discord.Embed(title="Random" ,description="",color=discord.Colour.green(),timestamp= datetime.datetime.utcnow())
        embed.add_field(name="Random name is ",value=data["result"])
        embed.set_author(name=author)
        embed.set_thumbnail(url="https://people.com/thmb/lxSDOxMNAA8aP8AyE0Xkztspr2Q=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(671x371:673x373)/shauna-rae-legal-name-change-082422-272fe74d53e34e59bae1eba1b5ba3a90.jpg")
        text = data["result"]
        await interaction.response.send_message(embed=embed)

# Stream Link 

@client.tree.command(name="streamlink",description="")
async def stream_link(interaction:discord.Interaction):
    author = client.user.name
    embed = discord.Embed(title="Stream Started", description="",color=discord.Colour.random(),timestamp= datetime.datetime.utcnow())
    embed.add_field(name="Live",value="https://gameria.tv/stream/91775435")
    embed.set_author(name=author)
    embed.set_thumbnail(url="https://static.cdn.asset.aparat.com/agf/liveCover-486745-7923-l.jpg")
    await interaction.response.send_message("@everyone",embed=embed)



@client.tree.command(name="test",description="")
async def test(interaction:discord.Interaction):
    author = client.user.name
    embed = discord.Embed(title="Stream Started", description="",color=discord.Colour.random(),timestamp= datetime.datetime.utcnow())
    embed.add_field(name="Live",value="https://gameria.tv/stream/91775435")
    embed.set_author(name=author)
    embed.set_thumbnail(url="https://static.cdn.asset.aparat.com/agf/liveCover-486745-7923-l.jpg")
    await interaction.response.send_message("@everyone",embed=embed)
# Token part and run a clinet side of bot -__-


client.run("token")
