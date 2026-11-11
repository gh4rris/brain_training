from question_generator import QuestionGenerator


class Game:
    def __init__(self, turns: int=10) -> None:
        self.turns = turns
        self.question_generator = QuestionGenerator()

    def _get_question(self) -> str:
        return self.question_generator.addition_generation()

    def ask_question(self) -> str | None:
        question = self._get_question()
        user_answer = input(f"{question}: ")
        try:
            user_answer = float(user_answer)
        except ValueError:
            print("Please enter a number")
            return
        return "Correct!" if self._evaluate_answer(user_answer) else "Incorrect!"

    def _evaluate_answer(self, user_answer: float) -> bool:
        return user_answer == self.question_generator.answer
