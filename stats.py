def count_words(file):
    count = 0

    for word in file.split():
        count += 1

    return count

def count_characters(file):
    character_count = {}
   
    for char in file.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count

def create_sorted_dicts(dictonary):
    dictornaies = []

    for key in dictonary:
        if key.isalpha():
            temp = {}
            temp["char"] = key
            temp["num"] = dictonary[key]

            dictornaies.append(temp)
        else:
            pass
    
    dictornaies.sort(reverse=True, key=sort_on)

    return dictornaies

def sort_on(items):
    return items["num"]

    