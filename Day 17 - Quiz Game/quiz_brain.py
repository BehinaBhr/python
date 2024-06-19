# TODO: make a quiz brain class with q_number=0 , q_list to an input of question_bank as attriburts
# TODO: next_q method retrieve at the current question_number from the q_list
# TODO: input q_text and ask for answer
# TODO: make a method still_remain_question to return True or False
# TODO: add score=0 as an attribute and check_answer as a method

class QuizBrain:
    def __init__(self, q_list):
        self. q_number = 0
        self. q_list = q_list
        self.score = 0

    def still_remain_question(self):
        # if len(self.q_list) > self.q_number:
        #     return True
        # else:
        #     return False
        return len(self.q_list) > self.q_number


    def next_question(self):
        current_q = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_q.text} (True/ False): ")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("@@ You got it right! @@")
        else:
            print("!!! That's wrong !!!")
        print(f"The correct answer was: {correct_answer}")
        print(f"** Your score is {self.score}/{self.q_number} **")
        print("\n")
