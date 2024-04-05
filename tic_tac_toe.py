from random import randint

def displayboard():
    global board
    print(board[0],board[1],board[2],sep='|')
    print('______')
    print(board[3],board[4],board[5],sep='|')
    print('______')
    print(board[6],board[7],board[8],sep='|')

def chkinp():
    if player == "o" or a=="p":
        while True:
            i=input('choose a number between 1-9: ')
            if i.isdigit() and '1'<=i<='9':
                if int(i) not in player_moves:
                    ans=int(i)
                    player_moves.append(ans)
                    return ans
                else:
                    continue
    else:
        while True:
            i=randint(1,9)
            if i not in player_moves:
                player_moves.append(i)
                return i
            else:
                continue
  
def updateboard(ans):
    global board,player
    i=ans-1
    board[i]=player
    displayboard()

def currentplayer():
    global player
    if player=='x':
        player='o'
    else:player='x'

def win(board,player):
    c=player
    if board[0]==board[1]==board[2] and board[0]==c:
        print('\nPlayer',player,'won')
        return False
    elif board[3]==board[4]==board[5] and board[3]==c:
        print('\nPlayer',player,'won')
        return False
    elif board[6]==board[7]==board[8] and board[6]==c:
        print('\nPlayer',player,'won')
        return False
    elif board[0]==board[3]==board[6] and board[0]==c:
        print('\nPlayer',player,'won')
        return False
    elif board[1]==board[4]==board[7] and board[1]==c:
        print('\nPlayer',player,'won')
        return False
    elif board[2]==board[5]==board[8] and board[2]==c:
        print('\nPlayer',player,'won')
        return False
    elif board[0]==board[4]==board[8] and board[0]==c:
        print('\nPlayer',player,'won')
        return False
    elif board[2]==board[4]==board[6] and board[2]==c:
        print('\nPlayer',player,'won')
        return False
    elif ' ' not in board:
        print('\nIts a draw')
        return False
    else:return True

def player2():
    ans=randint(0,8)
    return ans

while True:
    start=input('Do you want to start the game (y/n)?')
    if start.lower()=='y':
        pass
    else:break
    player='x'  
    player_moves=[]
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    a=input("DO you want to play with computer(c) or 'pass n play'(p): ")
    if a=="p":
        print("Player 1 is 'o' | Player 2 is 'x'")
    else:
        print("Player is 'o' | Computer is 'x'")

    while win(board,player):
        print()
        currentplayer()
        ans=chkinp()
        updateboard(ans)

            

        



    




