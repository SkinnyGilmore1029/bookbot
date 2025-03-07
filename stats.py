def get_word_count(words)->str:
    counted_words = words.split()
    return len(counted_words)

def get_characters(words)->None:
    words_list = words.split()
    character_dict:dict[str,int] = {}
    for word in words_list:
        word.lower()
        for w in word:
            if w in character_dict.keys():
                w +=1
            elif w not in character_dict.keys():
                w = 1
    return character_dict