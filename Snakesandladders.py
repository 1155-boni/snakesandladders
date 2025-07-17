def board(l):
    turn = 2
    for i in range(0,100):
        l.insert(i,i+1)
    for j in range(99,-1,-10):
        if(turn%2==0):
            print(l[j])
l=[]
board(l)