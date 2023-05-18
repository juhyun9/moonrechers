import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Okt
from nltk.corpus import stopwords
#nltk.download('stopwords')

df = pd.read_csv('sourc/crawling.csv',encoding='utf-8')
df = df.drop(['Unnamed: 0'],axis=1)
#df = df.style.hide(axis='index')
#youtubernum=len(df)
#df = df.set_index("youtuber")


clean_data1 =[]
for main in df['comments'].to_list():
    clean_main = re.sub('[^\w\d\s]', '', main)
    clean_data1.append(clean_main)

import konlpy
komoran = konlpy.tag.Komoran()
pos_data =[]

#이모지 제거
clean_data=[]
for text in clean_data1:
    emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
                            "]+", flags = re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    text = re.sub('[|A-Za-z|]+','', text)
    text = re.sub('[|0-9|]+','', text)
    text = re.sub("[^가-힣ㄱ-ㅎㅏ-ㅣ\\s]", "" ,text)    
    clean_data.append(text)

for clean_main in clean_data:
    try:
        pos_main = komoran.pos(clean_main)
    except: 
        continue
    pos_data.append(pos_main)

filter_data = []
for pos_main in pos_data:
    filter_main=[]
    for word, pos in pos_main:
        if pos == "NNP":
            filter_main.append(word)
        elif pos =='NNG':
            filter_main.append(word)
    filter_data.append(filter_main)

docu = []
for final_main in filter_data:
    docu.append(" ".join(final_main))

df['Aword'] = pd.Series(filter_data)
df['clean_com'] = pd.Series(docu)
df.info()
df.to_csv('sourc/comments_clean_data.csv', index=False)

#tfidf 추출
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

vecorizer = TfidfVectorizer()
docu_tfidf = vecorizer.fit_transform(np.array(docu))
docu_tfidf_matrix = pd.DataFrame(np.array(docu_tfidf.todense()), columns = vecorizer.get_feature_names_out(), index = df['youtuber'])
docu_tfidf_matrix.head(5)

docu_tfidf_matrix.to_csv('sourc/comments_vector_data.csv', index=False)
