def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list  = chars_dict_to_sorted_list(chars_dict)
    
    print(f"--- Beginning a report of {book_path}--- ")
    print(f"{num_words} words found in the document")
    print()
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character has been found {item['num']} times")
    print(f"--- End of Report for {book_path}---")

#splits up each word using whitespace then returns the len (number of words) of the variable created.    
def get_num_words(text):
    words = text.split()
    return len(words)

#key for sort()
def sort_on(d):
    return d["num"]

#sorts character dictionary
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

#gets a dictionary with a count of every character in 'text'
def get_chars_dict(text):
    chars = {}
    for c in text:
        book = c.lower()
        if book in chars:
            chars[book] += 1
        else:
            chars[book] = 1
    return chars

#opens file as f and then returns content.
def get_book_text(path):
    with open(path) as f:
        return f.read()
main()