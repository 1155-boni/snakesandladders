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
l=[]
board(l)
ladderandsnake()