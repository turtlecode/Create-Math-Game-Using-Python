import random
import operator

operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

def chooseNum():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    return num_1,num_2

def operate(operation):
    
    pureInt=True
    while pureInt:
        num_1,num_2=chooseNum()
        answer = operators.get(operation)(num_1, num_2)
        if (operation=='/' and num_1<num_2) or (operation=='/' and answer!=num_1//num_2):
            pureInt=True
        else:
            pureInt=False
    
    return answer,num_1,num_2

def random_problem():
 
    operation = random.choice(list(operators.keys()))
    answer,num_1,num_2 = operate(operation)

       
    print(f'What is {num_1} {operation} {num_2}')
    return answer

def ask_question():
    answer = int(random_problem())
    try:
        guess = int(input('Enter you answer: '))
    except:
        print('It is not an integer!')
        return False

    return guess == answer

def game():
    score = 0
    while True:
        if ask_question() == True:
            score += 1
            print('Correct !')
        else:
            print('Incorrect')
            break
    print(f'======== Game Over ========\nYou score is {score}\nKepp going!')

game()