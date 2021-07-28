import discord
from keep_alive import keep_alive
from discord.ext import commands
from discord.utils import get
import asyncio

client = commands.Bot(command_prefix='.')
client.remove_command('help')

@client.event
async def on_ready():
    print('bot online')
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name="DM for .menfess", type=discord.ActivityType.watching))

@client.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == 869989189846962227:
        if str(payload.emoji) == '<:jokowi:869997850170384424>':
            channel = client.get_channel(869989189846962227)
            message = await channel.fetch_message(payload.message_id)
            reaction = get(message.reactions, emoji=payload.emoji)
            if reaction and reaction.count > 1:
                await message.delete()

@client.command()
async def menfess(ctx):
    if ctx.channel.type == discord.ChannelType.private:
        emoji = '<:jokowi:869997850170384424>'
        mbed = discord.Embed(
            title='Ketik menfess kamu',
            description='Jangan abuse sistem menfess atau di mute\n\nBot hanya support text'

        )
        mbed.set_footer(text='Kamu memiliki 10 detik untuk tulis menfess')
        demand = await ctx.send(embed=mbed)\

        try:
            msg = await client.wait_for(
                'message',
                timeout=10,
                check=lambda message: message.author == ctx.author and message.channel == ctx.channel

            )
            if not msg.attachments:
                channel = get(client.get_all_channels(), guild__name='bot playground', name='bot-cmds')
                mbed = discord.Embed(
                    title='Menfess Pacil',
                    description=f'{msg.content}',
                    color=discord.Colour.random()
                )
                mbed.set_footer(text='React jika menurutmu menfess ini tidak layak')
                message = await channel.send(embed=mbed)
                await demand.delete()
                await message.add_reaction(emoji)


            else:
                await ctx.author.send('Pastikan menfess nya hanya text saja ya', delete_after=5)

        except asyncio.TimeoutError:
            await ctx.send('Gak jadi ya?', delete_after=5)
            await demand.delete()

    else:
        await ctx.message.delete()
        await ctx.send('Baca DM bro', delete_after=5)
        await ctx.author.send('BOT hanya menerima menfess melalui DM', delete_after=10)

# Supaya bot gak mati
#keep_alive()
client.run('ODY5ODk2NDQ0MjIyNTA0OTYx.YQE4Mg.NhenqsxnYNFBB_EGegwRjdpVnxo')


