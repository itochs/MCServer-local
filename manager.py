import asyncio
import subprocess
import os
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
# intents.messages = True
client = discord.Client(intents=intents)
server_proccess = None

@client.event
# 起動時に動作する処理
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('やっほ！ログインしたよ！')
    print('/help でコマンドの確認ができるよ')


@client.event
# メッセージ受信時に動作する処理
async def on_message(message):
    # メッセージ送信者がBotだった場合は処理しない
    if message.author.bot:
        return

    # ヘルプの表示
    if message.content == '/help':
        await message.channel.send('/start : 起動')
        await message.channel.send('/stop : 停止')
        await message.channel.send('/minecraft-help : server help')
        return

    # await message.channel.send(message.content)
    global server_proccess
    # サーバーの起動
    if message.content == '/start':
        await message.channel.send('Server starting up...')
        await message.channel.send('※「start up」が表示されるまで他のコマンドを実行させないこと※')
        await message.channel.send('up .minecraft_server starting...')

        jar_directory_pass = '../minecraft_server/server-v1.19/'
        os.chdir(jar_directory_pass)
        # subprocess.call("'java -Xmx1024M -Xms1024M -jar server-v1.19.jar nogui &", shell=True)
        server_proccess = subprocess.Popen(
            ["java","-Xmx1024M","-Xms1024M","-jar","server-v1.19.jar","nogui"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE)
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        while server_proccess.poll() is None:
            stdout_message = server_proccess.stdout.readline().decode().strip()
            print('status:',server_proccess.poll(), stdout_message)

            if("Done" in stdout_message):
                break
        
        if server_proccess.poll() is None:
            await message.channel.send('start up')
            return
        
        await message.channel.send('start up error. kill proccess')
        server_proccess.kill()
        outs, errs = server_proccess.communicate()
        print(outs)
        print("-----")
        print(errs)

    # サーバーの停止
    if message.content == '/stop':
        if server_proccess is None:
            await message.channel.send("maybe server is not starting")
            return
        
        if server_proccess.poll() is not None:
            await message.channel.send("already server is stopping")
            return
        
        await message.channel.send('Server is stopping')
        await message.channel.send('※「down」が表示されるまで他のコマンドを実行させないこと※')

        try:
            print("try")
            outs, errs = server_proccess.communicate(input=b"stop", timeout=10)
            print("inside try:")
            outs_texts = outs.decode().strip().split("\n")
            print(outs_texts)
        except subprocess.TimeoutExpired:
            server_proccess.kill()
            outs, errs = server_proccess.communicate()
            print("inside except:")
            print(outs)
            print("-----")
            print(errs)

        await message.channel.send('down')
    
    if message.content == '/minecraft-help':
        try:
            print("try")
            outs, errs = server_proccess.communicate(input=b"help", timeout=10)
            print("inside try:")
            outs_texts = outs.decode().strip().split("\n")
            for log in outs_texts:
                print(log)
        except subprocess.TimeoutExpired:
            server_proccess.kill()
            outs, errs = server_proccess.communicate()
            print("inside except:")
            outs_texts = outs.decode().strip().split("\n")
            for log in outs_texts:
                print(log)
            print("-----")
            print(errs)




client.run(os.getenv("TOKEN"))
