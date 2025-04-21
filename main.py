from stats import get_word_count, get_char_count, sort_char_dict
import sys


def get_book_text(file_path):
    with open(file_path) as file:
        contents = file.read()
        return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    contents = get_book_text(file_path)
    num_of_words = get_word_count(contents)
    char_dict = get_char_count(contents)
    sorted = sort_char_dict(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for char in sorted:
        if char.isalpha():
            print(f"{char}: {sorted[char]}")
    print("============= END ===============")


main()
