import codecs
import discord
import os
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
        b = "codecs.decode(b'" + a + "', 'hex_cedec').decode('utf-8')"
        c = codecs.decode(a, 'hex_codec').decode('utf-8').format(a=a)
        print(c)
        await message.channel.send(f"```{c}```")
if __name__ == "__main__":
    client.run(os.environ['SIN_TOKEN'])