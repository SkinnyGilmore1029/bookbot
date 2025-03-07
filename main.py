def get_book_text(filepath:str)->str:
    with open(filepath) as f:
        file_contents:str = f.read()
    return file_contents

def main()->str:
    words = get_book_text("books/frankenstein.txt")
    print(words)

def count_words()->str:
    words = get_book_text("books/frankenstein.txt")
    counted_words = str(len(words.split()))
    print(count_words)
    

if __name__ == "__main__":
    main()
    count_words()
