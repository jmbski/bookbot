"""Simple boot.dev project to read text from file and provide statistics"""

import sys

import stats

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path_to_file: str) -> str:
    """Read text from filestream

    Args:
        path_to_file (str): Path to local file to read

    Returns:
        str: Text of the file
    """

    with open(path_to_file, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def main() -> None:
    """Main function"""

    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    dict_list = stats.character_counter(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path_to_file + "...")
    print("----------- Word Count ----------")
    print("Found", stats.word_counter(text), "total words")
    print("--------- Character Count -------")
    for char, count in dict_list.items():
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
