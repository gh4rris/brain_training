from question_generator import QuestionGenerator
from player_select import PlayerSelect
from models import Player
from utils import validate_number

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import update


class BrainTrainGame:
    def __init__(self, Session: sessionmaker[Session], turns: int=3) -> None:
        self.session = Session
        self.turns = turns
        self.player_select = PlayerSelect(Session)
        self.turn_question_dict = {}
        self.question_generator = QuestionGenerator()
        self.score= 0

    def __generate_questions(self) -> None:
        for i in range(1, self.turns + 1):
            question, answer = self.question_generator.choose_question()
            self.turn_question_dict[i] = (question, answer)

    def __evaluate_answer(self, user_answer: float, correct_answer: float) -> bool:
        return user_answer == correct_answer

    def __ask_question(self, turn: int, question: str) -> float:
        user_answer_str = input(f"{turn}. {question}: ")
        user_answer = validate_number(user_answer_str)
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

        if self.player_select.active_player:
            with self.session.begin() as session:
                session.execute(update(Player).values(best_score=self.score).where(Player.id == self.player_select.active_player.id))

        print(f"Final score: {self.score}/{self.turns}")

    def create_or_choose_player(self):
        self.player_select.active_player = self.player_select.choose_player()

