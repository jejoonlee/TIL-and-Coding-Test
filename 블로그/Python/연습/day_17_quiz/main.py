from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append((Question(question['text'], question['answer'])))

question = QuizBrain(question_bank)

while question.still_has_question() == True:
    question.next_question()

    
print("You've completed the quiz")
print(f"Your final score was: {question.score}/{question.question_number}")