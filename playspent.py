import tkinter as tk
from tkinter import *
import random

w = Tk()
w.title('PlaySpent Python')
w.geometry('1200x600')

#Create global variables and their corresponding labels
day = 30
money = random.randint(800, 1000)
payday = 7
strikes = 0
m = Label(w, text='Money:' + str(money), font=('Verdana',10))
m.place(x=20, y=5)
d = Label(w, text='Days Left:' + str(day), font=('Verdana',10))
d.place(x=20,y=25)
pd = Label(w, text='Days Until Payday:' + str(payday), font=('Verdana',10))
pd.place(x=20,y=45)
s = Label(w, text='Job Strikes:' + str(strikes), font=('Verdana',10))
s.place(x=20, y=65)

#The twochoices and threechoices functions generate each scenario's
    #text and buttons, accepting text, the current game mode,
    #and changes to global variables as arguments
def twochoices(txxt, res1, btn1, amt1, stk1, stg1, res2, btn2, amt2, stk2, stg2):
    txt.config(text=txxt)
    b1.config(text=btn1, command=lambda: [popup(res1), loop(amt1, stk1, stg1)])
    b2.config(text=btn2, command=lambda: [popup(res2), loop(amt2, stk2, stg2)])
    b3.pack_forget()

#The config method simply updates global widgets        
def threechoices(txxt, res1, btn1, amt1, stk1, stg1, res2, btn2, amt2, stk2, stg2, res3, btn3, amt3, stk3, stg3):
    txt.config(text=txxt)
    b1.pack(ipadx=10, pady=10)
    b1.config(text=btn1, command=lambda: [popup(res1), loop(amt1, stk1, stg1)])
    b2.pack(ipadx=10, pady=10)
    b2.config(text=btn2, command=lambda: [popup(res2), loop(amt2, stk2, stg2)])
    b3.pack(ipadx=10, pady=10)
    b3.config(text=btn3, command=lambda: [popup(res3), loop(amt3, stk3, stg3)])

#This function is called whenever a choice is made,
    #accepting global variables and the current game mode
def loop(amt, stk, cmd):
    global day, money, strikes, payday
    #These if/elif blocks are only used for the gameover window
    if cmd == 're':
        restart(31, random.randint(800, 1000), 8, 0)
    if cmd == 'cs':
        w.destroy()
    #If the day is zero, the game is over, so all functionality
        #depends on the day being at least one
    if day > 0:
        #This calls the lottery function for appropriate scenarios
        if cmd == 'l1' or cmd == 'l2' or cmd == 'l3':
            lottery(amt, cmd)
        day -= 1
        d.config(text='Day:' + str(day))
        money += amt
        m.config(text='Money:' + str(money))
        #After updating the money value, the program ends the game
            #if zero or less; otherwise, it updates the strike
            #and payday variables if the player has not been fired
        if money > 0:
            if strikes != 'FIRED':
                strikes += stk
                s.config(text='Job Strikes:' + str(strikes))
                if strikes < 3:
                    payday -= 1
                elif strikes >= 3:
                    payday = 'FIRED'
                    pd.config(text='Days Until Payday: FIRED')
                    strikes = 'FIRED'
                    s.config(text='Job Strikes: FIRED')
                if payday == 0:
                    money += random.randint(300, 350)
                    m.config(text='Money:' + str(money))
                    payday = 7
                pd.config(text='Days Until Payday:' + str(payday))
            select(cmd)
        else:
            gameover('Sorry, but you failed to land on your feet. Try again?')
    #Else statements call gameover if the player runs out of money
        #or survives the month, supplying the appropriate arguments
    else:
        gameover('You survived your month in poverty with $' + str(money) + ''' remaining...
        but will it be enough to pay next month's rent?''')

def lottery(amt, cmd):
    #x defines the number of lottery tickets purchased
    x = 0
    if amt == -10:
        x = 3
    elif amt == -5:
        x = 1
    while x > 0:
        #Each ticket runs this loop once, with each time
            #offering a 500-to-one chance of immediate victory
        if random.randint(1,500) == 500:
            gameover('''You won $1,000,000 in the lottery
            and are no longer in poverty! Great job!!''') 
            return
        elif random.randint(1,500) in range(1,500):
            x -= 1
    if cmd == 'l1':
        select('c')
        return 
    if cmd == 'l2':
        select('s')
        return 
    if cmd == 'l3':
        select('r')
        return
    
def popup(res):
    #This function simply generates an informational popup
        #showing the result of each decision
    p = Toplevel(w)
    p.geometry("700x350")
    p.title("Result")
    Label(p, text=res, font=('Verdana', 13)).pack(pady=30)
    Button(p, text="Continue", font=('Verdana', 10), command=p.destroy).pack(padx=50, pady=10)          

def gameover(txxt):
    #This function simply passes arguments
        #into twochoices() to update the main window
    txxxt = txxt
    twochoices(txxxt, 'Good luck!', 'Restart', 0, 0, 're', 'Thanks for playing!', 'Close', 0, 0, 'cs')

def restart(dd, mm, pp, ss):
    #This function resets global variables and the main window
    global day, money, payday, strikes
    day = dd
    money = mm
    payday = pp
    strikes = ss
    m.config(text='Money:' + str(money))
    d.config(text='Days Left:' + str(day))
    pd.config(text='Days Until Payday:' + str(payday))
    s.config(text='Job Strikes:' + str(strikes))
    threechoices('''You just lost your home to foreclosure
    and must find an apartment for you and your teen to stay in.''',
    '''You won't have to worry about driving or gas,
    but inner-city living presents its own significant challenges.''',
    '''Inner city ($700 rent, no gas)''', -700, 0, 'c',
    '''You'll avoid the rough downtown neighborhoods,
    but a shortage of jobs in the suburbs means you'll face a long commute.''',
    '''Suburban ($500 rent, moderate gas)''', -1 * random.randint(600, 800), 0, 's',
    '''You'll enjoy lower rent, crime, and noise, but high gas expenditures
    and frequent traffic jams will be tough to adapt to.''',
    '''Rural ($300 rent, high gas)''', -1 * random.randint(500, 900), 0, 'r')

#The next 150 functions (through r50) pass arguments
    #to the choice functions, generating the scenarios
def c1():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''Your teen normally walks to school by themselves,
    but they can't today due to thunderstorms in the area.''',
    '''Your teen arrives on time to school, but you clock in
    thirty minutes tardy, scoring you a job strike.''', '''Hail him a cab''', -6, 1, 'c',
    '''Despite arriving on time to work, the truant officer calls and pledges
    legal action should your teen miss any more school.''', '''Run to work in the rain''',
    0, 0, 'c')
    
def c2():
    twochoices('''You've been struggling with social isolation
    due to your financial troubles and past poor decisions.
    A trip to the bar may deliver relief...
    if you can shell out $30 for a babysitter.''', '''Everyone there either is already taken or
    rejected you, and you return home feeling even more lonely.''', '''Pay the $30''', -30, 0,
    'c','''You feel like you missed out on a night of fun as you see cute couples
    from the bar on your social media feeds the next day.''', '''Stay home''', 0, 0, 'c')
    
def c3():
    threechoices('''The both of you have been living solely off beans, peanuts,
    frozen vegetables, chicken breast, and bread since foreclosure,
    but your teen is beginning to refuse to eat.''',
    '''Your teen is finally enjoying eating and consuming a more balanced diet.''',
    '''Buy him more expensive staples like dairy and other meats''', -50, 0, 'c',
    '''Your teen is bummed it's only one meal a week,
    but he still appreciates the break from the ultra-cheap diet.''',
    '''Buy him fast food once a week''', -20, 0, 'c',
    '''Your teen remains upset, but at least you manage to talk
    him into eating his rations tonight.''',
    '''Do not buy him any other foods''', 0, 0, 'c')
    
def c4():
    threechoices('''Your credit card is maxed out at $1,000
    after you used it to delay foreclosure.''',
    '''You are relieved to have paid your debts in full.''', '''Pay the whole balance''', -1000, 0, 'c',
    '''If you continue to only pay the minimum,
    you will take six years to pay off your card
    and pay 50% more in the end.''','''Pay the $90 minimum''', -90, 0, 'c',
    '''You will soon face several negative consequences,
    including late fees, elevated APRs, reduced credit scores,
    and even phone calls from debt collections agencies,
    costing you in both the short term and long term.''',
    '''Don't pay any this month''', -1 * random.randint(100,200), 0, 'c')
    
def c5():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''You finally have a day off work to
    spend with your teen, but a coworker's
    unwanted shift sits up for grabs.''', '''You feel sad to not be with your teen, but that extra $80 is
    completely worth it.''', '''Claim the shift''', 80, 0, 'c', '''You may have missed out on some extra
    cash, but you enjoyed every minute of your time off.''', '''Do not claim the shift''', 0, 0, 'c')
    
def c6():
    twochoices('''Maintenance has been saying for an
    entire week they've been working on it,
    but the heating systems are still malfunctioning.''', '''The warmth is worth the combined $100 in
    costs of both the heater itself and monthly usage.''', '''Buy a heater''', -100, 0, 'c',
    '''You and your teen continue to rely on coats
    and blankets to avoid freezing to death at night.''',
    '''Wait for the heat to be fixed''', 0, 0, 'c')
    
def c7():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''An old friend you thought ghosted you
    finally calls and asks to hang out after
    learning of your plight. The only problem?
    They're only free on days you work.''', '''Your stress melts away
    until you become aware of lost wages and a job strike.''', '''Skip half a day's work''', -40, 1, 'c',
    '''You missed out on invaluable social interaction
    but knew you couldn't risk your job.''', '''Say no''', 0, 0, 'c')
    
