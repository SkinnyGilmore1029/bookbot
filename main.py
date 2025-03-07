def get_book_text(filepath:str)->str:
    with open(filepath) as f:
        file_contents:str = f.read()
    return file_contents

def main()->str:
    words = get_book_text("books/frankenstein.txt")
    spilt_words = words.split()
    print(str(len(spilt_words)) + " words found in the document")


    

if __name__ == "__main__":
    main()

