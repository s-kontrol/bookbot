import os


def print_report(dict2array, dict):
    for k in dict2array:
        print(f"the {k} character was found {dict[k]} times")

def create_array(dict):
    a = []
    for k, v in dict.items():
        if k.isalpha():
            a.append(f"{k}")
    a.sort()
    return a
    
def get_characters_count(text):
    a = {}
    for line in text.split():
        for character in line.lower():
            if character in a:
                a[character] += 1
            else:
                a[character] = 1             
    return a

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():

    file_path = os.path.join('books', 'frankenstein.txt')
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    chars_dict = get_characters_count(text)
    print(f"{num_words} words found in the document")
    print(chars_dict)
    dict2array = create_array(chars_dict)
    print_report(dict2array, chars_dict)
main()