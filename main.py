import re
import sqlite3
from discord.ext import commands, tasks
import discord
import requests
from bs4 import BeautifulSoup


TOKEN = "TOKEN"

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!",intents=intents)
colors = [1752220,1146986,3066993,2067276,3447003,2123412,10181046,7419530,15277667,11342935,15844367,12745742,15105570,11027200,15158332,10038562,9807270,9936031,8359053,12370112,3426654,2899536,16776960]
db = sqlite3.connect('database.sqlite')
cursor = db.cursor()

workingEmoji = "🟢"
updatingEmoji = "🔴"
testingEmoji = "🟣"

#on ready
@client.event
async def on_ready():
    print("Bot is ready")
    await client.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name = "Holders"))


@client.command()
async def start(ctx):
    url = "https://lavicheats.com/status-page/"
    test = requests.get(url)
    test2 = BeautifulSoup(test.content,"html.parser")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    data1 = requests.get(url,headers=headers)
    data = data1.text

    deltaApex = re.search("<a href=\"https://lavicheats.com/topic/10-apex-delta-private/\" rel=\"\">Delta</a> - <strong><span style=\"color:#2ecc71;\">(.*)</span></strong><span",data).group(1)

    print(data)


    inBuiltSpoofer = re.search("</span>In-built Spoofer - <span style=\"color:#cc3333;\"><strong>(.*)</strong></span><strong><span style",data).group(1)



    if deltaApex == "Working":
        overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(connect=False)}
        deltaApexChannel = await ctx.guild.create_voice_channel(f"Delta Apex: {deltaApex}{workingEmoji}",overwrites=overwrites)
        cursor.execute(f"UPDATE status SET deltaApex = 'Working'")
        db.commit()
        cursor.execute(f"UPDATE channels SET deltaApex = '{deltaApexChannel.id}'")
        db.commit()
    elif deltaApex == "Updating":
        overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(connect=False)}
        deltaApexChannel = await ctx.guild.create_voice_channel(f"Delta Apex: {deltaApex}{updatingEmoji}",overwrites=overwrites)
        cursor.execute(f"UPDATE status SET deltaApex = 'Updating'")
        db.commit()
        cursor.execute(f"UPDATE channels SET deltaApex = '{deltaApexChannel.id}'")
        db.commit()
    elif deltaApex == "Testing":
        overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(connect=False)}
        deltaApexChannel = await ctx.guild.create_voice_channel(f"Delta APEX: {deltaApex}{testingEmoji}",overwrites=overwrites)
        cursor.execute(f"UPDATE status SET deltaApex = 'Testing'")
        db.commit()
        cursor.execute(f"UPDATE channels SET deltaApex = '{deltaApexChannel.id}'")
        db.commit()


    if inBuiltSpoofer == "Working":
        overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(connect=False)}
        spooferChannel = await ctx.guild.create_voice_channel(f"Spoofer: {inBuiltSpoofer}{workingEmoji}",overwrites=overwrites)
        cursor.execute(f"UPDATE status SET inBuiltSpoofer = 'Working'")
        db.commit()
        cursor.execute(f"UPDATE channels SET inBuiltSpoofer = '{spooferChannel.id}'")
        db.commit()
    elif inBuiltSpoofer == "Updating":
        overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(connect=False)}
        spooferChannel = await ctx.guild.create_voice_channel(f"Spoofer: {inBuiltSpoofer}{updatingEmoji}",overwrites=overwrites)
        cursor.execute(f"UPDATE status SET inBuiltSpoofer = 'Updating'")
        db.commit()
        cursor.execute(f"UPDATE channels SET inBuiltSpoofer = '{spooferChannel.id}'")
        db.commit()
    elif inBuiltSpoofer == "Testing":
        overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(connect=False)}
        spooferChannel = await ctx.guild.create_voice_channel(f"Spoofer: {inBuiltSpoofer}{testingEmoji}",overwrites=overwrites)
        cursor.execute(f"UPDATE status SET inBuiltSpoofer = 'Testing'")
        db.commit()
        cursor.execute(f"UPDATE channels SET inBuiltSpoofer = '{spooferChannel.id}'")
        db.commit()


@tasks.loop(seconds=15)
async def check():
    try:
        cursor.execute(f"SELECT deltaApex FROM channels")
        deltaApexID = cursor.fetchone()[0]
        cursor.execute(f"SELECT inBuiltSpoofer FROM channels")
        spooferID = cursor.fetchone()[0]
        deltaApexChannel = await client.fetch_channel(int(deltaApexID))
        spooferChannel = await client.fetch_channel(int(spooferID))

        cursor.execute(f"SELECT deltaAPEX FROM status")
        DBstatusDelta = cursor.fetchone()[0]
        cursor.execute(f"SELECT  FROM status")
        DBstatusSpoofer = cursor.fetchone()[0]

        url = "https://lavicheats.com/status-page/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        data1 = requests.get(url, headers=headers)
        data = data1.text

        deltaApex1 = re.search(
            "<a href=\"https://lavicheats.com/topic/10-apex-delta-private/\" rel=\"\">Delta</a> - <strong><span style=\"color:#2ecc71;\">(.*)</span></strong><span",
            data).group(1)

        WEBdeltaApex = re.search("(.*)</span><", deltaApex1[:15]).group(1)

        WEBinBuiltSpoofer = re.search(";\"><strong>(.*)</strong></span><strong>", deltaApex1).group(1)

        if WEBdeltaApex == DBstatusDelta:
            pass
        else:
            if WEBdeltaApex == "Working":
                await deltaApexChannel.edit(name=f"Delta Apex: Working{workingEmoji}")
                cursor.execute(f"UPDATE status SET deltaApex = 'Working'")
                db.commit()
            elif WEBdeltaApex == "Updating":
                await deltaApexChannel.edit(name=f"Delta Apex: Updating{updatingEmoji}")
                cursor.execute(f"UPDATE status SET deltaApex = 'Updating'")
                db.commit()
            elif WEBdeltaApex == "Testing":
                await deltaApexChannel.edit(name=f"Delta Apex: Testing{testingEmoji}")
                cursor.execute(f"UPDATE status SET deltaApex = 'Testing'")
                db.commit()
        if WEBinBuiltSpoofer == DBstatusSpoofer:
            pass
        else:
            if WEBinBuiltSpoofer == "Working":
                await spooferChannel.edit(name=f"Spoofer: Working{workingEmoji}")
                cursor.execute(f"UPDATE status SET inBuiltSpoofer = 'Working'")
                db.commit()
            elif WEBinBuiltSpoofer == "Updating":
                await spooferChannel.edit(name=f"Spoofer: Updating{updatingEmoji}")
                cursor.execute(f"UPDATE status SET inBuiltSpoofer = 'Updating'")
                db.commit()
            elif WEBinBuiltSpoofer == "Testing":
                await spooferChannel.edit(name=f"Spoofer: Testing{testingEmoji}")
                cursor.execute(f"UPDATE status SET inBuiltSpoofer = 'Testing'")
                db.commit()
    except:
        pass



check.start()
client.run(TOKEN)
print(client.user.name)