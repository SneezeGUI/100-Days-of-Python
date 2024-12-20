from question_model import Question
from ui import QuizInterface
from data import question_data
from quiz_brain import QuizBrain

# import requests
#
# request = requests.get(url="https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean")
# request.raise_for_status()
#
# data = request.json()['results']
# question_bank = []
# for result in data:
#     question_text = result["question"]
#     question_answer = result["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)
    # print(result)
    # print(question_bank)


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

