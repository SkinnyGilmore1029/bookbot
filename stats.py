def get_word_count(words)->str:
    counted_words = words.split()
    return len(counted_words)

def get_characters(words)->None:
    words_list = words.split().lower()
    character_dict:dict[str,int] = {}
    for w in words_list:
        if character_dict[w] in character_dict.keys():
            character_dict[w] +=1
        elif character_dict[w] not in character_dict.keys():
            character_dict[w] = 1
    return character_dict