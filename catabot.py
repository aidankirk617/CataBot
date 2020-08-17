# Dependencies
import discord
import random
from discord.ext import commands

# Client

client = commands.Bot(command_prefix='!')

# Response-Initializer


@client.event
async def on_message(message):
    msg = message.content.lower().replace(" ", "")

    if '!help' in msg:
        await message.channel.send('p - phone\nm - menu\na - address\nt - tram\ne - email\nh - hours\no - orientation\ni - info\nl - link\nr - resource\ng - map/geography ')

# Info

    """CRC"""
    if '!icrc' in msg:
        await message.channel.send('The Campus Recreation Center is a stand-alone facility located in the heart of campus between the University Center and Reid Gym and includes the following:\nMore than 9,800 square feet of fitness space featuring cardiovascular and weight equipment\nTwo multi-purpose courts\nA three-lane indoor jogging/walking track; each lap = 1/8 of a mile\nTwo group exercise/multipurpose studios\n48-foot climbing wall with belaying and bouldering\nMeeting room and conference room\nFull locker room facilities\nTwo assessment rooms\nAdministrative offices')

    if '!ireidpool' in msg:
        await message.channel.send('Reid Gym is the building southwest of the Campus Recreation Center, which is managed by the School of Teaching and Learning. Located within Reid are four gymnasiums and a pool. While the facility is mainly used for health education classes and parks and recreation management academic classes, Intramural Sports games are often held here too. To access upstairs Reid before 9:00pm, you can enter through the Reid Fitness area and take the stairwell upstairs.  If after 9 p.m., you must walk around to the backside of Reid and enter through a set of double doors at the bottom of a stair well. To get to Reid Pool, you must first enter the locker rooms and through there you may reach the pool.')

    if '!iclimbingwall' in msg:
        await message.channel.send('WCU is home to one of the most extensive climbing programs in the East, and we have the tallest collegiate wall in North Carolina. The climbing wall typically opens on weekdays at 4 pm, with additional hours for clinics, family climbs, and kids climbs also available. ')

    if '!idiscgolfcourse' in msg:
        await message.channel.send('Catamount Link is our on-campus disc golf course featuring 13 holes and 1 practice basket. Check out discs at the CRC equipment cage, then start at Hole #1 directly behind the CRC.')

    if '!ifields' in msg:
        await message.channel.send('The CRW Fields are located across the street/creek from the football stadium and the Ramsey Center. Depending on the semester, they accommodate two flag football fields, two softball fields, and one rugby field. These fields are typically reserved for Intramural Sports and Club Sports practices/games, but they can also be used for informal recreation on a first come, first serve basis. Groups wanting to reserve the intramural fields must complete a request form.')

    if '!icycleshop' in msg:
        await message.channel.send('The Base Camp Cycle Shop is your one-stop shop for all your cycling needs. Students have access to a fully equipped bike shop and trained technician to assist in repairs and answer questions. Whether a road bike, mountain bike, or something in between, we have the tools and knowledge to keep the cycling adventure going. Dont forget to ask about our monthly clinics ranging from basic bike maintenance to essential mountain biking skills. BCC also offers mountain bike rentals to explore nearly 7 miles of the WCU campus trail system')

    if '!ibasecamp' in msg:
        await message.channel.send('Base Camp Cullowhee gives you the opportunity to get out and explore the world around you. This is more than just a recreation program, you have an array of outdoor recreation trips, experiential education opportunities, and outdoor equipment rentals right at your fingertips.\nHome to human powered adventure at WCU, there are over 9,000 experiences available per year so no matter what you seek, trip programs, guide services, rental equipment or conquering our indoor climbing wall, theres an experience for everyone. Discover first hand how adventures can be one of the best ways to learn.\nWestern Carolina University has been named Top Adventure College - Blue Ridge Outdoor Magazine (2014, 2015, 2016, 2017, 2019)')

    if '!ifirstascent' in msg:
        await message.channel.send('Already love what you’re seeing and hearing about life at Western Carolina University? The First Ascent wilderness orientation program gives you the chance to make new friends and discover the beautiful region that surrounds WCU.\nWhether you want to simply dip your toe in and spend an afternoon rafting on the Nantahala River or want to immerse yourself in an experience that will take you beyond civilization and deep into the mountains, First Ascent has a trip for you. You’ll return with lasting memories and friends for future adventures.')

    if '!iintramuralsports' in msg:
        await message.channel.send('Intramural Recreational Sports offers a wide array of leagues and tournaments throughout the year. Intramural Recreational Sports are free for students and members of the Campus Recreation Center. For membership policies, please check "membership information" at go.wcu.edu/crw.')

    if '!ifitness' in msg:
        await message.channel.send('WCU Campus Recreation offers regular exercise programming, special events, certifications and training and more for the campus community.')

    """Parking"""

    if '!ifreshmanparking' in msg:
        await message.channel.send('Generally, yellow stripes denote spaces for faculty and staff members; white striped spaces are for students. White striped spaces near the residence halls are for on-campus resident students. Freshmen are not permitted to park at the residence halls, all Freshmen must park in freshmen Catamount Lot #73, Walker A Lot #19A, South Baseball Lot #8B or HHS Overflow Lot# 76B.\n Commuter students are permitted to park in faculty/staff spaces after 5:00pm Monday-Friday and weekends.')

    if '!iparking' in msg:
        await message.channel.send('Students, faculty and staff must register their vehicle with the parking operations office in order to park on campus.  Specific parking areas are designated for students by class status. Students should apply for a parking pass at the beginning of each academic year.')

    if '!istaffparking' in msg:
        await message.channel.send('Faculty and staff may register their vehicles to obtain parking permits anytime, and permanent staff and faculty parking permits are non-expiring. An employee is defined as a person who is paid by the University or a private contractor such as Aramark, is listed as an employee in Human Resources or in Academic Affairs, and is not at the University primarily for their own educational advancement.')

