import sys

from stats import (
    get_word_count,
    get_character_counts,
    get_sorted_character_dict)

def get_book_text(filepath):
   with open(filepath) as file:
       book_content = file.read()
       return book_content

def print_report(file_path, num_of_words, sorted_character_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")

    for char_count in sorted_character_counts:
        if char_count["name"].isalpha():
            print(f"{char_count["name"]}: {char_count["num"]} ")



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_contents = get_book_text(file_path)
    num_of_words = get_word_count(book_contents)
    character_counts = get_character_counts(book_contents)
    sorted_counts = get_sorted_character_dict(character_counts)
    print_report(file_path, num_of_words, sorted_counts)


# execute main
if __name__ == "__main__":
    main()
