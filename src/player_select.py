from models import Player
from utils import validate_integer

from typing import Sequence
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import select


class PlayerSelect:
    def __init__(self, Session: sessionmaker[Session]):
        self.session = Session
        self.active_player: Player | None = None

    def __get_choice_id(self, players: Sequence[Player]) -> int | None:
        print("Select Player:")

        print("0. Create new player")
        for player in players:
            print(f"{player.id}. {player.name}")

        selected_id_str = input("Enter number: ")
        selected_id = validate_integer(selected_id_str)

        return selected_id or self.__get_choice_id(players)

    def __create_player(self, name: str) -> int:
        with self.session() as session:
            player = Player(
                name=name,
                best_score=None
            )
            session.add(player)
            session.commit()
        print(f"Player {name} created")
        return player.id


    def choose_player(self) -> Player | None:
        with self.session() as session:
            players = session.scalars(select(Player)).all()

        selected_id = self.__get_choice_id(players)

        if selected_id == 0:
            selected_id = self.__create_player("Bob")

        with self.session() as session:
            player = session.scalar(select(Player).where(Player.id == selected_id))

        if player:
            print(f"{player.name} selected!")
        else:
            print("player not found")
            self.choose_player()

        return player

