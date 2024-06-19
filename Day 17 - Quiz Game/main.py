# TODO: make a quiz
# TODO: asking next_q in a loop until there are q
# TODO: checking if answer was correct
# TODO: checking if is the end of game

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q_data in question_data:
    q_data_text = q_data["text"]
    q_data_answer = q_data["answer"]
    question_bank.append(Question(q_data_text, q_data_answer))

quiz = QuizBrain(question_bank)
while quiz.still_remain_question():
    quiz.next_question()

print("You've complete the quiz.")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")


