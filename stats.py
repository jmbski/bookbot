"""Simple utility functions for the bookbot project"""

from collections import defaultdict


def word_counter(text: str) -> int:
    """Retrieve the number of words in a text file

    Args:
        text (str): Text to process

    Returns:
        int: number of words (determined by white space)
    """

    words = text.split()
    return len(words)


def character_counter(text: str) -> dict[str, int]:
    """Get a total count for each distinct character in the provided text

    Args:
        text (str): Text to process

    Returns:
        dict[str, int]: Mapping of the characters and their individual
            counts sorted by value
    """

    char_counts: dict[str, int] = defaultdict(int)  # renamed
    text = text.lower()

    for char in text:
        if char.isalpha():
            char_counts[char] += 1

    # Convert dict.items() into a list of tuple[str,int] values
    entry_list: list[tuple[str, int]] = list(char_counts.items())

    # sort entries based on the second item in each tuple
    entry_list.sort(key=lambda x: x[1], reverse=True)

    # dict can accept a list of 2-value tuples (representing key-value pairs)
    # so cast our list[tuple[str,int]] as a dict for the return value
    return dict(entry_list)

    # ↓↓ Fancy one line way of writing it out ↓↓
    # return dict(sorted(char_counts.items(), key=lambda x: x[1], reverse=True))


""" 
    Removed the other two functions for sorting since it can be condensed 
    into the character_counter() function
"""
