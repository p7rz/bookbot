def main():
    book_path = "books/Frankenstein.txt" #loon muutuja raamatu asukohaga
    text = open_book(book_path) #kasutan book_path muutujat koos open book funktsiooniga
    word_count = count_words(text) #kasutan text muutujas olevat teksti count_words funktsiooniga, et leida sõnade arv
    letter_counts = count_of_letter(text) #kasutan text muutujas olevat teksti count_of_letter funktsiooniga, et leida sõnade arv
    #printin väljundi, kasutades üleval määratud muutujaid
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    #see osa on selleks, et output oleks sorditud counti järgi kõrgemast madalamaks
    for i in sorted(letter_counts, key=letter_counts.get, reverse=True):
        print(f"The '{i}' character was found {letter_counts[i]} times") 
    print("--- End report ---")

#funktsioon avamaks tekstifaili ning selle sisse lugemiseks.
def open_book(book_path): 
    with open(book_path) as f:
        Book_contents = f.read()
        return Book_contents

#funktsioon sisse loetud teksti kasutamiseks, et leida sealt sönade arv    
def count_words(text):
    count_of_words = len(text.split())
    return count_of_words

#funktsioon sisse loetud teksti baasil tähtede arvu leidmiseks
def count_of_letter(text):
    text_lc = text.lower()   #teen kõik tähed lowercaseks
    letter_counts = {} #loon tühja dictionary
    for i in text_lc: #loopin kogu teksti läbi
        if i.isalpha(): #kasutan isalpha funktsiooni, et eemaldada special charid ja numbrid jms
            letter_counts[i] = letter_counts.setdefault(i, 0)+1 #setdefault funktsioon selleks, et määrata default count tähemärgile, kui see ei eksisteeri mu dictionarys. Kui see tekib, siis suurendab counti 1 võrra
    return letter_counts

main()