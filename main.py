def world_count(text):
    words = text.split()
    return len(words)


def character_count(text):
    characters = {}

    for character in text:
        character = character.lower()
        try:
            characters[character] += 1
        except KeyError:
            characters[character] = 1

    return characters


def main():
    content = ""
    with open("books/frankenstein.txt") as f:
        content = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{world_count(content)} words found in the document\n")
    for char, amount in character_count(content).items():
        print(f"The '{char}' character was found {amount} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
