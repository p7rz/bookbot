def count_words(s):
    return len(s.split())

def character_counts(s):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z', 'x', 'y']
    char_dict = {}
    for char in s.lower():
        if char not in char_dict and char in chars:
            char_dict[char] = 1
        elif char in char_dict and char in chars:
            char_dict[char] += 1
        else:
            continue
    
    return char_dict

def convert_to_list(dict):
    char_list = []
    for key, value in dict.items():
        temp_dict = {}
        temp_dict["char"] = key
        temp_dict["num"] = value
        char_list.append(temp_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict["num"]