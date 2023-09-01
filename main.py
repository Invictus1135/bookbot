with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
def get_chars_dict(file_contents):
    chars = {}
    for c in file_contents:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
chars_dict = get_chars_dict(file_contents)
def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

print("--- End report ---")

