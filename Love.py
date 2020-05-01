import numpy as np


def intro():
    print("Welcome to Love Calculator")
    name1 = input("Enter your name: ")
    name2 = input("Enter your partner's name: ")
    print("\nWe will ask you 5 questions, \nbased on which we will predict love percentage. ")
    print("Each question has 3 options as 1,2,3.\nPlease enter options as your answer.")
    print("Ready to begin? Press any key to proceed")
    input(">")
    return name1, name2


def question1():
    print("Question 1")
    print("For how long have you known each other?")
    print("1. 0-6 months")
    print("2. 1-2 Years")
    print("3. More than two years")
    return int(input("> "))


def question2():
    print("Question 2")
    print("How often do you guys fight?")
    print("1. Very often")
    print("2. Once in a while")
    print("3. We don't fight")
    return int(input("> "))


def question3():
    print("Question 3")
    print("How often do you guys have deep conversations?")
    print("1. Very often")
    print("2. Once in a while")
    print("3. We never have")
    return int(input("> "))


def question4():
    print("Question 4")
    print("How often do you guys go on dates?")
    print("1. Very often")
    print("2. Once in a while")
    print("3. I can't remember")
    return int(input("> "))


def question5():
    print("Question 5")
    print("How happy you are as a couple?")
    print("1. Very much")
    print("2. I don't know")
    print("3. Not at all")
    return int(input("> "))


def calculate(lower, upper, answers):
    answer1 = {1: 3, 2: 6, 3: 1}
    answer2 = {1: 1, 2: 6, 3: 3}
    answer3 = {1: 6, 2: 3, 3: 1}
    answer4 = {1: 6, 2: 3, 3: 1}
    answer5 = {1: 6, 2: 3, 3: 1}
    lower = lower + answer1.get(answers[1]) + answer2.get(answers[2]) + answer3.get(answers[3]) + \
            answer4.get(answers[4]) + answer5.get(answers[5])
    upper = lower + 5
    return lower, upper


def result(name_one, name_two, lower, upper):
    print("\nWow, we are finished. Excited for your results?\n")
    print("Enter 1 to know how much " + name_two + " loves " + name_one)
    print("Enter 2 to know how much " + name_one + " loves " + name_two)
    np.random.seed(1)
    partner_love = np.random.randint(lower, upper, 1)
    np.random.seed(2)
    your_love = np.random.randint(lower, upper, 1)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(name_two + " Loves " + name_one + " : ", partner_love[0], " %")
    else:
        print(name_one + " Loves " + name_two + " : ", your_love[0], " %")
    print("\nSatisfied with the results?\n")
    if choice == 1:
        print("Do you still wanna know how much " + name_one + " loves " + name_two)
        choice = int(input("1 for Yes, 0 for No: "))
        if choice == 1:
            print(name_one + " Loves " + name_two + " : ", your_love[0], " %")
    else:
        print("Do you still wanna know how much " + name_two + " loves " + name_one)
        choice = int(input("1 for Yes, 0 for No: "))
        if choice == 1:
            print(name_two + " Loves " + name_one + " : ", partner_love[0], " %")

    print("\nThank you. Visit Us soon(With another partner, maybe!)")


name_first, name_second = intro()
answers = [0, 0, 0, 0, 0, 0]
answers[1] = question1()
answers[2] = question2()
answers[3] = question3()
answers[4] = question4()
answers[5] = question5()
partner_love_lower = 50
partner_love_upper = 90
partner_love_lower, partner_love_upper = calculate(partner_love_lower, partner_love_upper, answers)
result(name_first, name_second, partner_love_lower, partner_love_upper)
