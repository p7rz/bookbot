def main():
    book_path = "books/Frankenstein.txt"
    text = open_book(book_path)
    word_count = count_words(text)
    letter_counts = count_of_letter(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for i in sorted(letter_counts, key=letter_counts.get, reverse=True):
        print(f"The '{i}' character was found {letter_counts[i]} times")
    print("--- End report ---")

def open_book(book_path):
    with open(book_path) as f:
        Book_contents = f.read()
        return Book_contents
    
def count_words(text):
    count_of_words = len(text.split())
    return count_of_words

def count_of_letter(text):
    text_lc = text.lower()
    letter_counts = {}
    for i in text_lc:
        if i.isalpha():
            letter_counts[i] = letter_counts.setdefault(i, 0)+1
    return letter_counts

main()