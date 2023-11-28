import discord
from discord.ext import commands, tasks
from mcstatus import JavaServer

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот запущен!')
    # Запускаем задачу для обновления названия канала каждые 5 минут
    update_channel_name.start()

@tasks.loop(minutes=5)
async def update_channel_name():
    server = JavaServer("z19.joinserver.xyz", 25902)
    status = server.status()
    online_players = status.players.online

    # Получаем объект гильдии (сервера), на котором находится бот
    guild = bot.get_guild(1177906623189110784)  # Замените YOUR_GUILD_ID на ID своей гильдии

    # Получаем объект канала по его ID
    channel_id = 1178234961745150043  # Замените YOUR_CHANNEL_ID на ID канала
    channel = guild.get_channel(channel_id)

    # Изменяем название канала с использованием результата выполнения команды
    await channel.edit(name=f'minecraft-online-{online_players}')

@bot.command()
async def minecraft(ctx):
    server = JavaServer("z19.joinserver.xyz", 25902)
    status = server.status()
    online_players = status.players.online
    await ctx.send(f'Онлайн на сервере: {online_players}')

# Замените 'your_bot_token' на токен своего бота Discord
bot.run('MTE3ODIxNjAzNTU1MjM0MjAxNw.GrFgKh.o2x-pLXG-zIav6Kn6jdXelDwdEHny5dTmjW5Qo')