class QuizBrain:
    # initialize a question_number=0 and question_list and score =0
    def __init__(self, q_list):

        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # it checks it reaches the length of question or not
    def still_has_question(self):
        # compare the question number with the length of question_list, and it should be less and return true
        if self.question_number < len(self.question_list):
            return True
        # if it exceeds length it prints false
        return False

    # it prints next question
    def next_question(self):
        # store the current question
        current_question = self.question_list[self.question_number]
        # question number increased by one everytime
        self.question_number = self.question_number + 1
        # display the question and takes the answer of the question
        output = input(f"Q.{self.question_number} : {current_question.text} (True/False) :")

        # it checks the answer is correct or not
        self.check_answer(output, current_question.answer)\


    # it checks the answer and takes user answer and correct answer of question
    def check_answer(self, user_answer, correct_answer):
        # compare the answer and increased the score
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score = self.score + 1

        else:
            print("That's wrong")
            print(f"Your Score is {self.score}")
        print(f"The correct answer was: {correct_answer}")
        print(f"The current store is {self.score}/{self.question_number} \n")
