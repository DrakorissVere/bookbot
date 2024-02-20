def count_letters(string):
    string = string.lower()
    letters = {}

    for c in string:
        if not c.isalpha():
            continue

        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

    return dict(sorted(letters.items(), key=lambda i: i[1], reverse=True))


def print_letters_report(dictionary):
    for c in dictionary:
        print(f"The '{c}' character was found {dictionary[c]} times")


def count_words(string):
    words = string.split()
    return len(words)


def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        print(f"{count_words(contents)} words found in the document\n")
        print_letters_report(count_letters(contents))


main()
