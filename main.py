import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

from stats import word_counter

from stats import character_counter

from stats import sort_on

from stats import tuples_to_sorted_dicts


def main():
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    dict_list = tuples_to_sorted_dicts(character_counter(text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path_to_file + "...")
    print("----------- Word Count ----------")
    print("Found", word_counter(text), "total words")
    print("--------- Character Count -------")
    for item in dict_list:
        if item["char"].isalpha():
            print(item["char"] + ":", item["num"])
    print("============= END ===============")
    

main()


