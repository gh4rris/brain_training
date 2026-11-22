from config import DB_URL
from game import BrainTrainGame

import sys
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    engine = create_engine(DB_URL)
    Session = sessionmaker(engine)

    random.seed(666)
    try:
        game = BrainTrainGame(Session)
        game.start_game()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit()


if __name__ == "__main__":
    main()
