from models import PlayerModel
from schemas import Player
from utils import validate_integer

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import select
from pydantic import ValidationError


class PlayerSelect:
    def __init__(self, Session: sessionmaker[Session]):
        self.session = Session
        self.active_player: Player | None = None

    def __get_choice_id(self, players: list[Player]) -> int:
        print("Select Player:")

        print("0. Create new player")
        for player in players:
            print(f"{player.id}. {player.name}")

        selected_id_str = input("Enter number: ")
        selected_id = validate_integer(selected_id_str)

        if selected_id == 0:
            return selected_id

        return selected_id or self.__get_choice_id(players)

    def __create_player(self, name: str) -> int:
        with self.session() as session:
            player = PlayerModel(
                name=name,
                best_score=None
            )
            session.add(player)
            session.commit()
            id = player.id
        print(f"Player {name} created\n")
        return id


    def choose_player(self) -> None:
        with self.session() as session:
            result = session.scalars(select(PlayerModel)).all()
            players = [Player.model_validate(p) for p in result]

        selected_id = self.__get_choice_id(players)

        if selected_id == 0:
            player_name = input("\nEnter player name: ")
            selected_id = self.__create_player(player_name)

        with self.session() as session:
            player_choice = session.get(PlayerModel, selected_id)

        try:
            self.active_player = Player.model_validate(player_choice)
            print(f"{self.active_player.name} selected!\n")
        except ValidationError:
            print("Player not found\n")
            self.choose_player()

