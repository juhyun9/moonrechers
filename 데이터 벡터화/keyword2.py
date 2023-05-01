import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Okt
from nltk.corpus import stopwords


df = pd.read_csv('C:/yotuber.csv', encoding = 'CP949')



var_data = [df[name].tolist() for name in df.columns]
                # name = 열 ex) 'youtuber'

#불용어
stop_words = stopwords.words('korean')
stop_words.extend(['을', '를', '이', '가', '은', '는', '에', '의', '로'])


#이모지 제거
emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\"  # flags (iOS)
                           "]+", flags = re.UNICODE)

okt = Okt()

## 벡터화
vectorizer = TfidfVectorizer(stop_word = stop_words)
vectors = vectorizer.fit_transform([' '.join([okt.morphs(emoji_pattern.sub(r'', text)) for text in data]) for data in var_data]).toarray()

df_vectors = pd.DataFrame(vectors, columns = vectorizer.get_feature_names(), index = df.index)
df_vectors.index.name = 'youtuber'
df_vectors.columns.name = 'comments'