# Links

    if '!ladmissions' in msg:
        await message.channel.send('https://www.wcu.edu/apply/undergraduate-admissions/apply.aspx')
    if '!lgraduateschool' in msg:
        await message.channel.send('https://www.wcu.edu/apply/graduate-school/admissions/apply-now.aspx')
    if '!lfinancialaid' in msg:
        await message.channel.send('https://www.wcu.edu/apply/undergraduate-admissions/costs-and-aid/index.aspx')
    if '!lscholarships' in msg:
        await message.channel.send('https://www.wcu.edu/apply/scholarships/index.aspx')
    if '!lwcuscholarships' in msg:
        await message.channel.send('https://www.wcu.edu/apply/scholarships/wcu-scholarships.aspx')
    if '!lnonwcuscholarships' in msg:
        await message.channel.send('https://www.wcu.edu/apply/scholarships/non-wcu-scholarships/index.aspx')
    if '!lfafsa' in msg:
        await message.channel.send('https://studentaid.gov/h/apply-for-aid/fafsa')
    if '!lworkstudy' in msg:
        await message.channel.send('https://www.wcu.edu/apply/financial-aid/types-of-aid/work-study.aspx')
    if '!lcollegeboard' in msg:
        await message.channel.send('https://www.collegeboard.org')
    if '!lblackboard' in msg:
        await message.channel.send('https://wcu.blackboard.com')
    if '!lfastweb' in msg:
        await message.channel.send('https://www.fastweb.com')
    if '!lcappex' in msg:
        await message.channel.send('https://www.cappex.com')
    if '!llinkedin' in msg:
        await message.channel.send('https://www.linkedin.com')
    if '!lgithub' in msg:
        await message.channel.send('https://github.com')
    if '!loutlook' in msg:
        await message.channel.send('https://outlook.live.com/owa/')
    if '!llinkedin' in msg:
        await message.channel.send('https://www.linkedin.com')
    if '!lmbti' in msg:
        await message.channel.send('https://www.16personalities.com/free-personality-test')

# Menu

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

# Hours

    """Food"""
    if '!hbrown' in msg:
        await message.channel.send("Breakfast\n Mon - Fri        7:00AM - 9:00AM\nSat - Sun        Closed")

    if '!hcaf' in msg:
        await message.channel.send("Breakfast\n Mon - Fri        7:00AM - 10:30AM\nBrunch          Sat - Sun9:00AM - 2:00PM\nLunch\nMon - Fri10:30AM - 4:45PM\nDinner\nMon - Fri4:45PM - 9:00PM\nSat - Sun4:45PM - 8:00PM\nLate Night\nThu - Sat10:00PM - 12:30AM")

    """Academic Buildings"""
    if '!hadventureshop' in msg:
        await message.channel.send("Mon: 11am - 5pm\nTue: 12pm - 5pm\nWed: 12pm - 5pm\nThu: 12pm - 5pm\nFri: 10am - 5pm")

    if '!hclimbingwall' in msg:
        await message.channel.send("Mon: 4pm - 8pm\nTue: 4pm - 8pm\nWed: 4pm - 8pm\nThu: 4pm - 8pm\nFri: 4pm - 7pm")

    if '!hcycleshop' in msg:
        await message.channel.send("Mon: 3pm - 5pm\nThu: 3pm - 5pm")

