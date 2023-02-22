class QuizBrain:
    def __init__(self, ques):
        self.question_number = 0
        self.question_list = ques
        self.score = 0

    def nextquestion(self):
        next_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {next_question.text}. (True/False)?: ")
        self.check_answer(next_question.answer, choice)

    def check_answer(self, correct_answer, user_answer):
        if correct_answer.lower() == user_answer.lower():
            print("Your answer was correct")
            self.score += 1
        else:
            print("your answer was wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your Current score is: {self.score}/{self.question_number}\n")

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def end_of_quiz(self):
        print("---------------------------------------------------------")
        print("You've completed the quiz")
        print(f"your final score was: {self.score}/{self.question_number}")
