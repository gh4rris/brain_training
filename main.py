from game import Game


def main():
    game = Game()
    response = game.ask_question()
    print(response)


if __name__ == "__main__":
    main()
