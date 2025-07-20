def board(l):
    turn = 2
    for i in range(0,100):
        l.insert(i,i+1)
    for j in range(99,-1,-10):
        if(turn%2==0):
            print(l[j],"|",l[j-1],"|",l[j-2],"|",l[j-3],"|",l[j-4],"|",l[j-5],"|",l[j-6],"|",l[j-7],"|",l[j-8],"|",l[j-9])
            print("-----------------------------------------------")
            turn-=1
        else:
            print(l[j-9],"|",l[j-8],"|",l[j-7],"|",l[j-6],"|",l[j-5],"|",l[j-4],"|",l[j-3],"|",l[j-2],"|",l[j-1],"|",l[j])
            print("-----------------------------------------------")
            turn+=1
def ladderandsnake():
    print("LADDERS\n 3-24\n 14-42\n 30-86\n 37-57\n 50-96\n 66-74\n")
    print("SNAKES\n 95-18\n 77-45\n 60-26\n 34-10\n 20-2\n")
def climb(x):
    if(x==3):
        x=24
    if(x==14):
        x=42
    if(x==30):
        x=86
    if(x==37):
        x=57
    if(x==50):
        x=96
    if(x==66):
        x=74
    return(x)
def fall(y):
    if(y==95):
        y=18
    if(y==77):
        y=45
    if(y==60):
        y=28
    if(y==34):
        y=10
    if(y==20):
        y=2
    return(y)
def accept_from_user(move_1,move_2):
    import random
    dice=[1,2,3,4,5,6]
    whoo=input("Enter Player 1 name in this GAME!\n")
    wh=input("Enter Player 2 name in this GAME!\n")
    who=int(input("Enter who wants to start the GAME! Enter 1 or 2...\n"))
    while(move_1<=100 and move_2<=100):
        if(who==1):
            chance_1=int(input("{0} Enter 1 POLL the die!".format(whoo)))
            if(chance_1==1):
                player_1=random.choice(dice)
                move_1+=player_1
                print(move_1,"before climb")
                move_1=climb(move_1)
                print("{0} is at position {1}".format(whoo,move_1))
                move_1=fall(move_1)
                print(move_1,"After fall")
                print("{0} is at position {1}".format(whoo,move_1))
            else:
                print("Enter 1 to PROCEED!..")
            who+=1
        else:
            chance_2=int(input("{0} Enter 1 POLL the die!".format(wh)))
            if(chance_2==1):
                player_2=random.choice(dice)
                move_2+=player_2
                print(move_2,"before climb")
                move_2=climb(move_2)
                print("{0} is at position {1}".format(wh,move_2))
                move_2=fall(move_2)
                print(move_2,"After fall")
                print("{0} is at position {1}".format(wh,move_2))
            else:
                print("Enter 1 to PROCEED!..")
            who-=1
    else:
        if(move_1>move_2):
            print("Congrats {0}!!".format(whoo))
        else:
            print("Congrats {0}!!".format(wh))

l=[]
board(l)
ladderandsnake()
accept_from_user(move_1=1,move_2=1)