class QuizBrain:
    
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)
        

    def next_question(self):
        current_qurstion = self.question_list[self.question_number]
        self.question_number += 1 
        user_asnwer = input(f"\nQ.{self.question_number}: {current_qurstion.text} (True/False):")
        self.check_answer(user_asnwer, current_qurstion.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1 
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"Te correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print('\n')

