def text_to_num(content):
    # take string contents and output (string) word count
    word_counter = 0
    word_list = content.split()
    for i in word_list:
        word_counter += 1
    return word_counter

def text_to_char(content):
    # count the number of each character, including spaces etc.
    chardict = {}
    content_lower = content.lower()
    for i in content_lower:
        if i in chardict:
            chardict[i] += 1
        else:
            chardict[i] = 1
    return chardict

def chardict_sort(chardict):
    # break dictionary down to list of dictionaries each with single key-value pair
    chardict_list = []
    for key in chardict:
        chardict_list.append({key: chardict[key]})
    # sort the list of dictionaries based on the value(# of that character) of each key (character e.g. "a")
    chardict_list.sort(reverse=True, key=sort)
    return chardict_list
    
def sort(chardict):
    for key in chardict:
        return chardict[key]

