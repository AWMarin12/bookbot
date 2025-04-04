import sys
from stats import get_num_words, get_count_chars, get_sorted_count_chars

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book = get_book_text("./" + book_path)
        num_words = get_num_words(book)
        sorted_count_chars = get_sorted_count_chars(get_count_chars(book))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for k in sorted_count_chars:
            print(f"{k["Character"]}: {k["Count"]}")
        print("============= END ===============")

main()
