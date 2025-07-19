import pprint
import pytest
from crossword_generator import (
    TrieNode,
    create_crossword,
    input_to_board,
    load_and_build_tries_of_diff_lengths,
    unique_word_length,
)


def test_unique_word_length_simple():
    board = [["o", "o"], ["o", "o"]]
    assert unique_word_length(board) == {2}


def test_unique_word_length_simple2():
    board = [["o", "x"], ["o", "o"]]
    assert unique_word_length(board) == {1, 2}


def test_unique_word_length_one_x():
    board = [["o", "o", "x"], ["o", "o", "o"], ["o", "o", "o"]]
    assert unique_word_length(board) == {2, 3}


def test_unique_word_length_two_xs():
    board = [["o", "o", "x"], ["o", "x", "o"], ["o", "o", "o"]]
    assert unique_word_length(board) == {1, 2, 3}


def test_unique_word_length_all_xs():
    board = [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
    assert unique_word_length(board) == set()


def test_input_to_board_o():
    text = """oOo
ooO
Ooo"""
    assert input_to_board(text) == [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]]


def test_input_to_board_x():
    text = """xXx
xxX
Xxx"""
    assert input_to_board(text) == [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]


def test_input_to_board_invalid():
    text = "xx\nxxx"
    with pytest.raises(ValueError):
        input_to_board(text)


def test_load_and_build_tries_of_diff_lengths():
    uniques = set([3, 4])
    tries = load_and_build_tries_of_diff_lengths(uniques, "popular_dictionary.txt")
    assert tries.keys() == uniques
    for num in tries.keys():
        assert type(tries[num]) == TrieNode


def test_create_crossword():
    crosswords = create_crossword(5, 5, False, "./tests/test_words_small.txt")
    pprint.pprint(crosswords)
    assert crosswords == [
        [
            ["a", "b", "b", "o", "t"],
            ["c", "r", "i", "m", "e"],
            ["h", "a", "t", "e", "s"],
            ["e", "v", "e", "n", "t"],
            ["s", "a", "s", "s", "y"],
        ],
        [
            ["a", "c", "h", "e", "s"],
            ["b", "r", "a", "v", "a"],
            ["b", "i", "t", "e", "s"],
            ["o", "m", "e", "n", "s"],
            ["t", "e", "s", "t", "y"],
        ],
    ]
