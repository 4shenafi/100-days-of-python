class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f'Q.{self.question_number} {current_question.text} (True/False)?: ').title()
        self.check_answer(user_input, current_question.answer)

    def check_answer(self, user_input, correct_answer):
        if user_input == correct_answer:
            print("You've got the right answer!")
            self.score += 1
        else:
            print("You missed the answer!")
        print(f'Correct Answer: {correct_answer}')
        print(f'Score: {self.score}')
