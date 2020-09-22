#An application which tells future based upon the zodiac sign
#Multiline printing

next = True
while next==True:
    print("1=2")
    print("this is the second line of loop")

    print('''   From all the mentioned Zodiac signs
    1)Aries
    2)Tauras
    3)Gemini
    4)Cancer
    5)Leo
    6)Virgo
    7)Libra
    8)Scorpio
    9)Sagittarius
    10)Capricorn
    11)Aquarius
    12)Pisces
    ''')
    s=int(input("pick your sign number and press enter to know ur future:"))
    print(s)

    if s==1:
        print("There is a hero deep inside of you, and you just might get a glimpse of that person today when you...")
    elif s==2:
        print("If drama erupts on the scene today, avoid it at all costs. Just keep your head down, mind your own...")
    elif s==3:
        print("You need to pay closer attention to the numbers today, especially if you're reviewing any budgets,..")
    elif s==4:
        print("You could receive an inexpensive but impactful gift, and it will be no bargain basement purchase!...")

    elif s==5:
        print("You will be exuding confidence today even if you don't feel particularly proud of what you have...")
    elif s==6:
        print("Are you worried that there is too much happening in your life right now? Think about those days...")
    elif s==7:
        print("Libra")
    elif s==8:
        print("Scorpio")
    elif s==9:
        print("Sagittaruis")
    elif s==10:
        print("Aquarius")
    else:
        print("plz enter correct number")

    next= True if input("Shall we do it again?? (Y/N)")=="Y" else False
    

