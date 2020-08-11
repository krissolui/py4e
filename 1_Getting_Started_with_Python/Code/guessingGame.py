from random import randrange
print('Welcome to the Guessing Game!')
play = True
while play == True :
    secret = randrange(1000)
    win = False
    while win == False :
        # Keep asking until valid input
        ask = True
        while ask == True :
            try :
                guest = int(input('Pick a number (0-999): '))
                ask = False
            except:
                print('Please input an INTEGER')
                ask = True
        # Print result
        if guest == secret :
            print('Congratulation!')
            win = True
        elif guest > secret :
            print('Too big...')
        else :
            print('Too small...')
    print('Do you want to start a new round?')
    print('Type "1" for Yes OR elsewhere for No')
    again = input()
    if again == '1' :
        play = True
    else :
        play = False
        print('Goodbye my friend')
