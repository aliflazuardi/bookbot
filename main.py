from stats import count_words, count_characters, sort_char_count_dict
import sys


def get_file_path(filepath):
    file_content = ""
    with open(filepath) as f:
        file_content = f.read()
    return file_content


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
filepath = sys.argv[1]


def main():
    print("============ BOOKBOT ============")

    book = get_file_path(filepath)
    print(f"Analyzing book found at {filepath}...")

    print("----------- Word Count ----------")
    num_words = count_words(book)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    counts = count_characters(book)
    stats = sort_char_count_dict(counts)
    for stat in stats:
        if stat["char"].isalpha():
            print(f"{stat['char']}: {stat['num']}")

    print("============= END ===============")


main()
