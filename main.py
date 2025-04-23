from src.crossword_generator import create_crossword, board_input
import sys


def main():
    # input_content = sys.stdin.read()

    # print(input_content.split('\n'))
    board_input()
    # create_crossword(5, 5, False)



if __name__ == "__main__":

    main()

# TODO allow user to create any shape crossword, could do this from a text file passed into it with X (can't go) and O (Open for letters)
# TODO Add two more letters for input, ignore up/down, ignore left/right
# TODO can also make words down down up and right to left
# TODO ignore 1 word cross words
# TODO add website UI
# TODO get a list of proper nouns
# TODO add AFD program to Garmin workout to my Notion