def c8():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''While walking home from work,
    you face the unthinkable: an armed robbery.
    Unfortunately, you didn't think to buy a fake wallet
    to ward off potential muggers.''',
    '''You lost your cash and will end up spending $30
    on a new wallet and identification cards,
    but you escaped uninjured.''', '''Hand over your wallet''', -1 * random.randint(45, 75), 0, 'c',
    '''You managed to avoid getting shot, but you got pistol-whipped
    and had to miss the next day of work. Job strike for you!''', '''Fight back''', -80, 1, 'c')

def c9():
    threechoices('''Your electric and water bills are
    both due today, each roughly $100.''', '''You are relieved to know
    your utilities will remain on this month.''', '''Pay both''', -200, 0, 'c', '''You are faced with the painful task
    of choosing which utility to save and which utility to lose.''', '''Pay one''', -100, 0, 'c', '''You wonder how you'll survive
    without electricity or running water.''', '''Pay none''', 0, 0, 'c')
    
def c10():
    twochoices('''Your teen wants to join the school basketball team,
    but the uniform costs $30.''',
    '''Your teen is happy to make friends and relieve stress,
    but your grocery bill will also spike $15
    to cover his increased caloric needs.''','''Say yes''', -45, 0, 'c',
    '''Your teen is very disappointed,
    and the two of you get into a heated argument.''', '''Say no''',
    0, 0, 'c')
    
def c11():
    twochoices('''Your local community college is offering
    a $300 course in computer science,
    which may eventually score you financial security and prosperity.''', '''Having failed to anticipate the
    course's high workload, you become overwhelmed and are forced to drop it.
    No wonder so few can escape the vicious cycle of poverty.''', '''Take it''', -300, 0, 'c',
    '''Lack of affordability within higher education
    severely restricts access for low-income students.''',
    '''Skip it''', 0, 0, 'c')
    
def c12():
    twochoices('''Your teen has been offered the opportunity
    to take some of his classes next year
    at the local community college. All applicants are accepted,
    tuition-free...as long as they pay an $80 fee.''',
    '''You are optimistic your teen will eventually enroll in higher education,
    paving the way for future prosperity.''', '''Pay the money''', -80, 0, 'c', '''You are ashamed your teen will
    miss this potential shot at a better future,
    but sadly day-to-day survival is more important right now.''',
    '''Say no''', 0, 0, 'c')
    
def c13():
    threechoices('''Your landlord cannot legally hike rents
    prior to the end of leases, but he does so anyway, by $100.''',
    '''Legal assistance is extremely difficult for those in poverty to access.
    Ninety percent of landlords in eviction cases have lawyers, while the
    same is true for just 10 percent of tenants.''', '''Pay the money''', -100, 0, 'c',
    '''Yes, it's illegal, but hiring an attorney will cost you
    much more than simply accepting the elevated rent.''', '''Seek legal help''', -100, 0, 'c',
    '''Your new apartment not only carries a $200 greater rent
    but is also situated an extra 20 minutes from school and work.
    You would also be on the hook for first and last month's rent,
    so you're better off staying.''', '''Move out''', -100, 0, 'c')

def c14():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''As if yet another terrible workday
    couldn't get any worse, you come home to a
    cockroach infestation. Your landlord will neither hire an
    exterminator nor reduce your rent as compensation.''',
    '''One hundred bucks later, your apartment is roach-free.''', '''Hire one yourself''', -100, 0, 'c',
    '''The infestation worsens to the point your sleep is affected,
    costing you half a day's work and a job strike.''', '''Do nothing''', -35, 1, 'c')

def c15():
    twochoices('''Looks like your ex isn't doing well either,
    offering $75 to crash in your place tonight.''',
    '''The night brings lots of fights and little sleep,
    but that $75 sure is worth it.''', '''Say yes''', 75, 0, 'c',
    '''You regret your decision the next morning when you think of
    everything that money could have bought you.''', '''Say no''',
    0, 0, 'c')

def c16():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''You receive a phone call at work saying
    your teen has been sent home for the day due to
    severe misbehavior and that he must be supervised.''',
    '''You are forced to spend the second half of your
    workday at home disciplining your teen, prompting a job strike.''', '''Return home as requested''', -40, 1, 'c',
    '''You and your teen are ticketed for neglect and truancy,
    respectively, for $100 each.''', '''Hope he returns home by himself''', -200, 0, 'c')

def c17():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''The water cut off just as you were
    about to wash all your work clothes.''', '''Your boss sends you
    home for your smelly clothes and awards you a strike.''', '''Wear dirty clothes tomorrow''', -80, 1, 'c',
    '''Your boss understands and gives you a new uniform the next day.''', '''Buy new ones''', -30, 0, 'c')

def c18():
    threechoices('''Your teen really wants a smartphone for his birthday,
    having quarreled with you about it for weeks.''', '''The both of you feel happier as your teen enjoys his
    gadget and you enjoy your teen's better behavior.''', '''Buy him a used phone for $150''', -150, 0, 'c',
    '''Your teen is disappointed but can at least
    text friends and reach you in an emergency.''',
    '''Buy him a flip phone for $30''', -30, 0, 'c', '''Your teen's continued arguing leaves you questioning
    whether skipping that purchase was really the right decision.''', '''Buy him no phone at all''', 0, 0, 'c')
    
def c19():
    twochoices('''Your teen has been struggling with his homework,
    yet you also struggle to help him.''',
    '''Your teen's improved grades are well worth that $70.''', '''Hire a tutor''', -70, 0, 'c',
    '''Your teen's academic performance continues to worsen,
    placing him at risk of becoming yet another
    dropout in the neighborhood.''', '''Do nothing''', 0, 0, 'c')

def c20():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    threechoices( '''Your entire body is sick and achy,
    but you have to be at work in an hour.''',
    '''You learn the hard way your employer offers
    no paid sick leave and earn a job strike.''', '''Call out''', -80, 1, 'c',
    '''Your N95 mask obscures your symptoms until they worsen
    halfway through your shift, after which you are
    sent home with a job strike.''', '''Go in anyway''', -40, 1, 'c', '''Without health insurance or sick leave,
    your visit costs a combined $180, but you miraculously manage
    to convince your boss to excuse your absence.''',
    '''Visit urgent care''', -180, 0, 'c')
    
def c21():
    twochoices('''While rummaging for paperwork, you recover a vase
    from your childhood you packed while moving.''',
    '''The vase cheers you up on particularly
    bad days by evoking fond memories.''', '''Keep it''', 0, 0, 'c',
    '''You are sad to part with the vase,
    especially since it only sold for $50.''', '''Sell it''', 50, 0, 'c')
    
def c22():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''At work, you discover a misplaced wallet. Inside is $22.''',
    '''You are promptly summoned to a disciplinary meeting,
    after which you will earn at least one job strike.''',
    '''Finders keepers!''', 22, random.randint(1,3), 'c', '''You don't earn any monetary rewards but are praised for your honesty.''',
    '''Turn it in''', 0, 0, 'c')
    
def c23():
    threechoices('''You wake up to discover a bullet hole in your window from
    last night's gang shootout...as well as a notice from your landlord
    that you're on the hook for $150 in repair costs.''',
    '''The police never catch the gunmen, and you never see that $150 again.''', '''Pay up''', -150, 0, 'c',
    '''Hiring an attorney would make an even bigger dent in your wallet,
    so you're stuck paying for the window.''',
    '''Call a lawyer''', -150, 0, 'c', '''An inspection reveals your "window" as a fake,
    prompting a notice to
    either pay up or face eviction proceedings.''', '''Buy a plastic film for $30''', -180, 0, 'c')
    
def c24():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''Your usual route to work is blocked by police activity,
    and you're already running 10 minutes behind.''', '''Despite arriving only five minutes late, your supervisor says she's
    discussing with the managers whether to give you a job strike.''', '''Take a detour''', -1, random.randint(0,1), 'c',
    '''The police issue you a $100 ticket for obstructing an officer.''', '''Sprint through there''', -100, 0, 'c')
    
def c25():
    twochoices('''Your younger brother's birthday is coming up,
    but you have neither the time nor the transportation
    to visit him and the rest of the family.''', '''He appreciates the gift, especially considering your financial
    hardships, and the two of you become closer.''', '''Buy him a $40 pair of earbuds''', -40, 0, 'c',
    '''He thanks you for the kind words.''', '''Buy him a card''', -3, 0, 'c')
 
