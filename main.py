import sys

from stats import count_chars, get_word_count, sort_chars_dict


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    contents = get_book_text(path)
    char_count = count_chars(contents)
    sorted_chars = sort_chars_dict(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(contents)} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        else:
            continue
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents


main()
