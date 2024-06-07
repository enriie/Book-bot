

def count_characters(text: str):
    result = {}

    for c in text:
        if c not in result.keys():
            result[c] = 0
        result[c] += 1
    return result

def main():
    file_contents = None
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = file_contents.split()
    print(len(words))

    text = file_contents.lower()

    data = count_characters(text)
    
    sorted_data = sorted(data.items(), reverse=True, key=lambda x:x[-1])
    for entry in sorted_data:
        if entry[0].isalpha():
            print(f"The \'{entry[0]}\' character was found {entry[1]} times")

if __name__ == '__main__':
    main()
