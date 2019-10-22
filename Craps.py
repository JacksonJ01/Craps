# Jared Jackson
# 10/21/19
# This program will be a game where you bet money and test your luck
from random import *
amounts = []
bets = []


def bank_roll():
    print("How much money do you wish to start with?")
    start = int(input(">>>"))
    amounts.append(start)


def roll_dice():
    rng = int(randint(1, 6) + randint(1, 6))
    return rng


def r_g():
    bets.clear()
    game()


def big1():
    big = input(">>>").title()

    if big == "Yes" or big == "Y":
        print("Well that's nice..")
        print("You won't find that here though.")
        print("Anyhow, let's continue.")

    elif big == "No" or big == "N":
        print("Too bad! Your answer isn't important.")
        print("Now let us continue.")

    else:
        print("Can you please repeat that for me?")
        big1()


def info1():
    info = input(">>>").title()

    if info == "Yes" or info == "Y":
        print("Are you stupid or something?!")
        print("Why would you give your number out a random, unsafe computer?")

    elif info == "No" or info == "N":
        print("Good, you have been trained well.")

    else:
        print("Sorry, didn't catch that.")
        print("Yes or No")
        info1()


def game():
    print(f"How much money, of your ${amounts[0]}, do you want to bet?")
    wager = int(input(">>>"))
    bets.append(wager)
    print("Your value has been entered!")
    print("Time to have your first roll.")
    r1 = roll_dice()
    if r1 == 7 or r1 == 11:
        print("You won!")
        print("Talk about lucky.")
        print("You have more money to bet now:")
        print(f"${amounts[0] + bets[0]}")
        amounts.append(amounts[0] + bets[0])
        amounts.remove(amounts[0])
        print("Would you like to bet again?")

        def more1():
            more = input(">>>").title()

            if more == "Yes" or more == "Y":
                print("Alright.")
                r_g()

            elif more == "No" or more == "N":
                print("Smart. Playing it safe.")
                print("I'll see yu around.")
                exit()

            else:
                print("One more time please. Yes or No?")
                more1()

        more1()

    elif r1 == 2 or r1 == 3 or r1 == 12:
        print("Wow, you lost on the first roll...")
        print(f"How did you manage to roll {r1}.")
        print("Since you lost, you now have:")
        print(f"${amounts[0] - bets[0]}")
        amounts.append(amounts[0] - bets[0])
        amounts.remove(amounts[0])
        print("Do you want to bet again?")

        def again_():
            again = input(">>>").title()

            if again == "Yes" or again == "Y":
                print("Well, someone isn't a sore loser.")
                r_g()

            elif again == "No" or again == "N":
                print("Sore loser!")
                exit()

            else:
                print("Repeat that for me please.")
                again_()

        again_()

    else:
        print("So, you didn't lose... but you didn't win either.")
        print(f"You rolled and got {r1} point(s).")
        print("You will have to keep rolling until you roll another", r1, "point(s).")
        print("If you roll a 7 you will crap out and lose the bet.")
        print("PRESS ENTER")

        def roll_dice2():
            input(">>>")
            rr = roll_dice()

            if rr == 7:
                print("You lost. All you had to do was not roll 7!")
                print(amounts[0] - bets[0])
                amounts.append(amounts[0] - bets[0])
                amounts.remove(amounts[0])
                print("Do you want to play again?")

                def again1_():
                    again1 = input(">>>").title()

                    if again1 == "Yes" or again1 == "Y":
                        print("Good. You aren't a sore loser like I thought you were.")
                        r_g()

                    elif again1 == "No" or again1 == "N":
                        print("I will respect your wishes.")
                        exit()

                    else:
                        print("Was that a Yes or a No?")
                        again1_()

                again1_()

            elif rr == r1:
                print("Hey, look at that, you won.")
                print(amounts[0] + bets[0])
                amounts.append(amounts[0] + bets[0])
                amounts.remove(amounts[0])
                print("Would you like to bet more?")

                def again2_():
                    again2 = input(">>>").title()

                    if again2 == "Yes" or again2 == "Y":
                        print("Cool, let's go.")
                        r_g()

                    elif again2 == "No" or again2 == "N":
                        print("Ahh, gonna play it safe I see.")
                        print("Alright then, bye.")
                        exit()

                    else:
                        print("Yes or No answers please")
                        again2_()

                again2_()

            else:
                print(f"Drats, you got {rr} point(s).")
                print("You get to another chance.")
                roll_dice2()

        roll_dice2()


input("CLICK SCREEN THEN PRESS ENTER")

print("Hello there. What is your name?")
name = input(">>>").title()
print(f"Why hello there {name}.")
print("Would you like to be a part of something big?")
big1()
print("\n")
print("Soo, today I am going to have you bet money.")
print("There's just one thing I need.")
print("May I have your debit and/or credit card info along with the pin number?")
info1()
print("\n")
print("For this game no real money will be needed but you will have to specify your starting amount of money.")
print("You will also be required to state your betting amount.")
print("These can be any value so pick your poison.")
print("After each game you will be able to play another round.")

bank_roll()
game()
