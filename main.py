import codecs
import discod

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
        codecs.decode(b'{a}', 'hex_codec').decode('utf-8')