def main():
    with open("books/frankenstein.txt") as f:
        content = f.read()
        print(content)


if __name__ == "__main__":
    main()
