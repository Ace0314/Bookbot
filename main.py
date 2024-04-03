def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    count = get_word_count(words)
    character_count = get_character_count(text)
    charcter_count_sorted = character_count_sort(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document.")
    print()

    for item in charcter_count_sorted:
        print(f"The {item['char']} character was found {item['num']} times")

    print("--- End report ---")
    

def sort_on(l):
    return l["num"]

def character_count_sort(character_count):
    sorted = []
    for c in character_count:
        sorted.append({"char": c, "num": character_count[c]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(word):
    num = 0
    for n in word:
        num += 1
    return num

def get_character_count(text):
    lowercase = text.lower()
    count = {}
    for c in lowercase:
        if c.isalpha():
            if c in count:
                count[c] += 1
            else:
                count[c] =1
    
    return count

    

main()