def get_word_count(contents):
    split_contents = contents.split()
    return len(split_contents)


def count_chars(contents):
    lowered_contents = contents.lower()
    char_dict = {}
    for char in lowered_contents:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def sort_on(items):
    return items["num"]


def sort_chars_dict(char_dict):
    list_of_chars = []
    for key, value in char_dict.items():
        letter = {}
        letter["char"] = key
        letter["num"] = value
        list_of_chars.append(letter)
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars
