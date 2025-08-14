class QuizBrain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def stillHasQuestions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def nextQuestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.txt}?")
        print(f"your current score is: {self.score}")
        self.checkAnswer(user_answer, current_question.ans)

    def checkAnswer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you got the correct answer!")
        print(f"the correct answer was: {correct_answer}")
        print(f"your score is now {self.score}/{self.question_number}\n")
