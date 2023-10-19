def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    word_count = count_words(text)
    letter_counts = count_letters(text)
    
    sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    
    print_report(book_path, word_count, sorted_letter_counts)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    counts = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts

def print_report(book_path, word_count, sorted_letter_counts):
    print(f"Report for: {book_path}")
    print(f"Total words: {word_count}")
    print("\nCharacter Frequencies:")
    for letter, count in sorted_letter_counts:
        print(f"\t{letter}: {count}")

main()