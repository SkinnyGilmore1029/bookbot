from stats import get_word_count,get_characters,make_dict_list

def get_book_text(filepath:str)->str:
    with open(filepath) as f:
        file_contents:str = f.read()
    return file_contents


def main()->str:
    words = get_book_text("books/frankenstein.txt")
    make_dict_list(words)


if __name__ == "__main__":
    main()