def c26():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''This terrible situation has done a serious number
    on your mental health and cognitive functioning.''',
    '''Those struggling are not only often reluctant to seek help
    but face steep price tags when they finally do.''',
    '''Obtain counseling''', -120, 0, 'c', '''Your thoughts and emotions continue to worsen,
    putting you at risk of accidents, tardiness,
    and other issues that jeopardize your job.''', '''Do nothing''', 0, random.randint(0,2), 'c')

def c27():
    twochoices('''You receive an email regarding the posting of a job
    that pays $20 an hour, double your current wages,
    and allows you to work from home. The only problem?
    You'll have to buy the company's propietary $100 software suite.''',
    '''The email turns out to be a scam.''', '''Apply''', -100, 0, 'c',
    '''High initial costs exclude many in poverty from decisions
    that return net gains, e.g. tertiary education, home buying/investing,
    or even buying healthier food to ward off disease.''', '''Pass''', 0, 0, 'c')

def c28():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    threechoices('''Your teen wakes up ill with cold- and flu-like symptoms,
    but you're scheduled to work today.''', '''With your help, your teen recovers in time to
    return to school the next day, but you earn a job strike for calling out.''', '''Stay home with them''',
    -80, 1, 'c', '''You receive a call a couple hours later
    informing you your teen was sent home
    and that you need to monitor them. Job strike for you!''',
    '''Send them to school''', -55, 1, 'c', '''You jot down some pointers
    for your teen to recover and hope for the best.''', '''Leave them home alone''', 0, 0, 'c')
    
def c29():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''You discover that your wages were
    illegally docked last time you were paid.''',
    '''Your boss insists you were lying
    despite the evidence and awards you a strike.''','''Speak to your supervisor''', -50, 1, 'c',
    '''No one there ever answers the phone,
    so you're unable to recover that missing $50.''', '''Speak to corporate''', -50, 0, 'c')

def c30():
    twochoices('''A local gym is offering discounted memberships
    to those with certain incomes, and you qualify.''',
    '''That $15 will go a long way into improving
    both your physical and mental health.''', '''Join for $15''', -15, 0, 'c',
    '''Reduced doesn't mean free. No wonder those with low incomes
    not only face food insecurity but also high rates of
    obesity and other chronic conditions.''', '''Put it off''', 0, 0, 'c')

def c31():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    threechoices('''Your knee begins to hurt like crazy when you
    get out of bed to take your first steps of the day.
    Looks like your walk to work will be a challenge.''', '''The ride cost you not only $10 but also the first few minutes
    of your shift and a reprimand from your boss.''', '''Hail a cab''', -12, random.randint(0,1), 'c',
    '''You manage to trudge into work on time after shelling out
    $65 for a brace and Ibuprofen at your local drug store.''',
    '''Buy pain relievers''', -65, 0, 'c', '''Without medical leave, you lose a day
    of pay and earn a job strike.''',
    '''Take the day off''', -80, 1, 'c')
    
def c32():
    twochoices('''Your teen receives a total of $83 from
    both friends and family for his birthday.''',
    '''Your teen at least buys enough snacks, however unhealthy,
    to slash $10 from this month's grocery bill.''',
    '''Let your teen keep the money''', 10, 0, 'c', '''Your teen is angry and only calms down
    after yet another long discussion
    of the dire need to make every penny count.''','''Take the money''', 83, 0, 'c')

def c33():
    threechoices('''Your cellphone and Internet bills are both due today, each $75.''',
    '''You are relieved to still be able to
    communicate with the outside world this month.''', '''Pay both''',
    -150, 0, 'c', '''You are forced to decide between
    sacrificing communication with your family
    and information from the web.''', '''Pay one''', -75, 0, 'c', '''You will soon no longer be able to call your
    relatives or engage in any online activities.''', '''Pay none''', 0, 0, 'c')
    
def c34():
    twochoices('''One of your relatives was seriously injured,
    and the entire family is pitching in $50.''',
    '''You wish for a speedy and full recovery.''', '''Contribute''', -50, 0, 'c',
    '''You feel somewhat like a pariah in your family
    as everyone recalls the decisions that
    put you in the position of being unable to chip in.''', '''Pass''', 0, 0, 'c')
    
def c35():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''Half of your coworkers are walking out today
    to protest the company's high profits and low employee wages.''', '''The strike was legally protected, but you
    --and all the other employees involved--were fired anyway.''', '''Join them''', 0, 3, 'c',
    '''You're certainly not the only low-wage laborer
    to remain silent to avoid risking termination.''',
    '''Keep working''', 0, 0, 'c')    
    
def c36():
    twochoices('''A major severe weather outbreak is
    expected to lash your city tonight.''',
    '''Your apartment loses power but suffers no damage.''', '''Buy boards for the windows''', -40, 0, 'c',
    '''A straight-line wind gust hurls a loose object through your window,
    shattering it and letting in floodwater,
    causing a total of more than $200 in damages.''', '''Hope for the best''', -1 * random.randint(201, 300), 0, 'c')    

def c37():
    twochoices('''You've had no time to clean your bathroom,
    and you now notice mildew running rampant.''',
    '''That $170 would have still been yours
    had you spent just one night per week cleaning
    rather than mindlessly surfing the Internet.''', '''Hire a maid''', -170, 0, 'c',
    '''The fungus has worsened to the point of being
    resistant to Clorox and will only worsen further.''', '''Ignore it''', 0, 0, 'c')
    
def c38():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''On the way to work, you find a bunch of
    $100 bills strewn about the street,
    which is extremely suspicious considering the significant
    drug and gang activity on your block.''',
    '''You feel queasy an hour into your shift, are sent to the hospital,
    and learn the bills were laced with fentanyl.
    Your boss excuses your absence, but you face a total of
    $270 in lost wages and immediate medical costs.''', '''Claim the cash''', -270, 0, 'c',
    '''You breathe a sigh of relief as the police later report
    the bills tested positive for fentanyl
    after an officer in the area seized them for testing.''', '''Don't claim the cash''', 0, 0, 'c')
    
def c39():
    threechoices('''You weren't paying attention and
    accidentally dropped your uninsured phone.''',
    '''You are thankful your wallet could take the sudden hit.''', '''Buy a new smartphone for $500''', -500, 0, 'c',
    '''This one performs considerably less well but still isn't cheap.''', '''Buy a used smartphone for $150''', -150, 0, 'c',
    '''You'll no longer be able to use the Internet for anything,
    including checking the weather, while out,
    but this phone's all you can afford right now.''', '''Buy a flip phone for $30''', -30, 0, 'c')
    
def c40():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''While walking to work in a blizzard,
    the wind grabs your umbrella and tosses it through a
    window of the managers' and supervisors' offices.''',
    '''Your boss appreciates your honesty
    and only requests you pay half of the restitution amount.
    But you're still paying full price for a new umbrella.''', '''Report the damage''', -130, 0, 'c',
    '''You were identified as the perpetrator from
    security camera footage and have been fired
    and summoned to small claims court, which can only be avoided
    by paying the $230 for a replacement window.''', '''Do nothing''', -230, 3, 'c')
    
def c41():
    threechoices('''Your teen wants to go on a date with
    a classmate to the local cinema. Tickets are $10 each.''', '''Your teen has just begun their first romantic relationship,
    significantly reducing both their--and your--stress levels.''', '''Pay for both''', -20, 0, 'c',
    '''Your teen never becomes romantically involved with this person,
    but the two of them still remain friends.''', '''Pay for one''', -10, 0, 'c', '''This potential romantic partner dumps your
    teen for not showing up to date night.''', '''Say no''', 0, 0, 'c')
   
def c42():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    threechoices('''The both of you are awokened by loud music
    from a neighboring apartment, but this isn't the first
    nighttime disruption linked to that specific unit.''',
    '''He apparently believes that your story is
    either unimportant or fabricated altogether.''',
    '''Report it to your landlord''', 0, 0, 'c', '''The neighbors quiet down by the time they show up,
    and the police cite you for false reporting.''','''Report it to the police''', -150, 0, 'c',
    '''Your neighbors become enraged and shove you to the ground,
    causing injuries. Looks like you're going to miss work tomorrow
    and need some medicine, costing you $200 and a job strike.''', '''Confront your neighbors directly''', -200, 1, 'c')

def c43():
    twochoices('''Your teen needs to replace one of his textbooks
    with his own money amid recent school budget cuts.''',
    '''While genuinely unfair, this expense is necessary to give your
    teen any chance at passing school this year.''',
    '''Replace it''', -30, 0, 'c', '''No wonder so many students in this neighborhood
    are at risk of dropping or failing out.''', '''Say no''', 0, 0, 'c')
    
def c44():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    twochoices('''A local political organization is organizing
    a rally against street crime and violence.
    But what really jumps out at you is the free food.''', '''The trivial grocery savings vanish when the protest
    deteriorates into a riot and you find yourself in handcuffs.
    You're eventually released without charges, but not soon enough
    to make it to work on time the next day. You are given a strike.''', '''Attend''', -26, 1, 'c',
    '''The event turns violent, triggering a heavy police response
    and mass arrests. It's why many people,
    especially those in marginalized groups, are afraid to
    make their voices heard, even in a free country.''',
    '''Don't attend''', 0, 0, 'c')

def c45():
    twochoices('''Your one and only coat just ripped,
    and winter is still far from over.''',
    '''It may not be cheap, but it sure makes
    your daily commutes bearable again.''', '''Buy a new one for $50''',
    -50, 0, 'c', '''That coat also rips after a week,
    after which you reluctantly buy an unused one.''',
    '''Buy a used one for $10''', -60, 0, 'c')
       
def c46():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l1', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l1', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 'c')
    
def c47():
    global payday
    if payday == 'FIRED':
        select('c')
        return
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l1', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l1', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 'c')  

def c48():
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l1', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l1', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 'c')

def c49():
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l1', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l1', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 'c')

