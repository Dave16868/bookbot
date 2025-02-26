import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    # take string filepath and output its string contents
    with open(filepath) as f:
        content = f.read()
        return content    

from stats import text_to_num, text_to_char, chardict_sort

def main():
    text = get_book_text(sys.argv[1])
    number = text_to_num(text)
    char = text_to_char(text)
    sortlist = chardict_sort(char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for i in range(0,len(sortlist)):
        dic = sortlist[i]
        for key in dic:
            if key.isalpha() == True:
                print(f"{key}: {dic[key]}")
    print("============= END ===============")


main()

