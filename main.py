def get_book_text(filepath):
    """Return the entire contents of the file as a string."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
     text = get_book_text("books/frankenstein.txt")
     print(text)

main()