def c50():
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l1', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l1', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 'c')
    
def s1():
    twochoices('''While rummaging for paperwork, you recover a vase
    from your childhood you packed while moving.''',
    '''The vase cheers you up on particularly
    bad days by evoking fond memories.''', '''Keep it''', 0, 0, 's',
    '''You are sad to part with the vase,
    especially since it only sold for $50.''', '''Sell it''', 50, 0, 's')
    
def s2():
    twochoices('''Your teen has been offered the opportunity
    to take some of his classes next year
    at the local community college. All are accepted,
    tuition-free...as long as they pay an $80 application fee.''',
    '''You are optimistic your teen will eventually enroll in higher education,
    paving the way for future prosperity.''', '''Pay the money''', -80, 0, 's', '''You are ashamed your teen will
    miss this potential shot at a better future,
    but sadly day-to-day survival is more important right now.''',
    '''Say no''', 0, 0, 's')

def s3():
    threechoices('''Your cellphone and Internet bills are both due today, each $75.''',
    '''You are relieved to still be able to
    communicate with the outside world this month.''', '''Pay both''',
    -150, 0, 's', '''You are forced to decide between
    sacrificing communication with your family
    and information from the web.''', '''Pay one''', -75, 0, 's', '''You will soon no longer be able to call your
    relatives or engage in any online activities.''', '''Pay none''', 0, 0, 's')

def s4():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    threechoices( '''Your entire body is sick and achy,
    but you have to be at work in an hour.''',
    '''You learn the hard way your employer offers
    no paid sick leave and earn a job strike.''', '''Call out''', -80, 1, 's',
    '''Your N95 mask obscures your symptoms until they worsen
    halfway through your shift, after which you are
    sent home with a job strike.''', '''Go in anyway''', -40, 1, 's', '''Without health insurance or sick leave,
    your visit costs a combined $180, but you miraculously manage
    to convince your boss to excuse your absence.''',
    '''Visit urgent care''', -180, 0, 's')

def s5():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    twochoices('''As if yet another terrible workday
    couldn't get any worse, you come home to a
    cockroach infestation. Your landlord will neither hire an
    exterminator nor reduce your rent as compensation.''',
    '''One hundred bucks later, your apartment is roach-free.''', '''Hire one yourself''', -100, 0, 's',
    '''The infestation worsens to the point your sleep is affected,
    costing you half a day's work and a job strike.''', '''Do nothing''', -35, 1, 's')

def s6():
    twochoices('''Maintenance has been saying for an
    entire week they've been working on it,
    but the heating systems are still malfunctioning.''', '''The warmth is worth the combined $100 in
    costs of both the heater itself and monthly usage.''', '''Buy a heater''', -100, 0, 's',
    '''You and your teen continue to rely on coats
    and blankets to avoid freezing to death at night.''',
    '''Wait for the heat to be fixed''', 0, 0, 's')
    
def s7():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    twochoices('''An old friend you thought ghosted you
    finally calls and asks to hang out after
    learning of your plight. The only problem?
    They're only free on days you work.''', '''Your stress melts away
    until you become aware of lost wages and a job strike.''', '''Skip half a day's work''', -40, 1, 's',
    '''You missed out on invaluable social interaction
    but knew you couldn't risk your job.''', '''Say no''', 0, 0, 's')
    
def s8():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    twochoices('''While walking to your apartment,
    you face the unthinkable: an armed robbery.
    Unfortunately, you didn't think to buy a fake wallet
    to ward off potential muggers.''',
    '''You lost your cash and will end up spending $30
    on a new wallet and identification cards,
    but you escaped uninjured.''', '''Hand over your wallet''', -1 * random.randint(45, 75), 0, 's',
    '''You managed to avoid getting shot, but you got pistol-whipped
    and had to miss the next day of work. Job strike for you!''', '''Fight back''', -80, 1, 's')

def s9():
    twochoices('''Your local auto parts store is advertising a special
    part for your car that could greatly increase its fuel economy.''',
    '''You hope the part will eventually pay for itself or
    remain a net financial loss.''', '''Buy it''', -100, 0, 's',
    '''Unfortunately, this potential money gainer is just one of many
    for which your wallet can't stomach the initial blow.''', '''Pass''',
    0, 0, 's')

def s10():
    twochoices('''Your teen is performing in a school play,
    but tickets cost $20.''', '''Your teen appreciates you coming out,
    and you appreciate the play.''', '''Attend''', -20, 0, 's',
    '''Your teen is disappointed but understands.''',
    '''Don't attend''', 0, 0, 's')

def s11():
    twochoices('''A passerby notices the stressed look on your face
    and offers you a cigarette.''', '''You depend on smoking to suppress your anxiety and loneliness,
    costing you at least $100 over the course of the month.''',
    '''Say yes''', -1 * random.randint(100, 150), 0, 's', '''This decision was a tough one to make
    considering everything going on, but it will protect
    both your wallet and health.''', '''Say no''', 0, 0, 's')

def s12():
    threechoices('''You and your teen want to compete in a road race
    this weekend, which costs $25 per runner.''', '''The both of you bond together
    and enjoy the fun, low-stakes competition.''', '''Sign you and you teen up''',
    -50, 0, 's', '''While you wanted to run, you're glad your teen could
    and that you could at least help along the course.''',
    '''Volunteer and sign your teen up''', -25, 0, 's', '''Now you know why low-income families
    tend to be at higher risk for dysfunction.''', '''Don't attend''', 0, 0, 's')

def s13():
    twochoices('''Your one and only coat just ripped,
    and winter is still far from over.''',
    '''It may not be cheap, but it sure makes
    the cold bearable again.''', '''Buy a new one for $50''',
    -50, 0, 's', '''That coat also rips after a week,
    after which you reluctantly buy an unused one.''',
    '''Buy a used one for $10''', -60, 0, 's')
       
def s14():
    threechoices('''You wake up to discover a bullet hole in your window from
    last night's gang shootout...as well as a notice from your landlord
    that you're on the hook for $150 in repair costs.''',
    '''The police never catch the gunmen, and you never see that $150 again.''', '''Pay up''', -150, 0, 's',
    '''Hiring an attorney would make an even bigger dent in your wallet,
    so you're stuck paying for the window.''',
    '''Call a lawyer''', -150, 0, 's', '''An inspection reveals your "window" as a fake,
    prompting a notice to
    either pay up or face eviction proceedings.''', '''Buy a plastic film for $30''', -180, 0, 's')

def s15():
    twochoices('''Looks like your ex isn't doing well either,
    offering $75 to crash in your place tonight.''',
    '''The night brings lots of fights and little sleep,
    but that $75 sure is worth it.''', '''Say yes''', 75, 0, 's',
    '''You regret your decision the next morning when you think of
    everything that money could have bought you.''', '''Say no''',
    0, 0, 's')

def s16():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    twochoices('''The water cut off just as you were
    about to wash all your work clothes.''', '''Your boss sends you
    home for your smelly clothes and awards you a strike.''', '''Wear dirty clothes tomorrow''', -80, 1, 's',
    '''Your boss understands and gives you a new uniform the next day.''', '''Buy new ones''', -30, 0, 's')

def s17():
    threechoices('''Your teen really wants a smartphone for his birthday,
    having quarreled with you about it for weeks.''', '''The both of you feel happier as your teen enjoys his
    gadget and you enjoy your teen's better behavior.''', '''Buy him a used phone for $150''', -150, 0, 's',
    '''Your teen is disappointed but can at least
    text friends and reach you in an emergency.''',
    '''Buy him a flip phone for $30''', -30, 0, 's', '''Your teen's continued arguing leaves you questioning
    whether skipping that purchase was really the right decision.''', '''Buy him no phone at all''', 0, 0, 's')
    
def s18():
    twochoices('''Your teen has been struggling with his homework,
    yet you also struggle to help him.''',
    '''Your teen's improved grades are well worth that $70.''', '''Hire a tutor''', -70, 0, 's',
    '''Your teen's academic performance continues to worsen,
    placing him at risk of becoming yet another
    dropout in the neighborhood.''', '''Do nothing''', 0, 0, 's')

def s19():
    threechoices('''Your electric and water bills are
    both due today, each roughly $100.''', '''You are relieved to know
    your utilities will remain on this month.''', '''Pay both''', -200, 0, 's', '''You are faced with the painful task
    of choosing which utility to save and which utility to lose.''', '''Pay one''', -100, 0, 's', '''You wonder how you'll survive
    without electricity or running water.''', '''Pay none''', 0, 0, 's')

def s20():
    threechoices('''Your car loan and insurance payments are
    both due today, each $200.''', '''You will be able to continue to drive
    legally, without fear of impoundment or arrest.''',
    '''Pay both''', -400, 0, 's', '''You will have to decide whether to take your chances
    with the creditors or the police. And if you're pulled over,
    you'll no longer be able to commute to your job.''', '''Pay one''', -200, 0, 's',
    '''Your car is soon seized, after which you lose your job.''', '''Pay none''', 0, 3, 's')

def s21():
    twochoices('''You have been offered $100 to monitor a neighbor's
    small child. The only problem? You're supposed to be at work.''',
    '''You ruminate over whether that $20 net gain was worth that strike.''',
    '''Watch the kid''', 23, 1, 's', '''Remaining in good standing at work is more
    important than a little money, and your neighbor understands.''', '''Go to work''',
    0, 0, 's')
    
