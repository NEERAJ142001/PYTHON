from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create a question_bank list
question_bank = []

for items in question_data:
    # adding text of question_data into question_text
    question_text = items["text"]

    # adding text of question_data into question_answer
    question_answer = items["answer"]

    # create an object new_question and call the Question class
    new_question = Question(question_text, question_answer)

    # adding new_question object to question_bank list
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
score = 0

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the Quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")


