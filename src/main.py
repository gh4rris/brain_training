from config import DB_URL
from game import BrainTrainGame

import sys
import random


def main():
    random.seed(666)
    try:
        game = BrainTrainGame(DB_URL)
        game.start_game()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit()


if __name__ == "__main__":
    main()
