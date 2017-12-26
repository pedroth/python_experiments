from random import randint

def game():
    mon = int(raw_input('\n[*] How much money do you have? > '))
    while mon > 0:
        r = randint(0,1) #generates either 0 or 1.  1 = 'heads'; 0 = 'tails'
        bet = int(raw_input('[*] Place your bet > '))
        if bet > mon:
            print("\n[!] You don't have that much money!")

        elif mon == 0:
            print('\n[!] You are out of money!\n')

        else:
            hd = raw_input('\n[*] All right, the million dollar question, HEADS or TAILS? > ')
            if (hd == 'heads' and r == 1) or (hd == 'tails' and r == 0):
                print('\n[!] You won!\n')
                mon += bet * 2
                print('> You now have %s!\n' % (mon))

            elif (hd == 'heads' and r == 0) or (hd == 'tails' and r == 1):
                print('\n[!] You lost...\n')
                mon -= bet
                print('> You now have %s!\n' % (mon))

            else:
                print('\n[!] Please choose HEADS or TAILS\n')

def main():
    print('#----------------#')
    print('| HEADS OR TAILS |')
    print('|    by n3xUs_   |')
    print('#----------------#')

    print('\n[*] This game is simple. You either choose HEADS or TAILS.\n')
    print('[*] If you win, you multiply the money you bet, if you lose, you lose the money.\n')
    print('[*] Simply input how much money you have and how much you want to bet.')
    raw_input('\n[*] Press ENTER to begin...')
    game()


main()
