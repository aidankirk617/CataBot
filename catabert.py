## Dependencies
import discord
import random
from discord.ext import commands

## Client

client = commands.Bot(command_prefix = '!')

## Response-Initializer

@client.event
async def on_message(message):
    msg = message.content.lower().replace(" ", "")

    if '!help' in msg:
        await message.channel.send('p - phone\nm - menu\na - address\nt - tram\ne - email\nh - hours\no - orientation ')

## Menu
    """School Dining"""
    if '!mbrown' in msg:
        await message.channel.send('oop')
    if '!mcaf' in msg:
        await message.channel.send('oop')
    """Chain Dining"""
    if '!mchickfila' in msg:
        await message.channel.send('https://www.chick-fil-a.com')
    if '!mchilis' in msg:
        await message.channel.send('https://www.chilis.com/menu')
    if '!msubway' in msg:
        await message.channel.send('https://www.subway.com/en-us/menunutrition/menu')
    if '!mpapajohns' in msg:
        await message.channel.send('https://www.papajohns.com/order/menu')
    if '!mpandaexpress' in msg:
        await message.channel.send('https://www.pandaexpress.com/menu')
    if '!mwhichwich' in msg:
        await message.channel.send('https://www.whichwich.com/menu/')
    if '!mmoes' in msg:
        await message.channel.send('https://www.moes.com/menu/')
    if '!msteaknshake' in msg:
        await message.channel.send('https://s3-us-west-2.amazonaws.com/cos-steak-n-shake/September+2018/WCU+Web+Menu+8-16-18.pdf')
    if '!mstarbucks' in msg:
        await message.channel.send('https://www.starbucks.com/menu')
    if '!meinsteinbros' in msg:
        await message.channel.send('https://www.einsteinbros.com/menu/')
    if '!mjavacity' in msg:
        await message.channel.send('https://www.menuism.com/menus/java-city-40736')
    if '!mfreshens' in msg:
        await message.channel.send('https://freshens.com/menu/')
    """Off-Campus Dining"""
    if '!mcitylights' in msg:
        await message.channel.send('http://www.citylightscafe.com')
    if '!mspeedys' in msg:
        await message.channel.send('https://www.speedyspizzaofsylva.com')
    if '!mwhitemoon' in msg:
        await message.channel.send('https://www.whitemoonnc.com/menus/')
    if '!mkobeexpress' in msg:
        await message.channel.send('https://www.zmenu.com/kobe-express-sylva-online-menu/')
    if '!mcreekside' in msg:
        await message.channel.send('https://www.zmenu.com/creekside-oyster-house-and-grill-sylva-online-menu/')
    if '!mjackthedipper' in msg:
        await message.channel.send('https://www.zmenu.com/jack-the-dipper-ice-cream-sylva-online-menu/')
    if '!mbignicks' in msg:
        await message.channel.send('https://www.zmenu.com/big-nicks-bbq-sylva-online-menu/')
    if '!mhaywoods' in msg:
        await message.channel.send('https://www.haywoodsmokehouse.com/pages/lunch-dinner-menu')
    if '!mkostas' in msg:
        await message.channel.send('https://www.kostasexpress.com/menu')
    if '!mforagers' in msg:
        await message.channel.send('https://www.foragerscanteen.com/lunch-dinner-menu.pdf')
    if '!mboots' in msg:
        await message.channel.send('https://www.bootssteakhouse.com/dinner-menu')

## Hours

    """Food"""
    if '!hbrown' in msg:
        await message.channel.send("Breakfast\n Mon - Fri        7:00AM - 9:00AM\nSat - Sun        Closed")

    if '!hcaf' in msg:
        await message.channel.send("Breakfast\n Mon - Fri        7:00AM - 10:30AM\nBrunch          Sat - Sun9:00AM - 2:00PM\nLunch\nMon - Fri10:30AM - 4:45PM\nDinner\nMon - Fri4:45PM - 9:00PM\nSat - Sun4:45PM - 8:00PM\nLate Night\nThu - Sat10:00PM - 12:30AM")

    """Academic Buildings"""
    if '!hcrc' in msg:
        await message.channel.send("Buff to buff")

    if '!hclimbingwall' in msg:
        await message.channel.send("Climb to climb")

