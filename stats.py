def get_word_count(words)->str:
    counted_words = words.split()
    return len(counted_words)

def get_characters(words)->dict[str,int]:
    lower_case_words = words.lower()
    words_list = lower_case_words.split()
    character_dict:dict[str,int] = {}
    for word in words_list:
        for letter in word:
            if letter not in character_dict:
                letter.lower()
                character_dict[letter] = 1
            else:
                character_dict[letter] +=1
    return character_dict

def sort_key(dict_to_sort)->int:
    return dict_to_sort["count"]

def make_dict_list(words:str)->None:
    char_dict = get_characters(words)
    dict_list = []
    for k ,v in char_dict.items():
        dict_list.append({"char":k,"count":v})
    dict_list.sort(reverse=True,key=sort_key)
    print(f"{" BOOKBOT ":=^24}\n"
          f"Analyzing book found at books/frankenstein.txt...\n"
        f"{" Word Count ":-^26}\n"
        f"Found {get_word_count(words)} total words\n"
        f"{" Character Count ":-^32}")
    for d in dict_list:
        print(f"{d["char"]}: {d['count']}")
    
