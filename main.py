from stats import count_words, character_counts, convert_to_list, sort_on
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    word_count = count_words(book)
    char_dict = character_counts(book)
    dict_list = convert_to_list(char_dict)

    print("============ BOOKBOT ============\n" \
    "Analyzing book found at books/frankenstein.txt...")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in dict_list:
        print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        read_data = f.read()
    return read_data

if __name__ == "__main__":
    main()