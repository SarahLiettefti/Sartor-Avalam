import random

def themove(body):
    m = hasard(body)
    moves = turningoodform(m)
    return moves

def hasard(body):#donne un coup au hasard sous la forme [[0,3],[0,4]]
    m=random.choice(coup(body))
    return m

def turningoodform(m):#transforme un [[0,3],[0,4]] en dictionnaire de la bonne forme
    moves = {"move": {"from": m[0], "to": m[1]}}
    return moves

def wichplayer(body):#renvoie la couleur jouée
    if (body["players"][0]==body["you"]): 
        return 0
    else: 
        return 1

def coup(body):
    casesoccupes= casejouables(body)
    game=body["game"]
    player=wichplayer(body)
    coups=[] #tous les coups possible
    ecrase=[]#met un de nos pions sur l'autre
    ecrase2=[] #met un de nos pions sur l'autre et creer un tour de 2
    ecrase3=[] #met un de nos pions sur l'autre et creer un tour de 3
    ecrase4=[] #met un de nos pions sur l'autre et creer un tour de 4
    ajout=[]#met un de nos pions sur un notre a nous
    embete=[]#met un des pions adversaire sur un autre a lui
    completusbyus = [] #complète un tour de 5 par notre couleur
    complettheybyus = [] #complète un tour de 5 par la couleur ennemie (apres l'avoir completé ce sont des pions ennemis qui ne savent plus bouger)
    complettheybythey = []
    seul=[]#liste de déplacements dont l'origine ne peut faire que ce déplacement
    seulvoisin=[] #une liste des cases qui n'ont qu'un déplacement possible
    ensembleseul=[]#déplacement d'une case qui ne peut que être deplacée à un endroit et qui écrase l'adversaire sur une tour qui ne pouvait aussi être déplacé que à cet endroit
    for line in range(9):
        for col in range(9):
            de=[line,col]
            if de in casesoccupes:
                autour = [[line,col+1],[line,col-1],[line+1,col],[line-1,col],[line-1,col+1],[line-1,col-1],[line+1,col+1],[line+1,col-1]]
                visit =[]
                for to in autour:
                    if to in casesoccupes:
                        if ((len(game[de[0]][de[1]]))+(len(game[to[0]][to[1]])))<=5:  
                            visit.append(to)
                            findallcoup(game,de,to,coups,ecrase,ecrase2,ecrase3,ecrase4,ajout,embete,player,completusbyus,complettheybyus,complettheybythey)
                ville = len(visit)
                if ville==1:
                    seul.append([de,visit[0]])
                    seulvoisin.append(de)
    for elem in seul:
        if elem[1] in seulvoisin:#verrifie que les deux cases n'ont qu'une option
            maybebest = [elem[0],elem[1]]
            if maybebest in ecrase:#verrifie que le coup mange un pion adversaire
                ensembleseul.append(maybebest)
    return Choosestrat(coups,ecrase2,ecrase3,ecrase4,ajout,embete,completusbyus,complettheybyus,complettheybythey,ensembleseul) #renvoie une liste à la fin

def casejouables(body):
    game=body["game"]
    casesoccupes = []#toutes cases "jouables" #au début 48
    li = 0
    for game[li] in game:
        col = 0
        for game[li][col] in game[li]:
            if (0<len(game[li][col])<5):
                casesoccupes.append([li,col])
            col+=1
        li+=1
    return casesoccupes

def findallcoup(game,de,to,coups,ecrase,ecrase2,ecrase3,ecrase4,ajout,embete,player,completusbyus,complettheybyus,complettheybythey):
    move = [de,to]
    coups.append(move)
    if game[de[0]][de[1]][-1]==player:#si le pion qu'on va déplacer est à nous
        if game[to[0]][to[1]][-1]==player:#si on le déplace sur un de nos pions
            ajout.append(move)
            if ((len(game[de[0]][de[1]]))+(len(game[to[0]][to[1]])))==5: #si ça complète une tour de 5 pions
                completusbyus.append(move)
        else:#si on le déplace sur un pion ennemi
            ecrase.append(move)
            if ((len(game[de[0]][de[1]]))+(len(game[to[0]][to[1]])))==5: 
                complettheybyus.append(move)
            elif ((len(game[de[0]][de[1]]))+(len(game[to[0]][to[1]])))==2: 
                ecrase2.append(move)
            elif ((len(game[de[0]][de[1]]))+(len(game[to[0]][to[1]])))==3: 
                ecrase3.append(move)
            elif ((len(game[de[0]][de[1]]))+(len(game[to[0]][to[1]])))==4: 
                ecrase4.append(move)
    else:#si le pion qu'on va déplacer est à l'ennemi
        if game[to[0]][to[1]][-1]!=player:
            embete.append(move)
            if ((len(game[de[0]][de[1]]))+(len(game[to[0]][to[1]])))==5: 
                complettheybythey.append(move)
    return coups, ecrase,ecrase2,ecrase3,ecrase4, ajout, embete, completusbyus,complettheybyus,complettheybythey

def Choosestrat(coups,ecrase2,ecrase3,ecrase4,ajout,embete,completusbyus,complettheybyus,complettheybythey,ensembleseul):#renvoie la liste de la meilleur strategie
    if len(ensembleseul)!=0:
        return ensembleseul
    elif len(complettheybyus)!=0:
        return complettheybyus
    elif len(ecrase2)!=0:
        return ecrase2
    elif len(ecrase3)!=0:
        return ecrase3
    elif len(ecrase4)!=0:
        return ecrase4  
    elif len(complettheybythey)!=0:
        return complettheybythey
    elif len(embete)!=0:
        return embete
    elif len(ajout)!=0:
        return ajout
    else:
        return coups