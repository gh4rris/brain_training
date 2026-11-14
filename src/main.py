from config import DB_URL
from game import BrainTrainGame
from player_select import PlayerSelect
from models import Base

import sys
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)

    # player_select = PlayerSelect(engine)
    # player_select.create_player("George")
    # player = player_select.choose_player()
    random.seed(666)
    try:
        game = BrainTrainGame(Session)
        game.start_game()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit()


if __name__ == "__main__":
    main()
