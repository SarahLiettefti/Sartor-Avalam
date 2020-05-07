import random

def casejouables(body):
    game=body["game"]
    casesoccupes = []#toute case "jouable"#au début 48
    li = 0
    for game[li] in game:
        col = 0
        for game[li][col] in game[li]:
            if (0<len(game[li][col])<5):
                casesoccupes.append([li,col])
            col+=1
        li+=1
    return casesoccupes

def findallcoup(game,de,to,coups):
    move = [de,to]
    coups.append(move)
    return coups

def coup(body):
    casesoccupes= casejouables(body)
    game=body["game"]
    coups=[] #tous les coups possible
    for line in range(9):
        for col in range(9):
            de=[line,col]
            if de in casesoccupes:
                autour = [[line,col+1],[line,col-1],[line+1,col],[line-1,col],[line-1,col+1],[line-1,col-1],[line+1,col+1],[line+1,col-1]]
                for to in autour:
                    if to in casesoccupes:
                        if ((len(game[de[0]][de[1]]))+(len(game[to[0]][to[1]])))<=5:  
                            findallcoup(game,de,to,coups)
    #print(coups)
    return coups #renvoie une liste à la fin

def turningoodform(m):#transforme un [[0,3],[0,4]] en ce quil faut
    moves = {"move": {"from": m[0], "to": m[1]}}
    return moves

def hasard(body):#donne un coup au hasard [[0,3],[0,4]]
    m=random.choice(coup(body))
    return m

def themove(body):
    m = hasard(body)
    moves = turningoodform(m)
    return moves