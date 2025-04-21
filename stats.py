def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    lowered = text.lower()
    char_dict = {}
    for char in lowered:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_char_dict(char_dict):
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_dict)
