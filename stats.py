def get_num_words(text):
    num_words = len(text.split())
    return (f'Found {num_words} total words')

def get_num_characters(text):
    character_dict = {}
    words = text.split()
    for word in words:
        lowercase_word = word.lower()
        for i in lowercase_word:
            if(i in character_dict):
                character_dict[i] += 1
            else:
                character_dict[i] = 1
    return character_dict

def sort_dictionary(character_count):
    sorted_keys = sorted(character_count)
    sorted_dict_by_keys = {}
    for key in sorted_keys:
        if(key.isalpha()):
            sorted_dict_by_keys[key] = character_count[key]

    return sorted_dict_by_keys