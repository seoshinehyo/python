from wordcloud import WordCloud
wordcloud = WordCloud()
text = 'Hello Hello Hello This is a word cloud example.'
wordcloud.generate(text)

import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

