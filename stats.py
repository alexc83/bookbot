# sort helper method
def sort_on(items):
    return items["num"]

def get_word_count(book_contents):
    book_words_list = book_contents.split()
    number_of_words = len(book_words_list)
    return number_of_words

def get_character_counts(book_contents):
    characters_found = set()
    character_counts = {}

    for character in book_contents:
        char_lower = character.lower()
        if char_lower in characters_found:
            character_counts[char_lower] += 1
        else:
            characters_found.add(char_lower)
            character_counts[char_lower] = 1

    return character_counts

def get_sorted_character_dict(character_counts):

    sorted_character_counts = []
    # create dictionaries
    for key in character_counts:
        this_character_count = {
            "name": key,
            "num": character_counts[key]
        }
        sorted_character_counts.append(this_character_count)

    # sort
    sorted_character_counts.sort(reverse=True, key=sort_on)

    return sorted_character_counts
