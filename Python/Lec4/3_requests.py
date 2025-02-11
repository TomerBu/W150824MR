# pip install requests

# update pip version:
#  pip install --upgrade pip
import requests
import html
from random import shuffle

url = 'https://opentdb.com/api.php?amount=10'

response = requests.get(url)

json_data = response.json()

results_list = json_data['results']



for result in results_list:
    question = result['question']
    question = html.unescape(question)
    correct_answer = result['correct_answer']
    all_answers = result['incorrect_answers']


    # add correct answer to all answers
    # so we have all answers in one list
    all_answers.append(correct_answer)

    shuffle(all_answers)
    print('Question:', question)
    print(all_answers)

    # input of a number -> from 1 to 4
    # -1 converts the int to 0 to 3
    user_choice = int(input('enter your answer: 1 to 4:')) - 1

    if correct_answer == all_answers[user_choice]:
        print('Correct!')
    else:
        print('Wrong! The correct answer is:', correct_answer)
    


