# open the book and print the whole thing
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

#word count function
def wordcount():
    num_words = len(file_contents.split())
    return num_words
#wordcount()


#character count function
counts = {}
def charcount():
    for letter in file_contents.lower():
        if letter not in counts:
            counts[letter] = 1           
        elif letter in counts:
            counts[letter] += 1    
    return counts
charcount()

#nicer formatted character counts
letters_only_counts = {}
def letters_only(dict):
    return dict["count"]
sorted_counts = []
def sort_counts(dictionary):
    for entry, value in dictionary.items():
        if entry.isalpha() == True:
            letters_only_counts[entry] = value
    for char, count in letters_only_counts.items():
        sorted_counts.append({"char":char, "count":count})
sort_counts(counts)
sorted_counts.sort(reverse=True, key=letters_only)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{wordcount()} words found in the document\n")
for item in sorted_counts:
    print(f"The '{item['char']}' character was found {item['count']} times")
print("--- End report ---")