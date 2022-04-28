import discord

hello_words = ["!привет", "!hello", "!hi", "!бонжур", "!добрый день"]
menu_words = ["!меню", "!menu"]
qof_words = ["!качество жизни", "!qof"]
crime_words = ["!преступность", "!crime"]
health_words = ["!здравоохранение", "!health care"]
rent_words = ["!аренда", "!rent"]
bye_words = ["!до встречи", "!пока", "!bye"]

client = discord.Client()

@client.event
async def on_ready():
    print('Вы залогинились как {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    msg_list = msg.split()

        #ПРИВЕТСТВИЕ
    find_hello_words = False
    for item in hello_words:
        if msg.find(item) >= 0:
            find_hello_words = True
    if (find_hello_words):
        await message.channel.send(f' { message.author.mention } Добрый день!')

        #МЕНЮ
    find_menu_words = False
    for item in menu_words:
        if msg.find(item) >= 0:
            find_menu_words = True
    if (find_menu_words):
        await message.channel.send(f' { message.author.mention } **Меню основных запросов**\n \n- **!качество жизни , !qof** : Качество жизни в Новосибирске\n- **!преступность , !crime** : Преступность в Новосибирске\n- **!здравоохранение , !health care** : Здравоохранение в Новосибирске\n- **!аренда , !rent** : Стоимость аренды недвижимости в Новосибирске')

        #КАЧЕСТВО ЖИЗНИ
    find_qof_words = False
    for item in qof_words:
        if msg.find(item) >= 0:
            find_qof_words = True
    if (find_qof_words):
        await message.channel.send(f' { message.author.mention } **Качество жизни в Новосибирске**\n \n-Индекс покупательной способности 30.11 Очень низкий\n-Индекс безопасности 52.31 Умеренный\n-Индекс здравоохранения 56.10 Умеренный\n-Климатический индекс 16.14 Низкий\n-Индекс стоимости жизни 42.46 Низкий\n-Отношение цены недвижимости к доходу 14.82 Высокий\n-Индекс времени движения на работу 40.58 Умеренный\n-Индекс загрязнения 71.03 Высокий\n \n**Индекс качества жизни: __Очень низкий__**')

        #ПРЕСТУПНОСТЬ
    find_crime_words = False
    for item in crime_words:
        if msg.find(item) >= 0:
            find_crime_words = True
    if (find_crime_words):
            await message.channel.send(f' {message.author.mention} **Преступность в Новосибирске**\n \n-Уровень преступности 48.55 Умеренный\n-Рост преступности за последние 3 года 51.15 Умеренный\n-Беспокойство по украденым вещам 32.18 Низкий\n-Беспокойство по грабежам 43.68 Умеренный\n-Беспокойство по угону автомобиля 43.24 Умеренный\n-Беспокойство по украденым вещам из автомобиля 53.53 Умеренный\n-Беспокойство по уличным нападениям 45.40 Умеренный\n-Беспокойство об оскорблениях 45.93	Умеренный\n-Беспокойство по уличным нападениям из-за цвета кожи, пола и т.д. 33.05 Низкий\n-Употребление или продажа наркотиков 56.03 Умеренный\n-Вандализм и кражи 54.12 Умеренный\n-Вооруженный разбой 35.29 Низкий\n-Коррупция и взяточниство 80.75 Очень высокий\n \n**Безопасность в Новосибирске**\n-Безопасная ходьба в одиночку днем 74.43 Высокий\n-Безопасная ходьба в одиночку ночью 34.88 Низкий')

        #ЗДРАВООХРАНЕНИЕ
    find_health_words = False
    for item in health_words:
        if msg.find(item) >= 0:
            find_health_words = True
    if (find_health_words):
            await message.channel.send(f' {message.author.mention} **Здравоохранение в Новосибирске**\n \n-Навыки и компетентность мед персонала 53.57 Умеренный\n-Скорость выполнение анализов и обследований 54.10 Умеренный\n-Оборудование для современной диагностики и лечения 54.74 Умеренный\n-Точность и полнота обследований 55.83 Умеренный\n-Дружелюбие и вежливость персонала 49.19 Умеренный\n-Отзывчивость в мед учреждениях 41.80 Умеренный\n-Удовлетворенность затратами 62.70 Высокий\n-Удобство местоположения больниц 70.24 Высокий')

        #АРЕНДА НЕДВИЖИМОСТИ
    find_rent_words = False
    for item in rent_words:
        if msg.find(item) >= 0:
            find_rent_words = True
    if (find_rent_words):
            await message.channel.send(f' {message.author.mention} **Цены на аренду недвижимости в Новосибирске**\n \n-Квартира(1 спальня) в центре города\n-Квартира(1 спальня) за пределами центра\n-Квартира(3 спальня) в центре города\n-Квартира(3 спальня) за пределами центра')

        #ПРОЩАНИЕ
    find_bye_words = False
    for item in bye_words:
        if msg.find(item) >= 0:
            find_bye_words = True
    if (find_bye_words):
        await message.channel.send(f' { message.author.mention } Удачного дня!')

    if message.content.startswith('!как дела?'):
        await message.channel.send(f' { message.author.mention } Отлично, как и погода сегодня')

    if message.content.startswith('!чем занимаешься?'):
        await message.channel.send(f' { message.author.mention } Как обычно. Составляю сводки')

    if message.content.startswith('!тебе нравится жить?'):
        await message.channel.send(f' { message.author.mention } Конечно! Надеюсь вам тоже нравится UwU')

    if message.content.startswith('!любишь котиков?'):
        await message.channel.send(f' {message.author.mention} Просто обожаю! =^.^=')

    if message.content.startswith('!город проживания'):
        await message.channel.send(f' {message.author.mention} Ваш город проживания **Москва**')

    if message.content.startswith('!город для релокации'):
        await message.channel.send(f' {message.author.mention} Ваш город для релокации **Новосибирск**')

    if message.content.startswith('!валюта вывода'):
        await message.channel.send(f' {message.author.mention} Ваша валюта **Российский рубль**')
    if message.content.startswith('!сводка о стоимости жизни'):
        await message.channel.send(f' {message.author.mention} -Аренда жилья в городе **Новосибирск** в среднем на __-64%__ ниже, чем в городе **Москва**')

client.run('OTY3MzMwMTUzNDU1ODM3MjI0.YmOuaA.n27IOs_a9pFIzij3Mdinn3UrjMU')