# Events

    if '!campusevents' in msg:
        await message.channel.send('https://www.flattenthecurve.com')

# Tram

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

# Memes

    if '!romance' in msg:
        await message.channel.send('https://www.youtube.com/watch?v=DWSUd2FpuRE')
    if '!saysomething' in msg:
        await message.channel.send('something')
    if '!areyouworkingcorrectly' in msg:
        await message.channel.send('no')
    if '!howoldami' in msg:
        await message.channel.send('college aged')
    if '!whotoldyouthat' in msg:
        await message.channel.send('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fassets.wired.com%2Fphotos%2Fw_1862%2Fwp-content%2Fuploads%2F2017%2F02%2FMarkZuckerberg.jpg&f=1&nofb=1')
    if '!boogie' in msg:
        await message.channel.send('https://www.youtube.com/watch?v=Zo_QeYg1uf8')
    if '!sleepmusic' in msg:
        await message.channel.send('https://www.youtube.com/watch?v=X2WH8mHJnhM')
    if '!debug' in msg:
        await message.channel.send('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fdata.whicdn.com%2Fimages%2F319821881%2Foriginal.jpg&f=1&nofb=1')
    if '!gibby' in msg:
        await message.channel.send('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fih1.redbubble.net%2Fimage.665117808.5911%2Fflat%2C750x1000%2C075%2Ct.u1.jpg&f=1&nofb=1')
    if '!tidus' in msg:
        await message.channel.send('https://www.youtube.com/watch?v=H47ow4_Cmk0')
    if '!megatidus':
        await message.channel.send('https://www.youtube.com/watch?v=GB-tlOWtKy4')

# Trail System

    if '!trailmap' in msg:
        await message.channel.send('https://wcucycling.files.wordpress.com/2013/08/wcutrailmap700.jpg?w=300&h=194&zoom=2')
    if '!trailinfo' in msg:
        await message.channel.send('https://wcucycling.wordpress.com/wcu-trail-system/')
    if '!trailguidelines' in msg:
        await message.channel.send("Trail Guidelines:\n– Participate at your own risk\n– Stay on the designated trail\n– No alcohol on the property and you must not be under the influence of alcohol or drugs while on the trail system\n– No Camping\n– No Fires\n– This is WCU property, so all WCU policies apply, such as: No guns or weapons")

# Study Resources
    """Music"""
    if '!studymusic' in msg:
        await message.channel.send('https://www.youtube.com/watch?v=5qap5aO4i9A' or
                                   'https://www.youtube.com/watch?v=mg7netw1JuM' or
                                   'https://www.youtube.com/watch?v=VB6SIKl8Md0' or
                                   'https://www.youtube.com/watch?v=jgpJVI3tDbY' or
                                   'https://www.youtube.com/watch?v=WPni755-Krg')

    """Online Resources"""
    if '!rcomputerscience' in msg:
        await message.channel.send('https://www.freecodecamp.org')
    if '!rmath' in msg:
        await message.channel.send('https://www.wolframalpha.com')
    if '!rmoocs' in msg:
        await message.channel.send('https://www.edx.org')

    """Language Resources"""
    if '!rjava' in msg:
        await message.channel.send('https://www.w3schools.com/java/')
    if '!rjavascript' in msg:
        await message.channel.send('https://www.w3schools.com/js/default.asp')
    if '!rpython' in msg:
        await message.channel.send('https://www.w3schools.com/python/default.asp')
    if '!rrust' in msg:
        await message.channel.send('https://www.rust-lang.org/learn')
    if '!rruby' in msg:
        await message.channel.send('https://www.ruby-lang.org/en/documentation/')
    if '!rc' in msg:
        await message.channel.send('\https://docs.microsoft.com/en-us/cpp/c-language/organization-of-the-c-language-reference?view=vs-2019')
    if '!rc#' in msg:
        await message.channel.send('https://www.w3schools.com/cs/default.asp')
    if '!rc++' in msg:
        await message.channel.send('https://www.w3schools.com/cpp/default.asp')
    if '!rswift' in msg:
        await message.channel.send('https://swift.org/documentation/#the-swift-programming-language')
    if '!rbash' in msg:
        await message.channel.send('https://www.gnu.org/software/bash/manual/')
    if '!rlinux' in msg:
        await message.channel.send('https://www.kernel.org/doc/html/latest/')
    if '!rcybersecurity' in msg:
        await message.channel.send('https://www.hackthebox.eu')
    if '!rhtml' in msg:
        await message.channel.send('https://www.w3schools.com/html/default.asp')
    if '!rcss' in msg:
        await message.channel.send('https://www.w3schools.com/css/default.asp')
    if '!rphp' in msg:
        await message.channel.send('https://www.w3schools.com/php/default.asp')

    """School Resources"""
    if '!rhunterlibrary' in msg:
        await message.channel.send('https://www.wcu.edu/hunter-library/')
    if '!rbardo' in msg:
        await message.channel.send('https://www.wcu.edu/bardo-arts-center/')
    if '!rtutoring' in msg:
        await message.channel.send('https://www.wcu.edu/learn/academic-success/tutoring-services/')
    if '!rmtc' in msg:
        await message.channel.send('https://www.wcu.edu/learn/academic-success/tutoring-services/services-resources/mathematics-tutoring-center/index.aspx')
    if '!rstaffdirectory' in msg:
        await message.channel.send('https://www.wcu.edu/discover/contact-wcu/staff-directory.aspx')

