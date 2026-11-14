from models import Player

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import select


class PlayerSelect:
    def __init__(self, Session: sessionmaker[Session]):
        self.session = Session

    def choose_player(self) -> Player:
        with self.session() as session:
            players = session.scalars(select(Player))

        print("Select Player:")
        print("0. Create new player")
        for player in players:
            print(f"{player.id}. {player.name}")
        selected_id = input("Enter number: ")

        player = self.session.scalar(select(Player).where(Player.id == selected_id))
        if player:
            print(player.name)
        else:
            print("No player exists")
        return player

    def create_player(self, name: str):
        with self.session() as session:
            player = Player(
                name=name,
                best_score=None
            )
            session.add(player)
            session.commit()
        print(f"Player {name} created")
