def main():
    book_path = "books/frankenstein.txt"
    print(f"Starting the program on {book_path}")
    text = get_text(book_path)
    word_count = count_words(text)
    print(f"The book contains {word_count} words.")
    amount_of_chars = count_characters(text)
    for key, value in sorted(amount_of_chars.items(), key=lambda x: x[1], reverse=True):
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")

def get_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_characters(text):
    character_counts = {}
    for char in text.lower():
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def sort_on(list):
    return list


main()