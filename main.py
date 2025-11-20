from stats import count_words, count_characters, sort_char_counts
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():

    # Check for correct CLI usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    text = get_book_text(filepath)

    # Word count
    word_count = count_words(text)

    # Character counts
    char_counts = count_characters(text)
    sorted_chars = sort_char_counts(char_counts)

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")

main()
