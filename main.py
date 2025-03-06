def get_book_text(filepath:str)->str:
    with open(filepath) as f:
        file_contents:str = f.read()
    return file_contents

def main(filepath:str)->str:
    words = get_book_text(filepath)
    return words

if __name__ == "__main__":
    main()
