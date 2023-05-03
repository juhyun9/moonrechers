import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Okt
from nltk.corpus import stopwords


df = pd.read_excel('C:/result.xlsx')



var_data = [df[name].tolist() for name in df.columns]
             

#불용어
stop_words = stopwords.words('korean')
stop_words.extend(['을', '를', '이', '가', '은', '는', '에', '의', '로'])


comments_daa = []
  #이모지 제거
  emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
                           "]+", flags = re.UNICODE)
    data_str = ' '.join(map(str,df[name].tolist()))
    data_str = emoji_pattern.sub(r'', data_str)
    data_str = re.sub("[^가-힣ㄱ-ㅎㅏ-ㅣ\\s]", "" ,data_str)    
    comments_data.append(data_str) 
  
okt = Okt()

## 벡터화
vectorizer = TfidfVectorizer(stop_words = stop_words)

#리스트 문자열 변환
var_data_str = [' '.join(map(str, lst))for lst in var_data]

vectors = vectorizer.fit_transform([emoji_pattern.sub(r'', text)) for text in var_data_str]).toarray()

df_vectors = pd.DataFrame(vectors, columns = vectorizer.get_feature_names_out(), index = df.columns)
df_vectors.to_csv('C:/df_vector.csv', index = False)

comments_df = pd.DataFrame({'comments': comments_data})
comments_df.to_csv('C:/comments_data.csv', index=False)
