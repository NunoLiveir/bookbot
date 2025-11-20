
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    return char_counts

def sort_char_counts(char_dict):
    
    sorted_list = [{"char": c, "num": n} for c, n in char_dict.items()]


    def sort_by_num(item):
            return item["num"]

    sorted_list.sort(key=sort_by_num, reverse=True)
    return sorted_list
