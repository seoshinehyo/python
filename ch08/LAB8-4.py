# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# f = open('a.txt', 'r')   왜 안 되지??
# s = f.read()
# print(s)

# wordcloud = WordCloud(background_color='white', font_path='C:/Windows/Fonts/malgun.ttf')
# wordcloud.generate_from_text(s)

# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()
# f.close()

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 파일 경로를 절대 경로로 지정
file_path = 'C:/Users/82105/Desktop/SSH/3-1/python/python/ch08/a.txt'

# 파일 열기를 with 문으로 변경하여 자동으로 닫히게 처리, with 써서 파일 열기
with open(file_path, 'r', encoding='utf-8') as f:
    s = f.read()
    print(s)

# WordCloud 객체 생성 및 단어 구름 생성
wordcloud = WordCloud(background_color='white', font_path='C:/Windows/Fonts/malgun.ttf')
wordcloud.generate(s)

# 단어 구름 이미지 표시
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
