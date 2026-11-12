from game import BrainTrainGame

import sys
import random


def main():
    random.seed(666)
    try:
        game = BrainTrainGame()
        game.start_game()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit()


if __name__ == "__main__":
    main()
