s = 'This movie was terrible! The acting was poor and the story was boring.'

# print(f's={s}')
# print(f'글자수={len(s)}')
# words = s.split()
# print(f'단어들의 리스트={words}')
# print(f'단어 수={len(words)}')
# print(f'평균 단어 길이={sum(len(word) for word in words) / len(words)}')

# print(s.count('#'))

print(f'글자수={len(s)}')
words = list(s.split())
print(f'단어들의 리스트={words}')
print(f'단어 수={len(words)}')
avg_len = sum(len(word) for word in words) / len(words)
print(f'평균 단어 길이={avg_len}')