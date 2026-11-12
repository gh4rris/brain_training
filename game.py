from question_generator import QuestionGenerator

import sys


class BrainTrainGame:
    def __init__(self, turns: int=3) -> None:
        self.turns = turns
        self.turn_question_dict = {}
        self.question_generator = QuestionGenerator()
        self.score= 0

    def __generate_questions(self) -> None:
        for i in range(1, self.turns + 1):
            question, answer = self.question_generator.choose_question()
            self.turn_question_dict[i] = (question, answer)

    def __validate_number(self, user_answer_str: str) -> float | None:
        if user_answer_str == "/q":
            print("Goodbye!")
            sys.exit()

        try:
            return float(user_answer_str)
        except ValueError:
            print("Please enter a number\n")

    def __evaluate_answer(self, user_answer: float, correct_answer: float) -> bool:
        return user_answer == correct_answer

    def __ask_question(self, turn: int, question: str) -> float:
        user_answer_str = input(f"{turn}. {question}: ")
        user_answer = self.__validate_number(user_answer_str)
        return user_answer or self.__ask_question(turn, question)


    def start_game(self):
        self.__generate_questions()
        for turn, (question, correct_answer) in self.turn_question_dict.items():
            user_answer = self.__ask_question(turn, question)
            if self.__evaluate_answer(user_answer, correct_answer):
                self.score += 1
                print("Correct!\n")
            else:
                print(f"Incorrect! Answer was: {correct_answer}\n")
        print(f"Final score: {self.score}/{self.turns}")

