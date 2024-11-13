def count(files):
    with open(files, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

files = 'file_here'
word_count = count(files)
print(f"Number of words: {word_count}")
