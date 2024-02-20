def count_words(string):
    words = string.split()
    return len(words)


def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        print(f"There is {count_words(contents)} words")


main()
