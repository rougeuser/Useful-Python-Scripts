def word_counter(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    result = word_counter(file_path)
    for word, count in result.items():
        print(f"{word}: {count}")
