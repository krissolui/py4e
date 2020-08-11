import random
word = ['html']
data = []
try:
    fhand = open('list.txt')
    data = fhand.read().split()
    for i in range(len(data)):
        if data[i].endswith(','):
            data[i] = data[i][:len(data[i]) - 1]

except:
    data = word
print('Welcome to the Programming Langguages Guessing Game')
score = 0
# Start game
while True :
    life = 5
    secret = data[random.randrange(len(data))]
    length = len(secret)
    count = 0
    win = True
    # Start round
    while True :
        # No more chance
        if life == 0 :
            print('The answer is ' + secret)
            win = False
            break
        # Guess all characters
        if count >= length :
            break
        # Print game
        if count == 0 and life == 5:
            print('You have 5 life to start with')
            print('This word has', length, 'characters')
            print('Please input your guess for the 1st character:', '_.' * length)
            guess = input()
        elif count == 0 : #Try 1st letter again
            print('You still have', life, 'life.')
            print('Please input your guess for the 1st character:', '_.' * length)
            guess = input()
        else : #Continue guessing
            index = 0
            word = ''
            # Print correct guess
            while index < count :
                word = word + secret[index] + '.'
                index = index + 1
            print('You still have', life, 'life.')
            print('Please input your guess for the next character:', word + '_.' * (length - count))
            guess = input()
        # Check if correct
        if guess.lower() == secret[count].lower() :
            count = count + 1
        elif guess == '' : #Skip blank input
            continue
        else :
            life = life - 1
    # Print result statment
    if win is True :
        score = score + 2
        print('Congratulation, You Win')
    else :
        score = score - 1
        print('Sorry, better luck next time')
    print('Your score:', score)
    # Ask if continue
    print('Do you want to play again? Type "1" and Enter if yes, or just hit Enter if no')
    if input() != '1' :
        print('Your final score:', score)
        print('Goodbye')
        break