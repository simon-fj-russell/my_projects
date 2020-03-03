from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from os import path, getcwd
import numpy as np
import matplotlib.pyplot as plt


def generate_wordcloud(words, mask):
    word_cloud = WordCloud(width=2279,
                           height=2246,
                           background_color='black',
                           stopwords=STOPWORDS,
                           mask=mask,
                           max_font_size=80,
                           min_font_size=4,
                           min_word_length=3
                           ).generate(words)
    plt.figure(figsize=(30, 20),facecolor='black', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    # plt.savefig('wordcloud.png', facecolor='k', bbox_inches='tight')

with open('_chat.txt', 'r') as f:
    text = []
    for line in f:
        text.append(line)

erin = []
simon = []
for x in text:
    if 'image omitted' in x:
      text.remove(x)
    elif 'Simon:' in x:
        simon.append(x.strip('\n').split('Simon:')[1])
    elif 'Silverberg:' in x:
        erin.append(x.strip('\n').split('Silverberg:')[1])

d = getcwd()
mask = np.array(Image.open(path.join(d, "heart2.png")))

words = ''
for word in simon:
    words += word.lower()

for word in erin:
    words += word.lower()

list_to_remove = ['hahaha',
                  'haha',
                  'good',
                  'yeah',
                  'know',
                  'now',
                  'will',
                  'think',
                  'one',
                  'want',
                  'really',
                  'yes',
                  'day',
                  'going',
                  'nice',
                  'time',
                  'dont',
                  'work',]
for remove in list_to_remove:
    words = words.replace(remove, '')


generate_wordcloud(words, mask)