def s22():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    twochoices('''Having gotten out the door a little late, you were
    planning on grabbing some McDonald's on the way to work.
    But traffic is extra crazy today.''', '''Apparently you weren't the only person
    running behind today considering your 20-minute wait
    for your food. You may be getting a strike for clocking in tardy.''',
    '''Grab a bite anyway''', -10, random.randint(0,1), 's', '''You are so ravenous and irritable that you
    drop a rude comment on the job, costing you a strike.''', '''Go hungry''', 0, 1, 's')

def s23():
    twochoices('''Your teen wants to join the school basketball team,
    but the uniform costs $30.''',
    '''Your teen is happy to make friends and relieve stress,
    but your grocery bill will also spike $15
    to cover his increased caloric needs.''','''Say yes''', -45, 0, 's',
    '''Your teen is very disappointed,
    and the two of you get into a heated argument.''', '''Say no''',
    0, 0, 's')
    
def s24():
    twochoices('''Your local community college is offering
    a $300 course in computer science,
    which may eventually score you financial security and prosperity.''', '''Having failed to anticipate the
    course's high workload, you become overwhelmed and are forced to drop it.
    No wonder so few can escape the vicious cycle of poverty.''', '''Take it''', -300, 0, 's',
    '''Lack of affordability within higher education
    severely restricts access for low-income students.''',
    '''Skip it''', 0, 0, 's')

def s25():
    twochoices('''Your younger brother's birthday is coming up,
    but you have neither the time nor the transportation
    to visit him and the rest of the family.''', '''He appreciates the gift, especially considering your financial
    hardships, and the two of you become closer.''', '''Buy him a $40 pair of earbuds''', -40, 0, 's',
    '''He thanks you for the kind words.''', '''Buy him a card''', -3, 0, 's')
 
def s26():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    twochoices('''This terrible situation has done a serious number
    on your mental health and cognitive functioning.''',
    '''Those struggling are not only often reluctant to seek help
    but face steep price tags when they finally do.''',
    '''Obtain counseling''', -120, 0, 's', '''Your thoughts and emotions continue to worsen,
    putting you at risk of accidents, tardiness,
    and other issues that jeopardize your job.''', '''Do nothing''', 0, random.randint(0,2), 's')

def s27():
    twochoices('''You receive an email regarding the posting of a job
    that pays $20 an hour, double your current wages,
    and allows you to work from home. The only problem?
    You'll have to buy the company's propietary $100 software suite.''',
    '''The email turns out to be a scam.''', '''Apply''', -100, 0, 's',
    '''High initial costs exclude many in poverty from decisions
    that return net gains, e.g. tertiary education, home buying/investing,
    or even buying healthier food to ward off disease.''', '''Pass''', 0, 0, 's')

def s28():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    threechoices('''Your teen wakes up ill with cold- and flu-like symptoms,
    but you're scheduled to work today.''', '''With your help, your teen recovers in time to
    return to school the next day, but you earn a job strike for calling out.''', '''Stay home with them''',
    -80, 1, 's', '''You receive a call a couple hours later
    informing you your teen was sent home
    and that you need to monitor them. Job strike for you!''',
    '''Send them to school''', -55, 1, 's', '''You jot down some pointers
    for your teen to recover and hope for the best.''', '''Leave them home alone''', 0, 0, 's')
    
def s29():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    twochoices('''You discover that your wages were
    illegally docked last time you were paid.''',
    '''Your boss insists you were lying
    despite the evidence and awards you a strike.''','''Speak to your supervisor''', -50, 1, 's',
    '''No one there ever answers the phone,
    so you're unable to recover that missing $50.''', '''Speak to corporate''', -50, 0, 's')

def s30():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    threechoices('''You notice several warning lights appear in your car,
    which is very old and has a history of breakdowns.''', '''You notice a big difference in how
    your car runs, including enhanced fuel efficiency.''',
    '''Take it to a mechanic''', -1 * random.randint(430, 470), 0, 's',
    '''Completing the repairs yourself only cost you $90
    but were very difficult and took until midnight to finish.
    You may or may not oversleep for work the next day.''', '''Troubleshoot it yourself''',
    -1 * random.randint(90,150), random.randint(0,1), 's',
    '''Your car breaks down the next day, forcing you to take an Uber to work,
    miss half a day, earn a strike, and pay approximately
    $50 more in transportation costs each month.''',
    '''Hope nothing's really wrong''', -1 * random.randint(70, 100), 1, 's')
    
def s31():
    twochoices('''Your city is raising money to improve its schools
    following recent state budget cuts.''', '''You are proud to contribute, especially
    as your teen constantly complains of overcrowding,
    understaffing, and subpar books.''', '''Donate $30''', -30, 0, 's',
    '''You are disappointed to be unable to help, especially
    considering your teen's disdain for his subpar learning environment.''',
    '''Pass''', 0, 0, 's')

def s32():
    twochoices('''You've been struggling with social isolation
    due to your financial troubles and past poor decisions.
    A trip to the bar may deliver relief...
    if you can shell out $30 for a babysitter.''', '''Everyone there either is already taken or
    rejected you, and you return home feeling even more lonely.''', '''Pay the $30''', -30, 0,
    's','''You feel like you missed out on a night of fun as you see cute couples
    from the bar on your social media feeds the next day.''', '''Stay home''', 0, 0, 's')

def s33():
    threechoices('''You know their radar is unreliable, but your apartment
    complex's security guards insist you were speeding in the parking lot.''',
    '''You will constantly fear having to
    drop another $50 over some technical malfunction.''', '''Pay up''',
    -50, 0, 's', '''The exorbant fees and wait times for legal assistance
    in your neighborhood are much worse than simply paying the $50 penalty.''',
    '''Seek legal help''', -50, 0, 's', '''Your landlord finds out soon enough
    and slaps you with a much larger penalty,
    along with the threat of eviction
    for any delay in payment.''', '''Hope they realize the error''', -150, 0, 's')

def s34():
    twochoices('''One of your relatives is seriously ill,
    and the entire family is pitching in $50.''',
    '''You wish for a speedy and full recovery.''', '''Contribute''', -50, 0, 's',
    '''You feel somewhat like a pariah in your family
    as everyone recalls the decisions that
    put you in the position of being unable to chip in.''', '''Pass''', 0, 0, 's')
    
def s35():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    twochoices('''Half of your coworkers are walking out today
    to protest the company's high profits and low employee wages.''', '''The strike was legally protected, but you
    --and all the other employees involved--were fired anyway.''', '''Join them''', 0, 3, 's',
    '''You're certainly not the only low-wage laborer
    to remain silent to avoid risking termination.''',
    '''Keep working''', 0, 0, 's')    
    
def s36():
    twochoices('''A major severe weather outbreak is
    expected to lash your city tonight.''',
    '''Your apartment loses power but suffers no damage.''', '''Buy boards for the windows''', -40, 0, 's',
    '''A straight-line wind gust hurls a loose object through your window,
    shattering it and letting in floodwater,
    causing a total of more than $200 in damages.''', '''Hope for the best''', -1 * random.randint(201, 300), 0, 's')    

def s37():
    twochoices('''You've had no time to clean your bathroom,
    and you now notice mildew running rampant.''',
    '''That $170 would have still been yours
    had you spent just one night per week cleaning
    rather than mindlessly surfing the Internet.''', '''Hire a maid''', -170, 0, 's',
    '''The fungus has worsened to the point of being
    resistant to Clorox and will only worsen further.''', '''Ignore it''', 0, 0, 's')

def s38():
    twochoices('''Your suburb is experiencing a widespread 
    broadband outage, which includes your apartment.''',
    '''You hope the network is fixed by the next day
    considering the cafe's $10 hourly rate.''',
    '''Visit your local Internet cafe''', -1 * random.randint(20, 120), 0, 's',
    '''Each hour of hotspot usage consumes an excess gigabyte
    of data and costs you $15. So you were better off
    hitting up that Internet cafe.''',
    '''Use your phone as a personal hotspot''', -1 * random.randint(30, 180), 0, 's')

def s39():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    threechoices('''You've been noticing your teen casually
    discussing drugs and weapons in the days since they've
    told you he's found a new group of friends.''',
    '''You leave work early to check on your teen, who you observe
    being nudged into trying illicit drugs. The eventual arrest of
    these "friends", who are actually wanted suspects,
    as well as a $200 reward from the police,
    are well worth that job strike.''', '''Investigate''', 120, 1, 's',
    '''The virtual therapy session cultivated positive behavioral
    shifts but set you back $75.''',
    '''Seek counseling''', -75, 0, 's',
    '''You set new rules for your teen that end the 
    hanging out with the questionable kids.
    But he becomes angry and punches a hole in a wall,
    putting you on the hook for repairs.''',
    '''Discuss with your teen''', -120, 0, 's')

def s40():
    twochoices('''Your teen receives a total of $83 from
    both friends and family for his birthday.''',
    '''Your teen at least buys enough snacks, however unhealthy,
    to slash $10 from this month's grocery bill.''',
    '''Let your teen keep the money''', 10, 0, 's', '''Your teen is angry and only calms down
    after yet another long discussion
    of the dire need to make every penny count.''','''Take the money''', 83, 0, 's')
    
