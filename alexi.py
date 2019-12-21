import collections
import discord
import requests


from discord.ext import commands


from feupy.exams import exams
from feupy import Student
from feupy import CurricularUnit
from pprint import pprint

bot = commands.Bot(command_prefix='*')
token_file = "token.txt"

with open(token_file) as f:
    TOKEN = f.read()

@bot.event
async def on_ready():
    #message = "Alex esta aqui para estourar tudo"
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="ALEXI", description="ESTOURAAA", color=0x666666)

    # give info about you here
    embed.add_field(name = "Author", value = "Rodykings")

    # give users a link to invite thsi bot to their server
    embed.add_field(name = "Invite", value = "https://discordapp.com/api/oauth2/authorize?client_id=657595527814184983&permissions=0&scope=bot")

    await ctx.send(embed = embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "AlexiBot", description = "Obrigado por terem vindo. Horário de atendimento: 14:40h - 17:00h M401, L209", color=0x666666)

    #embed.add_field(name = "*stats", value = "Gives stats about messages/emojis", inline = False)
    embed.add_field(name = "*info", value = "Gives a little info about the bot", inline=False)
    embed.add_field(name = "*help", value = "Gives all the commands", inline=False)
    embed.add_field(name = "*student <up number>", value = "Gives name, institution, course and SIGARRA LINK", inline=False)
    embed.add_field(name = "*exams <mieic year(1-5)>", value = "Gives table of exams", inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def student(ctx, up):  

    std = Student(up)

    embed = discord.Embed(title=f"{std.name}", description=up, color=0xFF0000)

    embed.add_field(name = "Course ID", value = f"{std.courses[0]['course']}")

    embed.add_field(name = "Institution", value = f"{std.courses[0]['institution']}")

    embed.add_field(name = "SIGARRA URL", value = f"{std.url}")

    
    await ctx.send(embed=embed)


@bot.command()
async def exams(ctx, y):  

    from feupy.exams import exams
    from feupy import CurricularUnit
    from pprint import pprint

    mieic_exams_url = "https://sigarra.up.pt/feup/pt/exa_geral.mapa_de_exames?p_curso_id=742"

    embed = discord.Embed(title="EXAMS MIEIC " + str(y) + "º ANO", color=0xFF0000)
    for i in exams(mieic_exams_url):
        val = str(i['start']) +  "\n" + str(i['finish']) +  "\n" + str(list(i['rooms'])) + "\n" + str(i['season'])
        if(int(y) == i['curricular unit'].curricular_year):
            embed.add_field(name = f"{i['curricular unit']}", value = val)

    await ctx.send(embed = embed)

bot.run(TOKEN)