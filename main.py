from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for quests in question_data:
    question = quests["text"]
    answer = quests["answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


