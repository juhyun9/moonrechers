import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Okt
#이제 nltk 한국어 불용어 지원안하는 듯. korean 파일만 없음
#from nltk.corpus import stopwords
#nltk.download('stopwords')


df = pd.read_csv('sourc/crawling.csv')
youtubernum=len(df)


#이모지 제거
emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
                           "]+", flags = re.UNICODE)

'''
#불용어 목록 입력
bull = []
inputword=str()
while inputword != 'no':
    inputword = input()
    bull.append(inputword)
bull.remove('no')

#불용어 리스트 저장
with open('sourc/bull.pkl','wb') as f :
    pickle.dump(bull,f)
'''
#불용어 제거
import pickle
#불용어 리스트 불러오기
with open ('sourc/bull.pkl','rb') as f: 
    bullword = pickle.load(f)

okt = Okt()
stop_words = bullword
#stop_words = set(stop_words.split(''))

comments_data = []

def process_data(data_str):
  data_str = emoji_pattern.sub(r'', data_str)
  data_str = re.sub("[^가-힣ㄱ-ㅎㅏ-ㅣ\\s]", "" ,data_str)
  data_str = re.sub('[^\w\d\s]','',data_str)

  word_tokens = okt.morphs(data_str)
  result = [word for word in word_tokens if not word in stop_words]

  comments_data.append(data_str)
  return comments_data



df['clean_com'] = df['comments'].apply(process_data)

comments_data = data_str.split()
df['clean_word'] = pd.Series(data_str)

## 벡터화
vectorizer = TfidfVectorizer()

#리스트 문자열 변환
var_data_str = [' '.join(map(str, lst))for lst in var_data]

vectors = vectorizer.fit_transform([(emoji_pattern.sub(r'', text)) for text in var_data_str]).toarray()

df_vectors = pd.DataFrame(vectors, columns = vectorizer.get_feature_names_out(), index = df.columns)
df_vectors.to_csv('sourc/df_vector_ju.csv', index = False)

comments_df = pd.DataFrame({'comments': comments_data})
comments_df.to_csv('sourc/comments_data_ju.csv', index=False)
