"""Simple boot.dev project to read text from file and provide statistics"""

import argparse
import sys

import stats


""" 
    This part here is a more advanced way to handle command line arguments
    Not strictly necessary at all, and sys.argv is perfectly fine for 
    single arg commands like this one. Just wanted to show an example of
    using argparse with a simple scenario
"""
parser = argparse.ArgumentParser(description=__doc__)
# __doc__ is a built-in variable that returns the docstring for the file

parser.add_argument("src_path", help="Path to file to check")
args = parser.parse_args()


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

    text = get_book_text(args.src_path)
    char_counts = stats.character_counter(text)  # renamed for clarity

    # Just demonstrating an alternate way to build str variables
    header: str = (
        "============ BOOKBOT ============\n"  # <- do note however, newlines have to be appended
        f"Analyzing book found at {args.src_path}...\n"
        "----------- Word Count ----------\n"
        f"Found {stats.word_counter(text)} total words\n"
        "--------- Character Count -------"
    )

    print(header)
    for char, count in char_counts.items():
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


# Rather than just doing main() out in the open, common practice is to
# hide it under a condition on __name__. __name__ is another built-in that
# returns the name of the module. Typically, module = filename, except if
# the module being executed is the initial one (i.e., the file that you
# run `python3 <file_name>` on), in which case the __name__ will always
# be "__main__". This prevents the code from being executed if this module
# were ever imported somewhere else.
#
# Not a worry in this simple example project, but it's a good habit to
# get into
if __name__ == "__main__":
    main()
