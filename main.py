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

    print(character_count(content))


if __name__ == "__main__":
    main()
