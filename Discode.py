import discord
from discord.ext import commands
from time import sleep
import random
from discord.player import FFmpegPCMAudio
from discord.utils import get



TOKEN = "MTE5MDkzOTEwMDUxNDEwMzM1Nw.GDwnsg.VF01XlYHTZOmKwlGhjKezz46LiYwwxw3BBC3AU"
CHANNELID = 739319238413779056 # チャンネルIDを貼り付け



client = discord.Client()
@client.event

async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content == '.help':
        await message.channel.send('.vc audio接続')
        await message.channel.send('.play 音声')
        await message.channel.send('.mute ミュート')
        await message.channel.send('.g o ')
        await message.channel.send('.random pon')
        

    #ランダム
    if message.content == '.random':
        await message.channel.send(random.randrange(100))
    if message.content == '.pon':
        janken = ["グー","チョキ","パー"]
        await message.channel.send(random.choice(janken))


        


#第五
    
    if message.content.startswith('g'):
        await message.channel.send('START')
        
        sleep(60)
        Tokushitsu = "鬼没"
        
        for i in range(3,0,-1):
            print(Tokushitsu + 'まで' + str(i))
            await message.channel.send(Tokushitsu + 'まで' + str(i))
            sleep(1)
                
    elif message.content.startswith('o'):
        await message.channel.send('鬼没おかわり')
        sleep(140)
        await message.channel.send('鬼没')



  # ボイスチャンネルに接続する
    if message.content == '.vc':
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return
  
        await message.author.voice.channel.connect()

        await message.channel.send("接続しました。")

    if message.content == ".play":
        if message.guild.voice_client is None:
            await message.channel.send("接続していません。")
            return
        message.guild.voice_client.playdiscord.FFmpegPCMAudio(f"C:\\Users\\kent\\Desktop\\jailbreak\\ffmpeg-master-latest-win64-gpl\\bin\\bgm.mp3")


    async def mute(ctx: commands.Context, member: discord.Member) -> None:

        if (role := get(member.roles, name="チャット制限")) is None: # ロールがサーバーに存在しない場合
        # ロールを作成
            role = await ctx.guild.create_role(
                name="チャット制限", # ロール名
                mentionable=True # メンションできるようにする
            )

        await member.add_roles(role) # メンバーにロールを付与
        await ctx.send(f"{member.mention} をチャット制限しました。")


#mute
    if message.content == ".mute":
        if message.author.guild_permissions.administrator:
            bot_vc = message.guild.me.voice.channel # botのいるボイスチャンネルを取得
            
            for member in bot_vc.members:
                await message.channel.send(member)
                await member.edit(mute=True) # チャンネルの各参加者をミュートする
        else:
            await message.channel.send("実行できません。")

    if message.content == ".nmute":
        if message.author.guild_permissions.administrator:
            bot_vc = message.guild.me.voice.channel # botのいるボイスチャンネルを取得
            
            for member in bot_vc.members:
                sleep(1)
                await message.channel.send(member)
                await member.edit(mute=False) # チャンネルの各参加者をミュートする
        else:
            await message.channel.send("実行できません。")




      
client.run(TOKEN)