# Colleges

    if '!collegeofartsandsciences' in msg:
        await message.channel.send('https://www.wcu.edu/learn/departments-schools-colleges/cas/index.aspx')
    if '!collegeofbusiness' in msg:
        await message.channel.send('https://www.wcu.edu/learn/departments-schools-colleges/cob/index.aspx')
    if '!collegeofeducationandalliedprofessions' in msg:
        await message.channel.send('https://www.wcu.edu/learn/departments-schools-colleges/ceap/index.aspx')
    if '!collegeofengineeringandtechnology' in msg:
        await message.channel.send('https://www.wcu.edu/learn/departments-schools-colleges/cet/index.aspx')
    if '!collegeoffineandperformingarts' in msg:
        await message.channel.send('https://www.wcu.edu/learn/departments-schools-colleges/fpa/index.aspx')
    if '!collegeofhealthandhumansciences' in msg:
        await message.channel.send('https://www.wcu.edu/learn/departments-schools-colleges/HHS/index.aspx')

# Phone Numbers

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

# Emails

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

# Addresses

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
    if '!abardo' in msg:
        await message.channel.send("199 Centennial Drive\nCullowhee, NC 28723")
    if '!aonestop' in msg:
        await message.channel.send("132 Killian Annex\nCullowhee, NC 28723")
    if '!aathleticsdepartment' in msg:
        await message.channel.send("Western Carolina University\nRamsey Center - Athletics\nCullowhee, NC 28723")
    if '!acommunityengagement' in msg:
        await message.channel.send("560 H.F. Robinson Administration\nWestern Carolina University\nCullowhee, NC 28723")

# Orientation

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

# Maps

    if '!gfullcampus' in msg:
        await message.channel.send("https://map.concept3d.com/?id=966#!ce/15111?ct/32505,32525,32528,32534,32552,32554,15111,35399,42553,42554")
    if '!gtram' in msg:
        await message.channel.send("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.wcu.edu%2FWebGraphicsNew%2FFall2016CommencementMap.jpg&f=1&nofb=1")
    if '!gcampuslegend' in msg:
        await message.channel.send("https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.mobilemaplets.com%2Fthumbnails%2F15590_thumbnail-1024.jpg&f=1&nofb=1")
    if '!groadroute' in msg:
        await message.channel.send("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.Bc-9txx79POL1jBRkED9dgHaI8%26pid%3DApi&f=1")
    if '!gfootballparking' in msg:
        await message.channel.send("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.wcu.edu%2FWebGraphicsNew%2Ffootballmap2016.jpg&f=1&nofb=1")
    if '!gbiltmorepark' in msg:
        await message.channel.send("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.wcu.edu%2FWebGraphicsNew%2FWCU_Biltmore_Parking.jpg&f=1&nofb=1")
    if '!gtrailsystem' in msg:
        await message.channel.send("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.singletracks.com%2Fblog%2Fwp-content%2Fuploads%2F2018%2F04%2Fwcu_bike_trail_map.jpg&f=1&nofb=1")
    if '!gmountainheritage' in msg:
        await message.channel.send("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.wcu.edu%2FWebGraphicsNew%2Fmhd-tab-map-2015.jpg&f=1&nofb=1")
    if '!gfootballstadium' in msg:
        await message.channel.send("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.wcu.edu%2Framsey%2F_resources%2Fimages%2FRamsey_Concourse_Map.jpg&f=1&nofb=1")

# Commands


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


# Startup

@client.event
async def on_ready():
    print('Bot is ready.')

client.run('NzM0NTAyNDczODI5NDQ5Nzg3.XxSovA.MxEQPyg7GeITKtrQbqcoRJy3gCY')
