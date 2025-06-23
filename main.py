from stats import(
    count_words, 
    count_characters, 
    create_sorted_dicts
    )
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_report(filepath, word_count, dlist):
    if len(sys.argv) < 2:
        raise Exception
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")

        for dict in dlist:
            print(f"{dict["char"]}: {dict["num"]}")

        print("============= END ===============")

def main():
    try:
        filepath = sys.argv[1]
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    dictonary_list = create_sorted_dicts(character_count)

    print_report(filepath, word_count, dictonary_list)
    

main()

