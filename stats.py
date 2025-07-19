def word_counter(text):
    words = text.split()
    return len(words)

def character_counter(text):
    characters_set = {}
    no_caps_characters = text.lower()
    for char in no_caps_characters:
        if char.isalpha():
            if char in characters_set:
                characters_set[char.lower()] += 1
            else:
                characters_set[char.lower()] = 1
    return characters_set

def sort_on(items):
    return items["num"]

def tuples_to_sorted_dicts(characters_set):
    dict_list = []
    tuple_to_dict = {}
    for tuple in characters_set.items():
        tuple_to_dict = {
           "char" : tuple[0],
           "num" : tuple[1]
        }
        dict_list.append(tuple_to_dict)
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list


    
        