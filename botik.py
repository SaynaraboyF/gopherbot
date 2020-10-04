import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import json
import requests
import re
import random
import time
import math
import time
import sqlite3
import os
import datetime
from discord import Game
from discord import Activity, ActivityType
from discord.utils import get
from bs4 import BeautifulSoup
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import pyowm
import wikipedia

PREFIX = '/'

client = commands.Bot(command_prefix=PREFIX)
client.remove_command('help')

@client.event
async def on_ready():
    print('Бот успешно запущен!')

    await client.change_presence(status=discord.Status.online, activity=discord.Game('/help ◉ /gopher'))


@client.event
async def on_member_join(member):
    channel = client.get_channel(761843798849355787)

    role = discord.utils.get( member.guild.roles, id = 744574892204359722)

    await member.add_roles(role)
    await channel.send(embed = discord.Embed(description = f'Пользователь {member.mention}, приземлятеся на сервер!', color = 0xFF69B4 ))


@client.command(pass_context=True)
async def мани(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

    author = ctx.message.author
    await ctx.send('Денег нет, но вы держитесь')


@client.command(pass_context=True)
async def бан(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

    author = ctx.message.author
    await ctx.send('Хочу сказать от всего админ состава, ты крутой!:sparkling_heart: ')


@client.command()
@commands.has_any_role(755527525547114558, 744464172665798686, 744464089270714378, 754737806106034326, 724716133550129194, 599218969580273669, 599218880224821258, 666745372856549421, 724560153927483433, 599221235745816598)
async def clear(ctx, amount: int = None):
    if amount is None:
        await ctx.send(embed=discord.Embed(description=f"{ctx.bot.command_prefix}{ctx.command} [количество сообщений]"),
                       delete_after=8)
        return
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(
        embed=discord.Embed(description=f':white_check_mark: Удалено {amount} сообщений', color=discord.Colour.green()),
        delete_after=8)


@client.command(pass_context=True)
@commands.has_any_role(755527525547114558, 744464172665798686, 744464089270714378, 754737806106034326, 724716133550129194, 599218969580273669, 599218880224821258, 666745372856549421, 724560153927483433, 599221235745816598)
async def kick(ctx, member: discord.Member, reason):
    emb = discord.Embed(title="Кик", colour=discord.Color.red())
    emb.add_field(name='Модератор', value=ctx.message.author.mention)
    emb.add_field(name='Нарушитель', value=member.mention)
    emb.add_field(name='Причина', value=reason, inline=False)
    emb.set_footer(text='© 2020 Все права защищены')
    await member.kick()
    await ctx.send(embed=emb)


@client.command()
@commands.has_any_role(755527525547114558, 744464172665798686, 744464089270714378, 754737806106034326, 724716133550129194, 599218969580273669, 599218880224821258, 666745372856549421, 724560153927483433, 599221235745816598)
async def ban(ctx, member: discord.Member, *, reason):
    await ctx.channel.purge(limit=1)

    emb = discord.Embed(title="Блокировка аккаунта.", color=0x09f12e0)

    emb.add_field(name='Модератор:', value=ctx.message.author.mention)
    emb.add_field(name='Нарушитель:', value=member.mention)
    emb.add_field(name='Причина:', value=reason)

    await member.ban()

    await ctx.send(embed=emb)


@client.command()
async def наташка(ctx):
    await ctx.channel.purge(limit=1)

    if ctx.author.id == 418786573283491853:
        await ctx.send(
            '<@538019617264762891> <@538019617264762891> <@538019617264762891> <@538019617264762891>. Быстро сюда!',
            delete_after=60)


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member: discord.Member):
    await ctx.channel.delete(limit=1)

    banned_users = await ctx.guild.bans()

    for ban_entery in banned_users:
        user = ban_entery.user

        await ctx.guild.unban(user)

        emb = discord.Embed(title="Разблокирован аккаунт.", color=0x13ab5a)

        emb.add_field(name='Модератор:', value=ctx.message.author.mention)

        await ctx.send(embed=emb)

        return


@client.command()
@commands.has_any_role(755527525547114558, 744464172665798686, 744464089270714378, 754737806106034326, 724716133550129194, 599218969580273669, 599218880224821258, 666745372856549421, 724560153927483433, 599221235745816598)
async def helpm(ctx, amount=1):
    emb = discord.Embed(title='Навигация по командам', colour = discord.Color.purple())
    await ctx.channel.purge(limit=amount)
    emb.add_field(name='{}clear'.format(PREFIX), value='Очистка чата', inline=False)
    emb.add_field(name='{}kick'.format(PREFIX), value='Кикнуть участника с сервера', inline=False)
    emb.add_field(name='{}mute'.format(PREFIX), value='Замутить участника', inline=False)
    emb.add_field(name='{}unmute'.format(PREFIX), value='Снять мут', inline=False)
    emb.add_field(name='{}ban'.format(PREFIX), value='Выдать пермаментный бан', inline=False)
    emb.add_field(name='{}tempban'.format(PREFIX), value='Выдать временный бан', inline=False)
    emb.add_field(name='{}unban'.format(PREFIX), value='Разбанить участника', inline=False)
    emb.add_field(name='{}slowmode'.format(PREFIX), value='Устнановить слоумод в канале', inline=False)

    await ctx.send(embed=emb)


@client.command(aliases=["тата"])
async def тати(ctx):
    await ctx.channel.purge(limit=1)

    if ctx.author.id == 228915819990482944:
        await ctx.send('**Вау, смотрите, какой тут красавчик**:hugging:, **я про него** <@228915819990482944>')


@client.command(aliases=["наташ"])
async def alaxomora(ctx):
    await ctx.channel.purge(limit=1)

    if ctx.author.id == 538019617264762891:
        await ctx.send('Верьте в себя, братья мои! Мы состоим под сильной угрозой.')


@client.command()
@commands.has_any_role(755527525547114558, 744464172665798686, 744464089270714378, 754737806106034326, 724716133550129194, 599218969580273669, 599218880224821258, 666745372856549421, 724560153927483433, 599221235745816598)
async def mute(ctx, member: discord.Member, time: int, reason):
    muterole = discord.utils.get(ctx.guild.roles, name='Mute')
    emb = discord.Embed(title="Мут", colour = discord.Color.red())
    emb.add_field(name='Модератор', value=ctx.message.author.mention)
    emb.add_field(name='Нарушитель', value=member.mention)
    emb.add_field(name='Причина', value=reason)
    emb.add_field(name='Время(Минут)', value=time)
    await member.add_roles(muterole)
    await ctx.send(embed=emb)
    await asyncio.sleep(time * 60)
    await member.remove_roles(muterole)


@client.command()
@commands.has_any_role(755527525547114558, 744464172665798686, 744464089270714378, 754737806106034326, 724716133550129194, 599218969580273669, 599218880224821258, 666745372856549421, 724560153927483433, 599221235745816598)
async def unmute(ctx, member: discord.Member):
    emb = discord.Embed(color=discord.Colour.green())
    await ctx.channel.purge(limit=1)

    mute_role = discord.utils.get(ctx.message.guild.roles, name='Mute')

    await member.remove_roles(mute_role)

    emb.set_author(name=member.name, icon_url=member.avatar_url)
    emb.add_field(name='Снята блокировка чата', value='Разблокирован чат участнику {}'.format(member.mention))

    await ctx.send(embed=emb)


@client.command(aliases=["Ботик"])
async def test(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('`Я тут, Я полон сил! Я готов к труду и обороне!`')


@client.command(pass_context=True)
async def лера(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

    author = ctx.message.author
    await ctx.send('Шладкая моя :heart: <@748207267626745896>')


@client.command()
async def gopher(ctx):
    await ctx.message.delete()

    emb = discord.Embed(title=f'Дискорд сервер бота. Для связи и помощи', url='https://discord.gg/pe3fN6s',
                        colour=discord.Colour.red())

    emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    emb.set_image(url='https://sun9-35.userapi.com/8xFgu0QXV8aN-3KdrMJA2bLeRB1Pnf3OsTM5tg/KR1NhgdUTvQ.jpg')

    await ctx.send(embed=emb)


@client.command()
async def invite(ctx):
    await ctx.message.delete()

    emb = discord.Embed(title='Пригласить меня на свой сервер.',
                        url='https://discord.com/api/oauth2/authorize?client_id=744274939497938985&permissions=8&scope=bot',
                        colour=discord.Colour.from_rgb(1, 1, 1))

    emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    emb.set_image(url='https://sun9-14.userapi.com/lndLuvVDAzE0Q9gO1Ol2UYZcJSwkR-tAlpMg5A/2jz5VllPi6I.jpg')

    await ctx.send(embed=emb)


@client.command()
async def панда(ctx):
    response = requests.get('https://some-random-api.ml/img/panda')
    jsoninf = json.loads(response.text)
    url = jsoninf['link']
    emb = discord.Embed(color=0xff9900)
    await ctx.channel.purge(limit=1)
    emb.set_image(url=url)
    await ctx.send(embed=emb)


@client.command()
async def лиса(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    jsoninf = json.loads(response.text)
    url = jsoninf['link']
    emb = discord.Embed(color=0xff9900)
    await ctx.channel.purge(limit=1)
    emb.set_image(url=url)
    await ctx.send(embed=emb)


@client.command()
@commands.has_permissions(administrator=True)
async def a_admin(ctx, member: discord.Member):
    emb = discord.Embed(title=f'Поздравляем! Вы были назначены на пост Администратора!', color=discord.Colour.orange())
    await ctx.channel.purge(limit=1)

    admin_role = discord.utils.get(ctx.message.guild.roles, name='--Администратор--')

    await member.add_roles(admin_role)

    emb.set_author(name=member.name, icon_url=member.avatar_url)

    await ctx.send(embed=emb)


@client.command()
@commands.has_permissions(administrator=True)
async def d_admin(ctx, member: discord.Member):
    emb = discord.Embed(title=f'К сожалению, вы были сняты с поста Администратора.', color=discord.Colour.green())
    await ctx.channel.purge(limit=1)

    admin_role = discord.utils.get(ctx.message.guild.roles, name='--Администратор--')

    await member.remove_roles(admin_role)

    emb.set_author(name=member.name, icon_url=member.avatar_url)

    await ctx.send(embed=emb)


@client.command()
async def bio(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    embed = discord.Embed(title=f"Информация о юзере \"{member.display_name}\":", color=discord.Color.green())
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.channel.purge(limit=1)

    desc = f"""
    **Общая информация**
        **Никнейм**: {member}
    """

    if member.status == discord.Status.online:
        desc += "**Статус:** :green_circle: Онлайн\n"

    elif member.status == discord.Status.idle:
        desc += "**Статус:** :crescent_moon: Не активен\n"

    elif member.status == discord.Status.do_not_disturb:
        desc += "**Статус:** :no_entry: Не беспокоить\n"

    else:
        desc += "**Статус:** :black_circle: Невидимый\n"

    desc += f"**Зашёл на сервер:** {member.joined_at.strftime('%d/%m/%Y %H:%M:%S')}\n"
    desc += f"**Когда регистрировался:** {member.created_at.strftime('%d/%m/%Y %H:%M:%S')}\n"

    embed.description = desc

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def a_moder(ctx, member: discord.Member):
    emb = discord.Embed(title=f'Поздравляем! Вы были назначены на пост Модератора чата.', color=discord.Colour.red())
    await ctx.channel.purge(limit=1)

    moder_role = discord.utils.get(ctx.message.guild.roles, name='--Модератор--')

    await member.add_roles(moder_role)

    emb.set_author(name=member.name, icon_url=member.avatar_url)

    await ctx.send(embed=emb)


@client.command()
@commands.has_permissions(administrator=True)
async def d_moder(ctx, member: discord.Member):
    emb = discord.Embed(title=f'К сожалению, вы были сняты с поста Модератора чата.', color=discord.Colour.purple())
    await ctx.channel.purge(limit=1)

    moder_role = discord.utils.get(ctx.message.guild.roles, name='--Модератор--')

    await member.remove_roles(moder_role)

    emb.set_author(name=member.name, icon_url=member.avatar_url)

    await ctx.send(embed=emb)


@client.command()
@commands.has_permissions(administrator=True)
async def ip_info(ctx, arg):
    response = requests.get(f'https://ipwhois.app/json/{arg}')
    all_info = ""
    parse_list = (
        ['ip'],
        ['continent'],
        ['city'],
        ['country_code'],
        ['country_capital'],
        ['country_phone'],
        ['region'],
        ['country'],
        ['timezone_gmt'],
        ['currency'],
        ['currency_code'],
        ['org'],
        ['timezone']
    )

    for par in parse_list:
        all_info.append(response.json(par) + '\n')

    user_flag = str(responce.json()['country_flag'])

    embed = discord.Embed(title='IP инфо', description=all_info)
    embed.set_thumbnail(icon_url=user_flag)
    await ctx.author.send(embed=embed)


@client.command()
async def search(ctx, *, question=None):
    if question is None:
        await ctx.send('Введите запрос!')
    else:
        await ctx.send('Подождите!')

        url = f'https://www.google.com/search?b-d&q=' + str(question).replace(' ', '+')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
            'accept': '*/*'
        }

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        items = soup.findAll('div', class_="rc")

        comps = []

        for item in items:
            comps.append({
                'link': item.find('a').get('href'),
                'title': item.find('h3', class_='LC20lb DKV0Md').get_text(strip=True)
            })
            await asyncio.sleep(3)

        emb = discord.Embed()

        counter = 0
        for comp in comps:
            counter += 1

            emb.add_field(
                name=f'[{counter}]    > #' + comp['title'],
                value='| ' + comp['link'],
                inline=False
            )

        emb.set_author(name='{}'.format(ctx.author), icon_url='{}'.format(ctx.author.avatar_url))
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            embed=discord.Embed(description=f'** {ctx.author.name}, данной команды не существует.**', color=0xff0000))
    else:
        embed = discord.Embed(
            title="Неизвестная ошибка!",
            colour=discord.colour.Color.from_rgb(255, 0, 0)
        )
        embed.add_field(name='Класс ошибки', value=str(error.__class__))
        embed.add_field(name='Сообщение', value=str(error))
        await ctx.bot.get_channel(759782113419067442).send(embed=embed)
        print(error.__class__, error)


@client.command()
async def help(ctx):
    emb = discord.Embed(title=f'Помощь | Все Модули', color=discord.Colour.orange())
    await ctx.channel.purge(limit=1)
    emb.add_field(name='Главные', value='``/help, /gopher``', inline=False)
    emb.add_field(name='Модерация', value='``Строго для модераторов! /helpm``', inline=False)
    emb.add_field(name='Весёлое', value='``/панда, /собачка, /птица, /лиса, /шар, /подмигнуть, /погладить, /обнять``',
                  inline=False)
    emb.add_field(name='О боте', value='``/бот, /проблемы, /ping``', inline=False)
    emb.add_field(name='Другое', value='``/search, /помощники``', inline=False)
    await ctx.send(embed=emb)


@client.command()
async def собачка(ctx):
    response = requests.get('https://some-random-api.ml/img/dog')
    jsoninf = json.loads(response.text)
    url = jsoninf['link']
    emb = discord.Embed(color=0xff9900)
    await ctx.channel.purge(limit=1)
    emb.set_image(url=url)
    emb.set_footer(text=ctx.author.name + ' | Все права защищены', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


@client.command()
async def птица(ctx):
    response = requests.get('https://some-random-api.ml/img/birb')
    jsoninf = json.loads(response.text)
    url = jsoninf['link']
    emb = discord.Embed(color=0xff9900)
    await ctx.channel.purge(limit=1)
    emb.set_image(url=url)
    emb.set_footer(text=ctx.author.name + ' | Все права защищены', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


# Магический шар
@client.command()
async def шар(ctx):
    answers = ["Ну не знаю я", "Знаки говорят Да", "Спроси еще разок", "Чуствую что это не правда", "Знаки говорят Нет"]
    ggg = random.choice(answers)
    await ctx.send(ggg)


# Помощники
@client.command()
async def помощники(ctx):
    emb = discord.Embed(title=f'Помощники в создании',
                        description='<@722757818683228240>, <@642614928808738818>, <@538019617264762891>, <@387226280330002433>.',
                        color=0xff0000)
    await ctx.channel.purge(limit=1)
    emb.set_footer(text=ctx.author.name + ' | Все права защищены', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 758052872637251587:  # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None
        if str(payload.emoji) == '🔐':  # Emoji для реакций
            role = guild.get_role(758053296966598876)  # ID Ролей для выдачи
        if role:
            member = guild.get_member(payload.user_id)
            if member:
                await member.add_roles(role)


@client.command()
async def проблемы(ctx):
    emb = discord.Embed(title=f'Проблемы бота',
                        description='\n\nБот включается очень редко, не стоит на хостинге, мало функций',
                        color=discord.Colour.orange())
    await ctx.channel.purge(limit=1)
    emb.set_footer(text=ctx.author.name + ' | Все права защищены', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


@client.command()
async def бот(ctx):
    emb = discord.Embed(title=f'Bot by who#9999',
                        description='`Меня зовут`\nGopher-Bot\n`Меня создал`\n<@418786573283491853>\n`Я написан на`\nязыке Python 3.8.6',
                        color=0xff0000)
    await ctx.channel.purge(limit=1)
    emb.set_footer(text=ctx.author.name + ' | Все права защищены', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


@client.event
async def on_message(message):  # trouble-free 24/7 event
    try:
        try:
            if isinstance(message.channel, discord.DMChannel):  # check on DM channel
                return
        except AttributeError:
            return
        await client.process_commands(message)  # continuation of command execution in case of on_message event
    except TypeError:
        return


@client.command()
@commands.has_permissions(administrator=True)
async def slowmode(ctx, delay: int):
    if delay == None:
        await ctx.send(
            embed=discord.Embed(title="Ошибка! :x:", description="Укажите время в секундах.Например: 21600(6ч)",
                                color=discord.Color.red()))
    await ctx.channel.edit(slowmode_delay=delay)
    await ctx.channel.purge(limit=1)
    await ctx.send(
        embed=discord.Embed(description=f"Успешно установлено задержку между сообщениями {delay} секунд на участника",
                            color=discord.Color.green(), delete_after=3))


@client.command()
async def w(ctx, *, text):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(
            'https://discordapp.com/api/webhooks/758063097091981422/x3dtiaMoqA4GhLaQvrHrAHyQizNutgp8tBHYC1Xn0JRCdhiKUCSMG6PCcnVgKkkS0lsV',
            adapter=AsyncWebhookAdapter(session))
        name = ctx.author.name
        avt = ctx.author.avatar_url
        await webhook.send(text, username=name, avatar_url=avt)


@client.command(aliases=['patt', 'Pat'])
async def погладить(ctx, member: discord.Member = None):
    response = requests.get('https://some-random-api.ml/animu/pat')
    json_data = json.loads(response.text)
    print(f'Команду погладить использовал пользователь {ctx.author.name}')
    embed = discord.Embed(title=f"{ctx.author} погладил`а {member}", colour=discord.Color.orange())
    await ctx.channel.purge(limit=1)
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@client.command(aliases=['hugg', 'Hug'])
async def обнять(ctx, member: discord.Member = None):
    response = requests.get('https://some-random-api.ml/animu/hug')
    json_data = json.loads(response.text)
    print(f'Команду обнять использовал пользователь {ctx.author.name}')
    embed = discord.Embed(title=f"{ctx.author} обнял'а {member}", color=0x2196F3)
    await ctx.channel.purge(limit=1)
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@client.command(aliases=['winkk', 'Wink'])
async def подмигнуть(ctx, member: discord.Member = None):
    response = requests.get('https://some-random-api.ml/animu/wink')
    json_data = json.loads(response.text)
    print(f'Команду подмигнуть использовал пользователь {ctx.author.name}')
    embed = discord.Embed(title=f"{ctx.author} подмигинул'a {member}", color=0x2196F3)
    await ctx.channel.purge(limit=1)
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    ping = client.latency
    ping_emoji = "🟩🔳🔳🔳🔳"
    await ctx.channel.purge(limit=1)

    ping_list = [
        {"ping": 0.10000000000000000, "emoji": "🟧🟩🔳🔳🔳"},
        {"ping": 0.15000000000000000, "emoji": "🟥🟧🟩🔳🔳"},
        {"ping": 0.20000000000000000, "emoji": "🟥🟥🟧🟩🔳"},
        {"ping": 0.25000000000000000, "emoji": "🟥🟥🟥🟧🟩"},
        {"ping": 0.30000000000000000, "emoji": "🟥🟥🟥🟥🟧"},
        {"ping": 0.35000000000000000, "emoji": "🟥🟥🟥🟥🟥"}]

    for ping_one in ping_list:
        if ping > ping_one["ping"]:
            ping_emoji = ping_one["emoji"]
            break

    message = await ctx.send("Пожалуйста, подождите. . .")
    await message.edit(content=f"Мой пинг: {ping_emoji} `{ping * 1000:.0f}ms`")


@client.command(name='weather', aliases=['погода'])
async def weather(ctx, city: str = None):
    if not city:
        await ctx.send(
            embed=discord.Embed(description="**Ты не указал город -_-**", colour=discord.Color.from_rgb(47, 49, 54)))
        await ctx.message.add_reaction("🔴")
    else:
        owm = pyowm.OWM('api key')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        w = observation.weather
        temp = w.temperature('celsius')["temp"]
        temp_max = w.temperature('celsius')["temp_max"]
        temp_min = w.temperature('celsius')["temp_min"]
        feels_like = w.temperature('celsius')["feels_like"]

        embed = discord.Embed(
            colour=discord.Color.from_rgb(47, 49, 54),
            description=f"**Погода в городе {city}**",
            timestamp=ctx.message.created_at
        )
        embed.set_thumbnail(
            url="https://avatars.mds.yandex.net/get-pdb/752643/d215f5fe-77ec-4923-aea7-b2184f2b6598/orig")
        embed.add_field(name="Температура", value=f"{temp} °С")
        embed.add_field(name="Ощущается как", value=f"{feels_like} °С")
        embed.add_field(name="Максимальная температура", value=f"{temp_max} °С")
        embed.add_field(name="Минимальная температура", value=f"{temp} °С")
        await ctx.send(embed=embed)
        await ctx.message.add_reaction("🟢")


@weather.error
async def weather_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(embed=discord.Embed(
            colour=discord.Color.from_rgb(47, 49, 54),
            description=f"**Город не найден**"
        ))
        await ctx.message.add_reaction("🔴")


@client.command()
async def avatar(ctx, member: discord.Member):
    if not member:
        member = ctx.author

    user = ctx.message.author if not member else member

    embed = discord.Embed(title=f'Аватар пользователя {member}', color=0xFF000)
    embed.set_image(url=user.avatar_url_as(format=None, size=4096))
    embed.set_author(icon_url='https://www.flaticon.com/premium-icon/icons/svg/2919/2919600.svg',
                     name='Участник | Аватар')
    embed.set_footer(text=f'{client.user.name} © 2020 | Все права защищены', icon_url=client.user.avatar_url)
    embed.timestamp = datetime.utcnow()

    await ctx.send(embed=embed)


# Репорт
@client.command()
async def report(ctx, *, arg):
    chanel = self.bot.get_channel(745875869100146699)
    if arg is None:
        await ctx.send(f'{ctx.author.mention}, вы не указали причину репорта!')
    else:
        emb = discord.Embed(title='**Успешно!**',
                            description=f'{ctx.author.mention}, вы успешно отправили репорт создателю бота!\nВ скором времени он свяжеться с вами!',
                            colour=discord.Color.green())
        await ctx.send(embed=emb)
        emb1 = discord.Embed(title='**Репорт!**', description=f'Репорт от: {ctx.author}\nСодержания: {arg}')
        await chanel.send(embed=emb1)


@client.command()
@commands.has_permissions(ban_members=True)
async def tempban(ctx, member: discord.Member = None, amount: int = None, tm: str = None, *, reason=None):
    if member is None:
        await ctx.send(f'{ctx.author.mention}, укажите пользователя которого хотите временно забанить!')
    elif reason is None:
        await ctx.send(f'{ctx.author.mention}, укажите причину бана!')
    elif amount is None:
        await ctx.send(f'{ctx.author.mention}, укажите время бана!')
    elif tm is None:
        await ctx.send('Укажите сколько будет действовать бан s = секунд, m = минут, h = часов, d = дней')
    else:
        emb = discord.Embed(title='**Бан!**',
                            description=f'**Администратор: {ctx.author.mention}\nНарушитель:{member.mention}\nПричина: {reason}\nВремя бана:{amount}{tm}!**',
                            colour=discord.Color.blue())
        await member.send(
            f'{member.mention}, вы были временно забанены на сервере: {ctx.guild.name}\nАдминистратор: {ctx.author.name}\nВремя: {amount}{tm}\nПричина: {reason}')
        await member.ban(reason=reason)
        await ctx.send(embed=emb)
        if tm == 's':
            await asyncio.sleep(amount)
        elif tm == 'm':
            await asyncio.sleep(amount * 60)
        elif tm == 'h':
            await asyncio.sleep(amount * 3600)
        elif tm == 'd':
            await asyncio.sleep(amount * 86400)
        emb1 = discord.Embed(title='**Разбан!**',
                             description=f'**У {member.mention}, прошло время бана!({amount}{tm})**',
                             colour=discord.Color.green())
        await ctx.guild.unban(member)
        await ctx.send(embed=emb1)


@client.command()
async def вовка(ctx):
    if ctx.author.id == 418786573283491853:
        await ctx.channel.purge(limit=1)
        await ctx.send(
            '<@591175705241452546> <@591175705241452546> <@591175705241452546> <@591175705241452546> <@591175705241452546> <@591175705241452546> <@591175705241452546>',
            delete_after=3)
    else:
        await ctx.send('Только Тоша может пинговать Вовку. 🐒', delete_after=5)

#Калькулятор
@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def калькулятор(ctx, amount: int = None, sho: str = None, amount2: int = None):
    if amount is None:
      await ctx.send('Введите 1 число')
    elif amount2 is None:
      await ctx.send('Введите 2 число')
    elif sho is None:
      await ctx.send('Введите действие: + - /')
    elif sho == '+':
      otv = amount + amount2
      emb1 = discord.Embed(title = '**Ответ!**', description = f'**Пример: {amount} {sho} {amount2}\nОтвет: {otv}**', colour = discord.Color.blue())
      await ctx.send(embed = emb1)
    elif sho == '-':
      otv = amount - amount2
      emb2 = discord.Embed(title = '**Ответ!**', description = f'**Пример: {amount} {sho} {amount2}\nОтвет: {otv}**', colour = discord.Color.blue())
      await ctx.send(embed = emb2)
    elif sho == '/':
      otv = amount / amount2
      emb3 = discord.Embed(title = '**Ответ!**', description = f'**Пример: {amount} {sho} {amount2}\nОтвет: {otv}**', colour = discord.Color.blue())
      await ctx.send(embed = emb3)
    else:
      await ctx.send('Вы ввели не правельный аргумент!')

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def emoji(ctx, emoji: discord.Emoji):
    
    e = discord.Embed(description = f"[Эмодзи]({emoji.url}) сервера {emoji}", color = discord.Colour.green())
    e.add_field(name = "Имя:", value = f"`{emoji.name}`")
    e.add_field(name = "Автор:", value = f"{(await ctx.guild.fetch_emoji(emoji.id)).user.mention}")
    e.add_field(name = "‎‎‎‎", value = "‎‎‎‎")
    e.add_field(name = "Время добавления:", value = f"`{emoji.created_at}`")
    e.add_field(name = "ID эмодзи:", value = f"`{emoji.id}`")
    e.add_field(name = "‎‎‎‎", value = "‎‎‎‎")
    e.set_thumbnail(url = f"{emoji.url}")
    await ctx.send(embed = e)

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
@commands.has_permissions(ban_members = True)
async def warn(ctx, member: discord.Member = None, reason = None):
        if member is None:
            await ctx.send("Введите пользователя которому хотите выдать варн!")
        elif member.id == 757919988202995712:
            await ctx.send("Вы не можите выполнить это действие с ботом!")
        elif reason is None:
            await ctx.send("Укажите причину!")
        else:
            cursor.execute("UPDATE users SET warn = warn + {} WHERE id = {} AND guild_id = {}".format(1, member.id, ctx.guild.id))
            connection.commit()
            emb = discord.Embed(title = "Удачно!", description = f'**Администратор {ctx.author.mention} выдал warn пользователю {member.mention}\nПричина: {reason}\nКоличество варнов: {cursor.execute("SELECT warn FROM users WHERE id = {} AND guild_id = {}".format(member.id, ctx.guild.id)).fetchone()[0]}**', colour = discord.Color.purple())
            await ctx.send(embed = emb)

            if cursor.execute("SELECT warn FROM users WHERE id = {} AND guild_id = {}".format(member.id, ctx.guild.id)).fetchone()[0] >= 3:
                await member.ban(reason = "3/3 warns|kindbot")
                emb1 = discord.Embed(title = "3/3", description = f"**У пользователя {member.mention}, было 3 варна и по этому он был забанен!**", colour = discord.Color.purple())
                await ctx.send(embed = emb1)

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
@commands.has_permissions(kick_members = True)
async def unwarn(ctx, member: discord.Member = None, *, arg = None):

        if member is None:
            await ctx.send(f'{ctx.author.mention}, укажите пользователя у которого хотите снять варн!')
            self.unwarn.reset_cooldown(ctx)
        else:
            if arg == "all":
                cursor.execute("UPDATE users SET warn = {} WHERE id = {} AND guild_id = {}".format(0, member.id, ctx.guild.id))
                connection.commit()
                emb = discord.Embed( title = '**Успешно!**', description = f'**У пользователя {member.mention}, были сняты все варн!**', colour = discord.Color.green())
                await ctx.send(embed = emb)
            elif arg is None:
                cursor.execute("UPDATE users SET warn = warn - {} WHERE id = {} AND guild_id = {}".format(1, member.id, ctx.guild.id))
                connection.commit()
                emb = discord.Embed( title = '**Успешно!**', description = f'**У пользователя {member.mention}, был снят варн!\nКол-во варнов: {cursor.execute("SELECT warn FROM users WHERE id = {} AND guild_id = {}".format(member.id, ctx.guild.id)).fetchone()[0]}**', colour = discord.Color.green())
                await ctx.send(embed = emb)

@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 761845992890040320:  # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None
        if str(payload.emoji) == '🐹':  # Emoji для реакций
            role = guild.get_role(744574667997577297)  # ID Ролей для выдачи
        if role:
            member = guild.get_member(payload.user_id)
            if member:
                await member.add_roles(role)

# Роль изменена
@client.event
async def on_guild_role_create(role):
    chanel = bot.get_channel(761852357519998987)
    async for entry in chanel.guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create):
        e = discord.Embed(colour=0x08dfab)
        e.set_author(name='Журнал аудита | создание роли', url=e.Empty,
                     icon_url='https://media.discordapp.net/attachments/689879530542071952/711588305506140241/verdict.png?width=407&height=407')
        e.add_field(name="Роль:", value=f"<@&{entry.target.id}>")
        e.add_field(name="ID роли:", value=f"{entry.target.id}")
        e.add_field(name="‎‎‎‎", value="‎‎‎‎", )
        e.add_field(name="Создал:", value=f"{entry.user.mention}")
        e.add_field(name="ID создавшего:", value=f"{entry.user.id}")
        e.add_field(name="‎‎‎‎", value="‎‎‎‎")
        await chanel.send(embed=e)
        return


# Роль удалена
@client.event
async def on_guild_role_delete(role):
    chanel = bot.get_channel(761852357519998987)
    async for entry in chanel.guild.audit_logs(action=discord.AuditLogAction.role_delete):
        e = discord.Embed(colour=0xe84444)
        e.set_author(name='Журнал аудита | удаление роли', url=e.Empty,
                     icon_url='https://media.discordapp.net/attachments/689879530542071952/711588305506140241/verdict.png?width=407&height=407')
        e.add_field(name="Роль:", value=f"{role.name}")
        e.add_field(name="ID роли:", value=f"{entry.target.id}")
        e.add_field(name="‎‎‎‎", value="‎‎‎‎", inline=False)
        e.add_field(name="Удалил:", value=f"{entry.user.mention}")
        e.add_field(name="ID удалившего:", value=f"{entry.user.id}")
        await chanel.send(embed=e)
        return


@client.command()
@commands.has_permissions(administrator=True)
async def a_fam(ctx, member: discord.Member):
	emb = discord.Embed(description=f'**Была выдана роль** <@&599220614800343073>', color=discord.Colour.purple())
	await ctx.channel.purge(limit=1)

	fam_role = discord.utils.get(ctx.message.guild.roles, name='🎓 Член семьи Red-Rock')

	await member.add_roles(fam_role)

	emb.set_author(name=member.name, icon_url=member.avatar_url)

	await ctx.send(embed=emb)

@client.command()
@commands.has_permissions(administrator=True)
async def d_fam(ctx, member: discord.Member):
	emb = discord.Embed(description=f'**Была снята роль** <@&599220614800343073>', color=discord.Colour.purple())
	await ctx.channel.purge(limit=1)

	fam_role = discord.utils.get(ctx.message.guild.roles, name='🎓 Член семьи Red-Rock')

	await member.remove_roles(fam_role)

	emb.set_author(name=member.name, icon_url=member.avatar_url)

	await ctx.send(embed=emb)                                     

token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