## Events

    if '!campusevents' in msg:
        await message.channel.send('https://www.flattenthecurve.com')

## Tram

    if '!tallcampusexpress' in msg:
        await message.channel.send('Monday-Friday: 7:30 am - 5:00 pm')
    if '!tcommuterexpress' in msg:
        await message.channel.send('Monday-Friday: 7:30 am - 5:00 pm')
    if '!tvillageexpress' in msg:
        await message.channel.send('Monday-Friday: 7:30 am - 5:00 pm')
    if '!thhsexpress' in msg:
        await message.channel.send('Monday-Friday: 7:00 am - 5:00 pm')
    if '!thhscommuterexpress' in msg:
        await message.channel.send('Monday-Friday: 5:00pm-11pm')

## Memes

    if '!romance' in msg:
        await message.channel.send('https://www.youtube.com/watch?v=DWSUd2FpuRE')

## Phone Numbers

    if '!pcrc' in msg:
        await message.channel.send("828-227-7069")
    if '!pchancellorsoffice' in msg:
        await message.channel.send("828-227-7100")
    if '!pprovostsoffice' in msg:
        await message.channel.send("828-227-7495")
    if '!phumanresources' in msg:
        await message.channel.send("828-227-7218")
    if '!pgraduateschool' in msg:
        await message.channel.send("800-369-9854")
    if '!pdistanceandonline' in msg:
        await message.channel.send("866-928-4723")
    if '!palumniassociation' in msg:
        await message.channel.send("877-440-9990")
    if '!pofficeoffinancialaid' in msg:
        await message.channel.send("828-227-7290")
    if '!padvancement' in msg:
        await message.channel.send("828-227-7124")
    if '!pcampuspolice' in msg:
        await message.channel.send("828-227-7301")
    if '!padvancement' in msg:
        await message.channel.send("828-227-7124")
    if '!pscholarships' in msg:
        await message.channel.send("828-227-7290")
    if '!pbardoartscenter' in msg:
        await message.channel.send("828-227-2787")
    if '!ponestop' in msg:
        await message.channel.send("828-227-7170")
    if '!pathleticsdepartment' in msg:
        await message.channel.send("828-227-7338")
    if '!pcommunityengagement' in msg:
        await message.channel.send("828-227-7495")

## Emails

    if '!eundergraduateadmissions' in msg:
        await message.channel.send("admiss@wcu.edu")
    if '!ehumanresources' in msg:
        await message.channel.send("jobs@wcu.edu")
    if '!egraduateschool' in msg:
        await message.channel.send("grad@wcu.edu")
    if '!edistanceandonline' in msg:
        await message.channel.send("distance@wcu.edu")
    if '!enewsandmediarelations' in msg:
        await message.channel.send("bstudenc@wcu.edu")
    if '!eofficeoffinancialaid' in msg:
        await message.channel.send("finaid@wcu.edu")
    if '!eonestop' in msg:
        await message.channel.send("osssc@email.wcu.edu")

## Addresses

    if '!achancellorsoffice' in msg:
        await message.channel.send("501 H.F. Robinson\nWestern Carolina University\nCullowhee, NC  28723")
    if '!aundergraduateadmissions' in msg:
        await message.channel.send("102 Cordelia Camp\nWestern Carolina University\nCullowhee, NC  28723")
    if '!aprovostsoffice' in msg:
        await message.channel.send("560 H.F. Robinson\nWestern Carolina University\nCullowhee, NC  28723")
    if '!ahumanresources' in msg:
        await message.channel.send("220 H.F. Robinson\nWestern Carolina University\nCullowhee, NC 28723")
    if '!agraduateschool' in msg:
        await message.channel.send("110 Cordelia Camp\nWestern Carolina University\nCullowhee, NC  28723")
    if '!adistanceandonline' in msg:
        await message.channel.send("138 Cordelia Camp\nCullowhee, NC 28723")
    if '!aalumniassociation' in msg:
        await message.channel.send("242 H.F. Robinson\nWestern Carolina University\nCullowhee, NC 28723")
    if '!aofficeoffinancialaid' in msg:
        await message.channel.send("105 Cordelia Camp\n1 University Drive\nCullowhee, NC 28723")
    if '!aadvancement' in msg:
        await message.channel.send("201 H.F. Robinson Administration\nWestern Carolina University\n1 University Drive\nCullowhee, NC 28723")
    if '!acampuspolice' in msg:
        await message.channel.send("Cordelia Camp Annex\nCullowhee, NC 28723")
    if '!ascholarships' in msg:
        await message.channel.send("105 Cordelia Camp\n1 University Drive\nCullowhee, NC 28723")
    if '!abardoartscenter' in msg:
        await message.channel.send("199 Centennial Drive\nCullowhee, NC 28723")
    if '!aonestop' in msg:
        await message.channel.send("132 Killian Annex\nCullowhee, NC 28723")
    if '!aathleticsdepartment' in msg:
        await message.channel.send("Western Carolina University\nRamsey Center - Athletics\nCullowhee, NC 28723")
    if '!acommunityengagement' in msg:
        await message.channel.send("560 H.F. Robinson Administration\nWestern Carolina University\nCullowhee, NC 28723")

