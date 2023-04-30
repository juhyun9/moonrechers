#konlpy 명사 추출
import pandas as pd
df1 = pd.read_cvs('C:/Users/xlawk/OneDrive/바탕 화면/제주대/논문/result.csv')
from konlpy.tag import Mecab
tagger = Mecab()


## 불용어 제거
stop_words = "불용어 목록"
stop_words = stop.words.split(' ')

nouns = []
for reple in reple:
    for noun in tagger.nouns(reple):
        if noun not in stop_words:
            nouns.append(noun)
nouns[]
