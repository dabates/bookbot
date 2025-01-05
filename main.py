import os


def main():
    for filename in os.scandir("books"):
        if not filename.name.endswith(".txt"):
            continue

        print(f'--- Begin report of {filename.path} ---')

        with open(filename.path) as f:
            file_contents = f.read()
            print(count_words(file_contents), "words found in the document\n")
            for char, count in count_characters(file_contents.lower()).items():
                print(f"The {char} was found {count} times")

        print('--- End report ---')


def count_words(file_contents):
    return len(file_contents.split())


def count_characters(file_contents):
    counts = {}
    for char in file_contents:
        if 'a' <= char <= 'z':
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1

    return counts


if __name__ == '__main__':
    main()
