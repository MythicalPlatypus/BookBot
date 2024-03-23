def main():
    book_path = "books/Frankenstein.txt"
    # Read the book text.
    text = get_book_text(book_path)
    # Get total num. of words in the book.
    num_words = get_num_words(text)
    # Count the occurances of each character in the book.
    chars_dict = get_chars_dict(text)
    # Sorts the characters by frequency.
    chars_sorted_list  = chars_dict_to_sorted_list(chars_dict)
    # Count occurances of each word
    word_counts = get_word_counts(text)
    # Sort words by number of occurances.
    words_sorted_list = word_counts_to_sorted_list(word_counts)
     
    #Begin Printing the Report.
    print(f"--- Beginning a report of {book_path}--- ")
    print(f"{num_words} words found in the document")
    print()
    print("Occurances of each letter:")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character has been found {item['num']} times")
    print()
    print("Top 10 most used words.")
    for item in words_sorted_list[:10]: #slice to show 10 words.
        print(f"The word '{item['word']}' appears {item['num']} times")
    print()
    print("Top 10 least used words.")
    for item in words_sorted_list[-10:]: #slice to show 10 words.
        print(f"The word '{item['word']}' appears {item['num']} times")
    print()
    print(f"--- End of Report for {book_path}---")
    #End Report Print

# opens file as f and then returns content.
def get_book_text(path):
    with open(path) as f:
        return f.read()

# splits up each word using whitespace then returns the len (number of words) of the variable created.    
def get_num_words(text):
    words = text.split()
    return len(words)

# gets a dictionary with a count of every character in 'text'
def get_chars_dict(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

# key for sort()
def sort_on(d):
    return d["num"]

# sorts character dictionary
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def clean_text(text):
    #Clean the text by converting to lowercase and replacing punctuation with whitespace.
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    clean_text = text.lower()
    for p in punctuation:
        clean_text = clean_text.replace(p, ' ')
    return clean_text

def get_word_counts(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def word_counts_to_sorted_list(word_counts):
    sorted_list = [{
        "word": word,
        "num": count
    } for word, count in word_counts.items()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()