
def printTheBoard():
    print('\n'+theBoard['top-L']+'|'+theBoard['top-M']+'|'+theBoard['top-R'])
    print('-+-+-')
    print(theBoard['mid-L']+'|'+theBoard['mid-M']+'|'+theBoard['mid-R'])
    print('-+-+-')
    print(theBoard['low-L']+'|'+theBoard['low-M']+'|'+theBoard['low-R']+'\n')

def winChecker():
    for i in ['X','O']:
        if theBoard['top-L'] == i:
            if theBoard['mid-L'] == i:
                if theBoard['low-L'] == i:
                    print('----> %s, YOU WON!!' %i)
                    return True
            elif theBoard['mid-M'] == i:
                if theBoard['low-R'] == i:
                    print('----> %s, YOU WON!!' %i)
                    return True
            elif theBoard['top-M'] == i:
                if theBoard['top-R'] == i:
                    print('----> %s, YOU WON!!' %i)
                    return True
        if theBoard['top-R'] == i:
            if theBoard['mid-R'] == i:
                if theBoard['low-R'] == i:
                    print('----> %s, YOU WON!!' %i)
                    return True
            elif theBoard['mid-M'] == i:  
                if theBoard['low-L'] == i:
                    print('----> %s, YOU WON!!' %i)
                    return True
        if theBoard['top-M'] == i:
            if theBoard['mid-M'] == i:
                if theBoard['low-M'] == i:
                    print('----> %s, YOU WON!!' %i)
                    return True
        if theBoard['mid-L'] == i:
            if theBoard['mid-M'] == i:
                if theBoard['mid-R'] == i:
                    print('----> %s, YOU WON!!' %i)
                    return True
        if theBoard['low-L'] == i:
            if theBoard['low-M'] == i:
                if theBoard['low-R'] == i:
                    print('----> %s, YOU WON!!' %i)
                    return True
    return False

turn_owner = ['X','0','X','0','X','0','X','0','X']

while True:
    print('Hello and welcome to the classic game called Tic-Tac-Toe!\n')

    theBoard = {'top-L':' ', 'top-M':' ', 'top-R':' ',
                'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
                'low-L':' ', 'low-M':' ', 'low-R':' '}

    for turn_number in range(9):
        move = input('Turn for %s. Move on which space? \n\n \
            top-L | top-M | top-R\n \
            ------+-------+-------\n \
            mid-L | mid-M | mid-R\n \
            ------+-------+-------\n \
            low-L | low-M | low-R\n' %turn_owner[turn_number])
        theBoard[move] = turn_owner[turn_number]
        printTheBoard()
        b = winChecker()
        if b == True:
            ans = (input('\nWould you like to play again? (y/n) ')).lower()
            break
    if (b == True and ans == 'n'):
        break
    elif b == False:
        print('No one won this game. Better luck in the next...\n')
        ans = (input('\nWould you like to play again? (y/n) ')).lower()
        if ans == 'n':
            break
print('\nExiting... Press ENTER to quit')
input()