def s41():
    threechoices('''You weren't paying attention and
    accidentally dropped your uninsured phone.''',
    '''You are thankful your wallet could take the sudden hit.''', '''Buy a new smartphone for $500''', -500, 0, 's',
    '''This one performs considerably less well but still isn't cheap.''', '''Buy a used smartphone for $150''', -150, 0, 's',
    '''You'll no longer be able to use the Internet for anything,
    including checking the weather, while out,
    but this phone's all you can afford right now.''', '''Buy a flip phone for $30''', -30, 0, 's')
    
def s42():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    twochoices('''You normally take Exit 19 on your morning commute,
    but you got distracted and missed it.''', '''That maneuver is extremely dangerous.
    You're lucky you were ticketed $150
    (and still made it to work on time)
    rather than fatally rear-ended.''', '''Back up to the exit''', -150, 0, 's',
    '''The heavy traffic makes you late for work
    and costs you a strike, but you made the safer choice.''',
    '''Continue to Exit 21 and double-back''', -20, 1, 's')
    
def s43():
    threechoices('''Your credit card is maxed out at $1,000
    after you used it to delay foreclosure.''',
    '''You are relieved to have paid your debts in full.''', '''Pay the whole balance''', -1000, 0, 's',
    '''If you continue to only pay the minimum,
    you will take six years to pay off your card
    and pay 50% more in the end.''','''Pay the $90 minimum''', -90, 0, 's',
    '''You will soon face several negative consequences,
    including late fees, elevated APRs, reduced credit scores,
    and even phone calls from debt collections agencies,
    costing you in both the short term and long term.''',
    '''Don't pay any this month''', -1 * random.randint(100,200), 0, 's')
    
def s44():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    twochoices('''You finally have a day off work to
    spend with your teen, but a coworker's
    unwanted shift sits up for grabs.''', '''You feel sad to not be with your teen, but that extra $80 is
    completely worth it.''', '''Claim the shift''', 80, 0, 's', '''You may have missed out on some extra
    cash, but you enjoyed every minute of your time off.''', '''Do not claim the shift''', 0, 0, 's')

def s45():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    threechoices('''The both of you are awokened by loud music
    from a neighboring apartment, but this isn't the first
    nighttime disruption linked to that specific unit.''',
    '''He apparently believes that your story is
    either unimportant or fabricated altogether.''',
    '''Report it to your landlord''', 0, 0, 's', '''The neighbors quiet down by the time they show up,
    and the police cite you for false reporting.''','''Report it to the police''', -150, 0, 's',
    '''Your neighbors become enraged and shove you to the ground,
    causing injuries. Looks like you're going to miss work tomorrow
    and need some medicine, costing you $200 and a job strike.''', '''Confront your neighbors directly''', -200, 1, 's')
    
def s46():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l2', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l2', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 's')
    
def s47():
    global payday
    if payday == 'FIRED':
        select('s')
        return
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l2', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l2', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 's')
    
def s48():
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l2', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l2', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 's')
    
def s49():
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l2', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l2', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 's')
    
def s50():
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l2', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l2', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 's')
    
def r1():
    threechoices('''Upon waking up, you discover a bat in your bedroom.''', '''The sudden loss of $300 is much better
    than the sudden loss of your life to rabies,
    a rare but deadly virus that is almost
    100% fatal once symptoms begin.''', '''Go to the doctor''', -300, 0, 'r',
    '''The bat tests positive for rabies, so you're not only paying
    to drive to (and from) the county health department but also
    for vaccinations as this virus is deadly.''', '''Capture him for testing''', -360, 0, 'r', '''That's an extremely dangerous choice.
    If that bat is indeed rabid and made contact with your skin,
    you will face certain death within weeks or months.''', '''Do nothing''', 0, 0, 'r')
    
def r2():
    twochoices('''While rummaging for paperwork, you recover a vase
    from your childhood you packed while moving.''',
    '''The vase cheers you up on particularly
    bad days by evoking fond memories.''', '''Keep it''', 0, 0, 'r',
    '''You are sad to part with the vase,
    especially since it only sold for $50.''', '''Sell it''', 50, 0, 'r')
    
def r3():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    threechoices('''You notice several warning lights appear in your car,
    which is very old and has a history of breakdowns.''', '''You notice a big difference in how
    your car runs, including enhanced fuel efficiency.''', '''Take it to a mechanic''', -1 * random.randint(430, 470), 0, 'r',
    '''Completing the repairs yourself only cost you $90
    but were very difficult and took until midnight to finish.
    You may or may not oversleep for work the next day.''', '''Troubleshoot it yourself''',
    -1 * random.randint(90,150), random.randint(0,1), 'r',
    '''Your car breaks down the next day, forcing you to take an Uber to work,
    miss half a day, earn a strike, and pay approximately
    $80 more in transportation costs each month.''', '''Hope nothing's really wrong''', -1 * random.randint(100, 150), 1, 'r')

def r4():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    twochoices('''Your main route to work is flooded.''', '''You show up an hour late, attracting a strike.''',
    '''Take a detour''', -11, 1, 'r', '''The water is much deeper than you were expecting,
    causing your engine to stall. You then sit on the side of the road all day
    awaiting repairs, which, despite being
    covered by insurance, set you back $75.
    You also have lost wages and a job strike to worry about.''', '''Take a chance''', -155, 1, 'r')

def r5():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    twochoices('''A Tornado Watch has been posted for your county.
    And they're saying it'll really be bad this time.''', '''No tornadoes hit your area, but your home
    took some damage from a severe straight-line gust.
    Your relative will support you until repairs are complete,
    and your only new costs will be slightly higher gas expenses.''',
    '''Flee to a relative's house''', -1 * random.randint(50, 90), 0, 'r',
    '''A thunderstorm boasting 80-mile-per-hour wind gusts
    struck your area just after midnight, damaging your mobile home
    and injuring you to the point of requiring urgent care and
    sidelining you from work for a day. You are given a strike.''',
    '''Stay in your mobile home''', -1 * random.randint(140, 170), 1, 'r')

def r6():
    threechoices('''Despite being not allowed to do so during your lease,
    your landlord hikes your rent by $100.''',
    '''Legal assistance is extremely difficult for those in poverty to access.
    Ninety percent of landlords in eviction cases have lawyers, while the
    same is true for just 10 percent of tenants.''', '''Pay the money''', -100, 0, 'r',
    '''Yes, it's illegal, but hiring an attorney will cost you
    much more than simply accepting the elevated rent.''', '''Seek legal help''', -100, 0, 'r',
    '''The cost of burning all that gas to stay warm each night
    would easily exceed your now $400 rent over the course
    of a month. So you're better off staying.''', '''Live in your car''', -100, 0, 'r')
    
def r7():
    twochoices('''Drip, drop, is that what I think it is? You notice a
    a small but growing puddle of water in your bedroom.''',
    '''Repairs set you back a total of $150.''', '''Have your roof fixed''',
    -150, 0, 'r', '''The leak continues to expand, threatening the integrity
    of both your floor and your roof.''', '''Ignore it''', 0, 0, 'r')

def r8():
    twochoices('''One of your neighbors, who is going on a date,
    is offering you $50 to babysit their young child.''',
    '''You may have been exhausted after a long day of working
    (and commuting!), but the money is well worth it.''',
    '''Take the job''', 50, 0, 'r', '''Your neighbor is disappointed to be
    unable to go out.''', '''Skip the job''', 0, 0, 'r')

def r9():
    twochoices('''Your teen is offered a job on a neighbor's farmland,
    but work takes place during school hours.''', '''The work will add $150 to the monthly household income,
    but your teen will need to take classes online,
    increasing the risk of not graduating on time.''', '''Take the job''', 150, 0, 'r',
    '''That extra $150 per month would have been nice,
    but a high school diploma would open much better-paying
    jobs to your teen.''', '''Stay in school''', 0, 0, 'r')

def r10():
    threechoices('''Your teen has finally found a potential romantic partner.
    The only problem? They live on the opposite side of town.''',
    '''Your teen's increased happiness is worth every penny
    you shelled out to drive him to and from.''', '''Drive him there''',
    -22, 0, 'r', '''The video chats add up and exceed your monthly
    data cap, adding an extra $10 to your Internet bill
    (you chose a metered plan with low baseline costs)''',
    '''Allow a "date" over FaceTime''', -10, 0, 'r',
    '''This person dumps your teen, stirring both sadness
    and resentment towards you.''', '''Say no''', 0, 0, 'r')

def r11():
    threechoices('''Your car loan and insurance payments are
    both due today, each $200.''', '''You will be able to continue to drive
    legally, without fear of impoundment or arrest.''',
    '''Pay both''', -400, 0, 'r', '''You will have to decide whether to take your chances
    with the creditors or the police. And if you're pulled over,
    you'll no longer be able to commute to your job.''', '''Pay one''', -200, 0, 'r',
    '''Your car is soon seized, after which you lose your job.''', '''Pay none''', 0, 3, 'r')

def r12():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    twochoices('''You overhear coworkers discussing scavenging the county
    landfill for cash after observing a dollar bill in a trash can.''',
    '''You recover a decent sum of money but are detected by security cameras.
    In the end, you are given a $100 citation for trespassing and fired.''',
    '''Join them''', random.randint(50, 90), 3, 'r', '''Your boss thanks you and warns the rest of
    the team not to trespass in the landfill.''', '''Report them''', 0, 0, 'r')

