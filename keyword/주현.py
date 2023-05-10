"#%%"
import pandas as pd
df1= pd.read_csv("sourc/crawling.csv", sep=",", encoding='utf-8')

#konlpy 명사 추출
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from emoji import core
import re

#기호 제거
#기존 data 변수는 csv파일 내용 data 내부는 제목 title, 본문 main
cl_data=[]
#df1['comments'].tolist()
for main in df1['comments'].tolist():
    pattern = r'[^a-zA-Z가-힣]'
    main = re.sub(pattern=pattern, repl=' ', string=main)
    main = core.replace_emoji(main, replace=" ")
    main = main.split()
    cl_data.append(main)


## 불용어 제거
stop_words = ['00','01','02','03','04','05','06','07','08','09']
fi_data = []
for word in cl_data:
    if word in stop_words:
        while word in main:
            main.remove(word)
    if len(word) <= 1:
        while word in main:
            main.remove(word)
    fi_data.append(main)


# 분석 데이터
rep = []
for fi_main in fi_data:
    rep.append(" ".join(fi_main))

yor=pd.DataFrame()
#yor.insert(0,"word",fi_data,True)
yor = yor.assign(word = fi_data, 
               comment = rep)
'''yor['단어'] = fi_data
yor['본문'] = rep'''

## 데이터 벡터화 df idf
vecorizer = CountVectorizer()
yor_tfidf = vecorizer.fit_transform(np.array(yor))
yor_tfidf_matrix = pd.DataFrame(np.array(yor_tfidf.todense()), columns = vecorizer.ger_feature_names(), index = data['제목'])   ## 크롤링 한 data변수의 제목
yor_tfidf_matrix
