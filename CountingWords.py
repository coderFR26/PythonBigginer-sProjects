from collections import Counter

contents = ''
with open('file.txt', 'r') as f:
    contents = f.read()

words_collection = Counter(contents.split())

print(f'{"WORD":>8} {"COUNT":>10}')
for word, count in words_collection.items():
    print(f'{word:>8} {count:>10}')

print(f'Number of unique words: {len(words_collection)}')