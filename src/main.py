from config import DB_URL
from game import BrainTrainGame
from models import Base

import sys
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)

    random.seed(666)
    try:
        game = BrainTrainGame(Session)
        game.create_or_choose_player()
        game.start_game()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit()


if __name__ == "__main__":
    main()
