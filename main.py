import codecs
import discord
import os
import subprocess
client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '!sin':
        await message.channel.send("16進数の文字を入力してください")

        def check(command):
            return command.author == message.author
        cc = await client.wait_for("message", check=check)

        a = cc.content
        c = codecs.decode(a, 'hex_codec').decode('utf-8').format(a=a)
        print(c)
        await message.channel.send(f"```{c}```")
    if message.content == '!cos':
        await message.channel.send("文字を入力してください")

        def check(command):
            return command.author == message.author
        cc = await client.wait_for("message", check=check)

        a = cc.content
        command = 'echo -n ' + a + '| xxd -p'
        print(command)
        c = subprocess.check_output(command,shell=True)
        c = c.decode()
        c = c.replace("b'", '')
        c = c.replace("\n'", '')
        print(c)
        await message.channel.send(f"```{c}```")
if __name__ == "__main__":
    client.run(os.environ['MARK1_TOKEN'])