import json
import pprint

with open("./puzzles/crosswordPuzzles5x5.json", "r") as f:
    crosswords = json.load(f)


pprint.pprint(crosswords)

crossword = crosswords[0]
# TODO could have pixel art hint, or other types of hints
# TODO add in proper nones, it is missing countries, towns