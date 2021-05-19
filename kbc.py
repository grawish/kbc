from questions import QUESTIONS
import random


def isAnswerCorrect(question, answer):
    return True if answer == question['answer'] else False


def lifeLine(ques):
    print(ques)
    ans = ques['answer']
    remove1 = random.randint(1, 4)
    while remove1 == ans:
        remove1 = random.randint(1, 4)
    remove2 = random.randint(1, 4)
    while remove2 == remove1 or remove2 == ans:
        remove2 = random.randint(1, 4)
    ques["option" + str(remove1)] = "Wrong answer"
    ques["option" + str(remove2)] = "Wrong answer"
    print(ques)
    return ques


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            0->10000->320000
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.

    #  For each question, display the prize won until now and available life line.

    # For now, the below code works for only one question without LIFE-LINE and QUIT checks]
    i = -1
    curmoney = 0
    minmoney = 0
    lose = False
    l = len(QUESTIONS)
    life = 1
    while 1:
        i = i + 1
        if i > l - 1:
            break
        print(f'\tQuestion {i + 1}: {QUESTIONS[i]["answer"]} {QUESTIONS[i]["name"]}')
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')
        # ans = str(QUESTIONS[i]["answer"])
        # check for the input validations
        if ans.lower() == "quit":
            print("You Won: ₹" + str(curmoney))
            break
        elif ans.lower() == "lifeline":
            if i != 14 and life > 0:
                QUESTIONS[i] = lifeLine(QUESTIONS[i])
                life -= 1
            else:
                print("sorry! You cannot use lifeline")
                input()
            i -= 1

        if ans.isnumeric():
            if isAnswerCorrect(QUESTIONS[i], int(ans)):
                # print the total money won.
                # See if the user has crossed a level, print that if yes
                curmoney = QUESTIONS[i]["money"]
                if i == 4 or i == 9:
                    minmoney = QUESTIONS[i]["money"]
                print('\nCorrect !')
            else:
                # end the game now.
                # also print the correct answer
                lose = True
                print('\nIncorrect !')
        else:
            print("\nenter a valid input!")
        # print the total money won in the end.
        if lose:
            print("You Won: ₹" + str(minmoney))
            break
        else:
            print("You Won: ₹" + str(curmoney))


kbc()
