def count_letters(string):
    string = string.lower()
    letters = {}

    for c in string:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

    return letters


def count_words(string):
    words = string.split()
    return len(words)


def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        print(f"There is {count_words(contents)} words")
        print("There are this amount of symbols:")
        print(count_letters(contents))


main()