def r13():
    threechoices('''As an outsider in a small town, you struggle
    to fit in and make friends.''', '''You begin to bond with the townsfolk
    in spite of the steep price tag.''', '''Join a club for $50''', -50, 0, 'r',
    '''You know it's not ideal but don't see a cheap alternative.''',
    '''Join a dating site and video chat (uses extra data)''', -15, 0, 'r',
    '''Your loneliness will soon roar back,
    even worse than it is now.''', '''Play video games''', 0, 0, 'r')

def r14():
    threechoices('''Your heater broke, but winter isn't completely over yet.''',
    '''The return of warmth to your home is worth that $130.''',
    '''Buy a new heater now''', -160, 0, 'r',
    '''You and your teen struggle to adapt to the cold nights.''',
    '''Wait until next winter''', 0, 0, 'r', '''This solution may not be ideal, but
    it's the only one you can afford.''', '''Buy more blankets and coats''',
    -80, 0, 'r')

def r15():
    twochoices('''As the sun's peak altitude increases, you begin to
    notice you teen's face turning red.''', '''It's crucial in the prevention
    of burns and eventual skin cancer.''', '''Buy sunscreen''', -10, 0, 'r',
    '''Continued unprotected UV exposure will put your
    teen at risk for more burns and eventually skin cancer.''',
    '''Do nothing''', 0, 0, 'r')

def r16():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    twochoices('''The water cut off just as you were
    about to wash all your work clothes.''', '''Your boss sends you
    home for your smelly clothes and awards you a strike.''', '''Wear dirty clothes tomorrow''', -80, 1, 'r',
    '''Your boss understands and gives you a new uniform the next day.''', '''Buy new ones''', -30, 0, 'r')

def r17():
    threechoices('''Your teen really wants a smartphone for his birthday,
    having quarreled with you about it for weeks.''', '''The both of you feel happier as your teen enjoys his
    gadget and you enjoy your teen's better behavior.''', '''Buy him a used phone for $150''', -150, 0, 'r',
    '''Your teen is disappointed but can at least
    text friends and reach you in an emergency.''',
    '''Buy him a flip phone for $30''', -30, 0, 'r', '''Your teen's continued arguing leaves you questioning
    whether skipping that purchase was really the right decision.''', '''Buy him no phone at all''', 0, 0, 'r')

def r18():
    twochoices('''You've been struggling with social isolation
    due to your financial troubles and past poor decisions.
    A trip to the bar in the next town over may deliver relief...
    if you can afford the 50-mile drive.''', '''Everyone there either is already taken or
    rejected you, and you return home feeling even more lonely.''',
    '''Pay the $30''', -1 * random.randint(23, 37), 0,
    'r','''You feel like you missed out on a night of fun as you see cute couples
    from the bar on your social media feeds the next day.''', '''Stay home''', 0, 0, 'r')

def r19():
    twochoices('''Your local auto parts store is advertising a special
    part for your car that could greatly increase its fuel economy.''',
    '''You hope the part will eventually pay for itself or
    remain a net financial loss.''', '''Buy it''', -100, 0, 'r',
    '''Unfortunately, this potential money gainer is just one of many
    for which your wallet can't stomach the initial blow.''', '''Pass''',
    0, 0, 'r')

def r20():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    twochoices('''A local group of farmers will host a rally
    to protest the buying of their lands by a large corporation.
    You also strongly oppose the buyout
    and want to make your voice heard.''', '''The event unexpectedly turns violent,
    after which you're caught in a wave of mass arrests
    and jailed. You're eventually released but not in time
    for work the next day, netting you a strike.''', '''Join''', -45, 1, 'r',
    '''You later hear the protest escalated into a riot
    and were relieved to remain uninvolved.''', '''Don't join''', 0, 0, 'r')

def r21():
    threechoices('''You weren't paying attention and
    accidentally dropped your uninsured phone.''',
    '''You are thankful your wallet could take the sudden hit.''',
    '''Buy a new smartphone for $500''', -500, 0, 'r',
    '''This one performs considerably less well but still isn't cheap.''',
    '''Buy a used smartphone for $150''', -150, 0, 'r',
    '''You'll no longer be able to use the Internet for anything,
    including checking the weather, while out,
    but this phone's all you can afford right now.''',
    '''Buy a flip phone for $30''', -30, 0, 'r')
    
def r22():
    twochoices('''Your younger brother's birthday is coming up,
    but you have neither the time nor the transportation
    to visit him and the rest of the family.''',
    '''He appreciates the gift, especially considering your financial
    hardships, and the two of you become closer.''',
    '''Buy him a $40 pair of earbuds''', -40, 0, 'r',
    '''He thanks you for the kind words.''', '''Buy him a card''', -3, 0, 'r')
 
def r23():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    twochoices('''This terrible situation has done a serious number
    on your mental health and cognitive functioning.''',
    '''Those struggling are not only often reluctant to seek help
    but face steep price tags when they finally do.''',
    '''Obtain counseling''', -120, 0, 'r', '''Your thoughts and emotions continue to worsen,
    putting you at risk of accidents, tardiness,
    and other issues that jeopardize your job.''', '''Do nothing''', 0, random.randint(0,2), 'r')

def r24():
    twochoices('''You receive an email regarding the posting of a job
    that pays $20 an hour, double your current wages,
    and allows you to work from home. The only problem?
    You'll have to buy the company's propietary $100 software suite.''',
    '''The email turns out to be a scam.''', '''Apply''', -100, 0, 'r',
    '''High initial costs exclude many in poverty from decisions
    that return net gains, e.g. tertiary education, home buying/investing,
    or even buying healthier food to ward off disease.''', '''Pass''', 0, 0, 'r')

def r25():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    threechoices('''Your teen wakes up ill with cold- and flu-like symptoms,
    but you're scheduled to work today.''', '''With your help, your teen recovers in time to
    return to school the next day, but you earn a job strike for calling out.''', '''Stay home with them''',
    -80, 1, 'r', '''You receive a call a couple hours later
    informing you your teen was sent home
    and that you need to monitor them. Job strike for you!''', '''Send them to school''', -55, 1, 'r', '''You jot down some pointers
    for your teen to recover and hope for the best.''', '''Leave them home alone''', 0, 0, 'r')
    
def r26():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    twochoices('''You discover that your wages were
    illegally docked last time you were paid.''',
    '''Your boss insists you were lying
    despite the evidence and awards you a strike.''','''Speak to your supervisor''', -50, 1, 'r',
    '''No one there ever answers the phone,
    so you're unable to recover that missing $50.''', '''Speak to corporate''', -50, 0, 'r')

def r27():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    threechoices( '''Your entire body is sick and achy,
    but you have to be at work in an hour.''',
    '''You learn the hard way your employer offers
    no paid sick leave and earn a job strike.''', '''Call out''', -80, 1, 'r',
    '''Your N95 mask obscures your symptoms until they worsen
    halfway through your shift, after which you are
    sent home with a job strike.''', '''Go in anyway''', -40, 1, 'r', '''Without health insurance or sick leave,
    your visit costs a combined $180, but you miraculously manage
    to convince your boss to excuse your absence.''',
    '''Visit urgent care''', -180, 0, 'r')

def r28():
    threechoices('''Your cellphone and Internet bills are both due today, each $75.''',
    '''You are relieved to still be able to
    communicate with the outside world this month.''', '''Pay both''',
    -150, 0, 'r', '''You are forced to decide between
    sacrificing communication with your family
    and information from the web.''', '''Pay one''', -75, 0, 'r',
    '''You will soon no longer be able to call your
    relatives or engage in any online activities.''', '''Pay none''', 0, 0, 'r')

def r29():
    twochoices('''Your Internet has been extremely slow lately.''',
    '''You can clearly feel that extra bandwidth.''', '''Upgrade to an "express" plan''',
    -50, 0, 'r', '''Lack of reliable Internet access plagues rural communities.''',
    '''Stay with the basic plan''', 0, 0, 'r')

def r30():
    threechoices('''Your teen is becoming very thin from
    either walking hours to and from school or working each day.''',
    '''Your teen really needs the extra nutrients.''',
    '''Double your grocery expenditures''', -65, 0, 'r',
    '''These snacks may be unhealthy, but they at least supply
    enough calories to help your teen continue to get by.''', '''Buy junk food''',
    -20, 0, 'r', '''Your teen's malnutrition deteriorates to the
    point of triggering a trip to the hospital. Welfare covers
    direct medical costs, but you still pay in the end because your teen
    cannot perform any more strenous activity this month. They will
    have to be driven to school or quit their farm job, costing you.''',
    '''Do nothing''', -1 * random.randint(130, 170), 0, 'r')

def r31():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    twochoices('''You normally take Exit 255 on your morning commute,
    but you got distracted and missed it.''', '''That maneuver is extremely dangerous.
    You're lucky you were ticketed $150
    (and still made it to work on time)
    rather than fatally rear-ended.''', '''Back up to the exit''', -150, 0, 'r',
    '''An accident near Exit 260 makes you late for work
    and costs you a strike, but you made the safer choice.''',
    '''Continue to Exit 260 and double-back''', -20, 1, 'r')

