from stats import get_num_words, get_num_characters, sort_dictionary
import sys

def get_book_text(file_path):

    word_count = None
    character_count = None
    #Prints the contents from file_path.

    #Parameters:
    #    file_path (str):The relative file path.
 
    with open(file_path) as f:
        print(f'Analyzing book found at {file_path}...')

        file_contents = f.read()
        word_count = get_num_words(file_contents)
        character_count = get_num_characters(file_contents)

    return word_count, character_count

    
if __name__=="__main__":
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    word_count, character_count = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    sorted_dictionary = sort_dictionary(character_count)
    for character in sorted_dictionary:
        print(f'{character}: {sorted_dictionary[character]} \n')
