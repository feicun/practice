import random

num = random.randint(1, 9)
count = 0
guess = 0

while guess != num and guess != 'exit':
    guess = raw_input('What is your guess? ')

    if guess == 'exit':
        break

    guess = int(guess)
    count += 1

    if guess > num:
        print 'Too high!'
    elif guess < num:
        print 'Too low!'
    else:
        print 'You got it!'
        print 'It took you ' + str(count) + ' tries!'
