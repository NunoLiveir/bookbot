from stats import count_words
from stats import count_characters



def get_book_text(filepath):
    """Return the entire contents of the file as a string."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def main():
     text = get_book_text("books/frankenstein.txt")
     print(f"Found {count_words(text)} total words")

     char_counts = count_characters(text)
     print(char_counts)
     

main()
