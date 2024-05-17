stop_words = ['is', 'and', 'the', 'a', 'an', 'in', 'of', 'to']

s = 'This is an example of removing stop words from a string.'
words = s.split()
filtered_sentence = [word for word in words if word.lower() not in stop_words]

print(f'입력={s}')
print(f'출력={" ".join(filtered_sentence)}')