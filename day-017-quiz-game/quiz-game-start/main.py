from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#
question_bank = []
for i in range(len(question_data)):
    question_txt = question_data[i]["question"]
    answer = question_data[i]["correct_answer"]
    new_question = Question(question_txt, answer)
    question_bank.append(new_question)


gameTest = QuizBrain(question_bank)
while(gameTest.stillHasQuestions()):
    gameTest.nextQuestion()

print("you've completed the quiz")
print(f"your final score is {gameTest.score}/{gameTest.question_number}")
