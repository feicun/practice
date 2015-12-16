import sys

user1 = raw_input("What's your name?")
user2 = raw_input("And your name?")
user1_answer = raw_input(
    "%s, do you want to choose rock, paper or scissors" % user1)
user2_answer = input(
    "%s, do you want to choose rock, paper or scissors?" % user2)


def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors wins!")
        else:
            return("Rock wins!")
    else:
        return(
            "Invalid input! " +
            "You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))