## Orientation

    if '!ocampusactivities' in msg:
        await message.channel.send("https://www.youtube.com/watch?v=ipvP58Jl-bg")
    if '!ohealthandwellness' in msg:
        await message.channel.send("https://www.youtube.com/watch?v=-jBwCMQ8_88&list=PLjrEsnlZROynYkcYIpysgTM89frWza1iS")
    if '!ostudentemployment' in msg:
        await message.channel.send("https://www.youtube.com/watch?v=zkKuPKK4CSQ&list=PLjrEsnlZROynYkcYIpysgTM89frWza1iS&index=2")
    if '!oacademiclife' in msg:
        await message.channel.send("https://www.youtube.com/watch?v=MF4VDTTqk2M&list=PLjrEsnlZROynYkcYIpysgTM89frWza1iS&index=3")
    if '!ocampussafety' in msg:
        await message.channel.send("https://www.youtube.com/watch?v=ZvgDIZ-IRpY&list=PLjrEsnlZROynYkcYIpysgTM89frWza1iS&index=4")
    if '!oinformationtechnology' in msg:
        await message.channel.send("https://www.youtube.com/watch?v=RRlYjYgU7Ho&list=PLjrEsnlZROynYkcYIpysgTM89frWza1iS&index=5")
    if '!odeanofstudents' in msg:
        await message.channel.send("https://www.youtube.com/watch?v=6l3eeFam9r4&list=PLjrEsnlZROynYkcYIpysgTM89frWza1iS&index=6")
    if '!ointerculturalaffairs' in msg:
        await message.channel.send("https://www.youtube.com/watch?v=97-8i_Hj0bs&list=PLjrEsnlZROynYkcYIpysgTM89frWza1iS&index=7")
    if '!ocampusdining' in msg:
        await message.channel.send("https://www.youtube.com/watch?v=6ZiPdwhUAiY&list=PLjrEsnlZROynYkcYIpysgTM89frWza1iS&index=8")
    if '!oresidentialliving' in msg:
        await message.channel.send("https://www.youtube.com/watch?v=aRiZDnvfCfk&list=PLjrEsnlZROynYkcYIpysgTM89frWza1iS&index=10")
    if '!oorientation' in msg:
        await message.channel.send("https://www.youtube.com/watch?v=epg_mzV8olg&list=PLjrEsnlZROynYkcYIpysgTM89frWza1iS&index=11")

## Commands

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):

    responses = ['It is certain',
                 'Without a doubt',
                 'You may rely on it',
                 'Yes definitely',
                 'It is decidedly so',
                 'As I see it, yes',
                 'Most likely',
                 'Yes',
                 'Outlook good',
                 'Signs point to yes',
                 'Reply hazy try again',
                 'Better not tell you now',
                 'Ask again later',
                 'Cannot predict now',
                 'Concentrate and ask again',
                 'Don’t count on it',
                 'Outlook not so good',
                 'My sources say no',
                 'Very doubtful',
                 'My reply is no'
    ]

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


## Startup

@client.event
async def on_ready():
    print('Bot is ready.')

client.run('NzM0NTAyNDczODI5NDQ5Nzg3.XxS37A.uDSPpzSMevd1dvCZRQFL94i7pKI')