#some neccesary things
import random
import time
game_over = True
still_on = True

#original money to compare later
orin = 500000

#Bank
user_money = 500000
computer_money = 500000

while game_over:
    #check the amount of money first
    print("\nYour balance: >>>", user_money, "$\n")
    print("\nTarget balance: >>>", computer_money, "$\n")
    if user_money == 0:
        print("You have ran out of money")
        quit()
    if computer_money == 0:
        print("computer lose all its money")
        quit()
    else:
        pass

    #random function
    def ran():
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        card = random.choice(cards)
        return card

    #Deposit cards
    user_card = []
    computer_card = []
    why = []

    #First 2 cards for both computer and player
    for i in range(2):
        m = ran()
        n = ran()
        computer_card.append(m)
        user_card.append(n)
        why.append('?')
    to_c = sum(computer_card)
    to_u = sum(user_card)

    #if the sum of cards in player or computer cards holder above 21 and its contain 11 change it from 11 to 1 (special rules)
    def change(a,b):
        if a > 21 and 11 in user_card:
            user_card.remove(11)
            user_card.append(1)
        elif b > 21 and 11 in computer_card:
            computer_card.remove(11)
            computer_card.append(1)
    
    #New rounds system
    def new_r(a):
        ask = input("New rounds?(y/n): ").lower()
        if ask.isalpha() and ask == "y":
            a = True
            print("\033c\033[3J", end='')
        elif ask.isalpha() and ask == "n":
            print("\033c\033[3J", end='')
            if user_money > orin:
                print("Congrats you have made ", (user_money - orin), "$")
            elif user_money < orin:
                print("You have lost ", (orin - user_money), "$")
            else:
                print("same amount of money duh")
            a = False
            quit()
        else:
            quit()


    #Game
    print("Your card is: >>", user_card)
    print("Computer card is >> ", why)

    m_an = True

    while m_an:
        m = input("Do you want to get more cards? (y/n): ").lower()
        if m.isalpha() and m == "y":
            m = ran()
            user_card.append(m)
            print(user_card)
            to_u += m
            change(to_u, to_c)
            if sum(user_card) > 21:
                m_an = False
        elif m.isalpha() and m == "n":
            m_an = False
        else:
            quit()
        print("Target is thinking....")
        time.sleep(2)
        if to_c < 21:
            m = ran()
            computer_card.append(m)
            to_c += m
            change(to_u, to_c)
            why.append('?')
            print("Target decided to pick one more card\n")
        else:
            print("Target choose to stay\n")
            pass
    
    n = input("Check? (y/n): ").lower()

    if n == "y":
        to_un = sum(user_card)
        to_cn = sum(computer_card)
        if to_un > to_cn and to_un <= 21:
            user_money += 500 * len(computer_card)
            computer_money -= 500 * len(computer_card)
            print("You win")
        elif to_un < to_cn and to_cn <= 21:
            user_money -= 500 * len(user_card)
            computer_money += 500 * len(user_card)
            print("Target win")
        if to_un > to_cn and to_un > 21:
            user_money -= 500 * len(user_card)
            computer_money += 500 * len(user_card)
            print("Target win")
        elif to_un < to_cn and to_cn > 21:
            user_money += 500 * len(computer_card)
            computer_money -= 500 * len(computer_card)
            print("You win")
        elif to_un == to_cn:
            print("Draw")

        print("\nYour cards >>> ", user_card, "\n")
        print("\nTarget cards >>> ", computer_card, "\n")
        print("\nYour balance: >>>", user_money, "$\n")
        print("\nTarget balance: >>>", computer_money, "$\n")
        new_r(game_over)
    else:
        new_r(game_over)

