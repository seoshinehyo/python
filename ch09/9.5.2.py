from wordcloud import WordCloud
wordcloud = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf')
text = '안녕 안녕 안녕 이것은 워드 클라우드 예제야.'
wordcloud.generate(text)

import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# 한글은 지원 안 해서 네모 박스로 나옴 -> 경로 지정해주기