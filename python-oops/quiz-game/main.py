from question_model import Question
from data import question_data
from quiz_brain import  QuizBrain

question_bank = []

for items in question_data:
    ques = Question(items["text"], items["answer"])
    question_bank.append(ques)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.nextquestion()

quiz.end_of_quiz()