def r32():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    threechoices('''You've been feeling very fatigued lately and
    feel a visit to a doctor is necessary.''', '''You are prescribed medication that ultimately
    pays off, but the two-hour drive costs you
    $80 worth of gas, while the visit itself costs another $80.''', '''Get it checked out''', -160, 0, 'r',
    '''You know you shouldn't make this a habit, but it's cheaper than
    both the visit itself and the lengthy drive.''', '''Turn to Red Bull''', -20, 0, 'r',
    '''Your condition worsens to the point you
    oversleep and earn a job strike.''', '''Wait it out''', -80, 1, 'r')

def r33():
    twochoices('''Another tenant chronically litters, attracting
    wild animals, and you know it's the same person every time.''',
    '''Due to a lack of security cameras in the park,
    the tenant not only dodges accountability but shifts
    the blame to you, attracting a $200 penalty fee.''',
    '''Report them to your landlord''', -200, 0, 'r',
    '''The litterbug goes unpunished while
    animals continue to gather, with one eventually
    invading your home and eating $25 worth of food.''', '''Stand by''', -25, 0, 'r')

def r34():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    twochoices('''While walking through the woods, your teen notices a
    cavern with lots of cash inside.''',
    '''Though not easy, especially in the face of potential riches,
    you must play it safe. And good thing you did:
    the police find criminals with drugs and weapons in the cave.''',
    '''Contact authorities''', 0, 0, 'r', '''The cave is actually a makeshift drug house
    whose inhabitants are hostile. You and your teen escape, albeit with
    injuries, and must both stay home the next day. Job strike for you!''',
    '''Get rich''', -80, 1, 'r')
    
def r35():
    twochoices('''A local solar panel company is advertising major deals.''',
    '''They'll pay for themselves eventually, but the upfront
    costs will deal a major blow to your wallet.''', '''Buy some for $200''', -200, 0, 'r',
    '''Without enough money in the bank now, you'll be
    unable to reap the long-term financial gains of solar panels.''', '''Pass''',
    0, 0, 'r')

def r36():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    twochoices('''As if yet another terrible workday
    couldn't get any worse, you come home to a
    cockroach infestation. Your landlord will neither hire an
    exterminator nor reduce your rent as compensation.''',
    '''One hundred bucks later, your apartment is roach-free.''', '''Hire one yourself''', -100, 0, 'r',
    '''The infestation worsens to the point your sleep is affected,
    costing you half a day's work and a job strike.''', '''Do nothing''', -35, 1, 'r')
 
def r37():
    threechoices('''Your credit card is maxed out at $1,000
    after you used it to delay foreclosure.''',
    '''You are relieved to have paid your debts in full.''', '''Pay the whole balance''', -1000, 0, 'r',
    '''If you continue to only pay the minimum,
    you will take six years to pay off your card
    and pay 50% more in the end.''','''Pay the $90 minimum''', -90, 0, 'r',
    '''You will soon face several negative consequences,
    including late fees, elevated APRs, reduced credit scores,
    and even phone calls from debt collections agencies,
    costing you in both the short term and long term.''',
    '''Don't pay any this month''', -1 * random.randint(100,200), 0, 'r')
    
def r38():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    twochoices('''You finally have a day off work to
    spend with your teen, but a coworker's
    unwanted shift sits up for grabs.''', '''You feel sad to not be with your teen, but that extra $80 is
    completely worth it.''', '''Claim the shift''', 80, 0, 'r', '''You may have missed out on some extra
    cash, but you enjoyed every minute of your time off.''', '''Do not claim the shift''', 0, 0, 'r')

def r39():
    twochoices('''Your town is experiencing a widespread satellite
    Internet outage, which includes your home.''',
    '''You hope the satellite is fixed by the next day
    considering the cafe's $10 hourly rate.''',
    '''Visit your local Internet cafe''', -1 * random.randint(20, 120), 0, 'r',
    '''Because you have no cellular service at home,
    you will not only lack Internet access but also
    the ability to call and text until at least tomorrow.''',
    '''Wait it out''', 0, 0, 'r')
    
def r40():
    twochoices('''Your local community college is offering
    a $300 course in computer science,
    which may eventually score you financial security and prosperity.''', '''Having failed to anticipate the
    course's high workload, you become overwhelmed and are forced to drop it.
    No wonder so few can escape the vicious cycle of poverty.''', '''Take it''', -300, 0, 'r',
    '''Lack of affordability within higher education
    severely restricts access for low-income students.''',
    '''Skip it''', 0, 0, 'r')

def r41():
    twochoices('''Your one and only coat just ripped,
    but winter isn't quite over yet.''',
    '''It may not be cheap, but it sure makes
    the cold bearable again.''', '''Buy a new one for $50''',
    -50, 0, 'r', '''That coat also rips after a week,
    after which you reluctantly buy an unused one.''',
    '''Buy a used one for $10''', -60, 0, 'r')
       
def r42():
    threechoices('''Your electric and water bills are
    both due today, each roughly $100.''', '''You are relieved to know
    your utilities will remain on this month.''', '''Pay both''', -200, 0, 'r', '''You are faced with the painful task
    of choosing which utility to save and which utility to lose.''', '''Pay one''', -100, 0, 'r', '''You wonder how you'll survive
    without electricity or running water.''', '''Pay none''', 0, 0, 'r')
    
def r43():
    twochoices('''A passerby notices the stressed look on your face
    and offers you a cigarette.''', '''You depend on smoking to suppress your anxiety and loneliness,
    costing you at least $100 over the course of the month.''',
    '''Say yes''', -1 * random.randint(100, 150), 0, 'r', '''This decision was a tough one to make
    considering everything going on, but it will protect
    both your wallet and health.''', '''Say no''', 0, 0, 'r')

def r44():
    threechoices('''Your home has gotten so dirty that your neighbors and
    landlord can smell it. You are ordered to clean it immediately.''',
    '''You are relieved to come home to a fresh, spotless home but
    also frustrated considering what else that $180 could have bought you.''',
    '''Hire a maid''', -180, 0, 'r',
    '''The mold, grime, and garbage are so rampant that
    you end up shelling out $50 for heavy-duty cleaning supplies.''',
    '''Clean it yourself''', -50, 0, 'r', '''The air freshener works but only for a few hours.
    Your landlord then charges you $200 to
    send his janitorial staff into your home.''', '''Settle for Lysol''', -215, 0, 'r')

def r45():
    twochoices('''Your teen receives a total of $83 from
    both friends and family for his birthday.''',
    '''Your teen at least buys enough snacks, however unhealthy,
    to slash $10 from this month's grocery bill.''',
    '''Let your teen keep the money''', 10, 0, 'r', '''Your teen is angry and only calms down
    after yet another long discussion
    of the dire need to make every penny count.''','''Take the money''', 83, 0, 'r')

def r46():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l3', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l3', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 'r')
    
def r47():
    global payday
    if payday == 'FIRED':
        select('r')
        return
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l3', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l3', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 'r')
    
def r48():
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l3', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l3', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 'r')
    
def r49():
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l3', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l3', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 'r')
    
def r50():
    threechoices('''While grocery shopping, you notice that
    lottery tickets are on sale, 3 for 10.''',
    '''For the nation's poorest, gambling may seem
    like the only route to a better life.''', '''Buy three''',
    -10, 0, 'l3', '''For the nation's poorest, gambling may seem like the only route to a better life.''',
    '''Buy one''', -5, 0, 'l3', '''Those tickets probably would
    have all lost anyway.''', '''Buy none''', 0, 0, 'r')
    
    
def select(cmd):
    #This function selects a random scenario based on
        #the current game mode
    if cmd == 'c':
        lstc = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
        c11, c12, c13, c14, c15, c16, c17, c18, c19, c20,
        c21, c22, c23, c24, c25, c26, c27, c28, c29, c30,
        c31, c32, c33, c34, c35, c36, c37, c38, c39, c40,
        c41, c42, c43, c44, c45, c46, c47, c48, c49, c50]
        random.choice(lstc)()
        
    elif cmd == 's':
        lsts = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10,
        s11, s12, s13, s14, s15, s16, s17, s18, s19, s20,
        s21, s22, s23, s24, s25, s26, s27, s28, s29, s30,
        s31, s32, s33, s34, s35, s36, s37, s38, s39, s40,
        s41, s42, s43, s44, s45, s46, s47, s48, s49, s50]
        random.choice(lsts)()

    elif cmd == 'r':
        lstr = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10,
        r11, r12, r13, r14, r15, r16, r17, r18, r19, r20,
        r21, r22, r23, r24, r25, r26, r27, r28, r29, r30,
        r31, r32, r33, r34, r35, r36, r37, r38, r39, r40,
        r41, r42, r43, r44, r45, r46, r47, r48, r49, r50]
        random.choice(lstr)()

#The text and button widgets that are updated in the
    #choice functions are created and packed
txt = Label(w, text='''You just lost your home to foreclosure
    and must find an apartment for you and your teen to stay in.''',
    font=('Verdana', 17))
txt.pack(padx=100, pady=100)
b1 = Button(w, text='', font=('Verdana', 10), command='')
b1.pack(ipadx=10, pady=10)
b2 = Button(w, text='', font=('Verdana', 10), command='')
b2.pack(ipadx=10, pady=10)
b3 = Button(w, text='', font=('Verdana', 10), command='')
b3.pack(ipadx=10, pady=10)

#The start function and mainloop are called, finishing the program
restart(30, random.randint(800, 1000), 7, 0)

w.mainloop()
