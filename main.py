def get_book_text(filepath:str)->str:
    with open(filepath) as f:
        file_contents:str = f.read()
    return file_contents

def get_word_count(words)->str:
    counted_words = words.split()
    return len(counted_words)

def main()->str:
    words = get_book_text("books/frankenstein.txt")
    count_words = get_word_count(words)
    return len(count_words)


if __name__ == "__main__":
    main()

