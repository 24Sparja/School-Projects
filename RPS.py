import random
random.seed()
pointEarned = []
pointLost = []
#Player choses from last 3, cpu choses from first 3.
weapons = ['Scissors', 'Rock', 'Paper', 'Scissors']


playerScore = int(0)
comScore = int(0)
def main():
    global playerScore
    global comScore
    playing = True
    print('Welcome to Rock, Paper, Scissors.\n Rock Beats Sciccors, Scissors beats Paper, and Paper beats Rock.')
    while playing == True:
        while playerScore != 3 and comScore != 3 :
            gameRound() 
        if playerScore == 3:
            print('VICTORY! would you like to try again?')
        elif comScore == 3:
            print('Unfortunate, would you like to try again?')
        keepPlaying = int(input('      1) Yes   2) No\n'))
        if keepPlaying == 1:
            playerScore = 0
            comScore = 0 
        else:
            playing = False



def gameRound():
    global playerScore
    global comScore
    playerWeapon = int(input(' 1) Rock  2) Paper  3) Scissors \n'))

    #Pick Weapons
    while weapons[int(playerWeapon)] not in weapons or playerWeapon == 0:
        print('Not a choice, pick again.')
        playerWeapon = input()
    comWeapon = random.randrange(1,3)
    print(f'You chose {weapons[int(playerWeapon)]}')
    print(f'Your enemy brought {weapons[int(comWeapon)]}')

    #Determine Winner
    if playerWeapon - comWeapon == 0 or playerWeapon - comWeapon == 3 :
        print('Tie')    
    elif playerWeapon - comWeapon == 1 :
        print('Win')
        playerScore += 1
    else :
        print('lose')
        comScore += 1
    print(f'Player:{playerScore}')
    print(f'Enemy:{comScore}')

main()