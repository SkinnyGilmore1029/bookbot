from stats import get_word_count,get_characters,make_dict_list
import sys

def get_book_text(filepath:str)->str:
    with open(filepath) as f:
        file_contents:str = f.read()
    return file_contents

def print_report(book_path:str,num_words:int,dict_list:list[dict[str,str|int]])->None:
    print(f"{" BOOKBOT ":=^24}\n"
          f"Analyzing book found at {book_path}...\n"
        f"{" Word Count ":-^26}\n"
        f"Found {num_words} total words\n"
        f"{" Character Count ":-^32}")
    for d in dict_list:
        print(f"{d["char"]}: {d['count']}")

def main()->str:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    chars_dict = get_characters(text)
    dict_lists = make_dict_list(chars_dict)
    print_report(book_path,num_words,dict_lists)


if __name__ == "__main__":
    main()

