def main():
    with open("books/Frankenstein.txt") as f: 
        file_contents = f.read()
    return file_contents

def word_count():
    text = main()
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count


def character_count():
    text = main()
    characters = {}
    for character in text:
        lower_case = character.lower()
        if lower_case.isalpha():
            characters[lower_case] = characters.get(lower_case, 0) + 1 
    return characters

def sort_on(character):
    return character["count"]

def sort_dict():
    dict_into_list = []
    sorted_dict = character_count() 
    sorted_dict = sorted_dict.items()
    for key, value in sorted_dict:
        dictionary = {"character" : key, "count" : value}
        dict_into_list.append(dictionary)
    dict_into_list.sort(reverse = True, key = sort_on)
    for dict in dict_into_list:
        print(f"The '{dict['character']}' was found {dict['count']} times")



def final_report():
    wc = word_count()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wc} words found in the document")
    
    sort_dict()    
    print("--- End report ---")

print(final_report())



    
    






    
     





        
    




