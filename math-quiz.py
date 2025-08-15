import random


def quation_generatot():
    a = random.randint(1 , 9)
    b = random.randint(1, 9)
    operator_list = ["+" , "-" , "*"]
    selected_operator = random.choice(operator_list)
    print(f"{a} {selected_operator} {b} = ?")
    
    if selected_operator == "+":
        return a + b
    elif selected_operator =="-":
        return a - b
    else:
        return a*b


question_number_limit = 5
question_number = 0
score = 0

while question_number < question_number_limit :
    result = str(quation_generatot())

    user_answer = input('Enter your answer: ')

    if result == user_answer:
        score +=1
        print (f"Perfect , score: {score}")
    else:
        print(f"Sorry, your answer is wrong")




    question_number += 1

