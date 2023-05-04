import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import CountVectorizer


dirname = '/Users/bini/Desktop/Excel_Data/df_vector.csv'
dfvector = pd.read_csv(dirname, encoding='utf-8')

dirname2 = '/Users/bini/Desktop/Excel_Data/comments_data.csv'
comdata = pd.read_csv(dirname2, encoding='utf-8')

# 댄드로그램 만들기
method = 'ward'
Z = linkage(dfvector, 'ward')  # ward method를 사용한 linkage

plt.figure(figsize=(10, 5))
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Sample index")
plt.ylabel("Distance")
dendrogram(Z, leaf_rotation=90., leaf_font_size=8.)
plt.show()

'''
##요거는 챗지피티가 알려준 코드##
# 병합 군집 분석 객체 생성
agg_clustering = AgglomerativeClustering(n_clusters=3)

# 모델 학습
agg_clustering.fit(df)

# 결과 출력
print(agg_clustering.labels_)
'''

### 내가 생각하기에 적절하다고 생각되는 군집 개수로 클러스팅
analyser = AgglomerativeClustering(linkage= method, n_clusters=3)
cluster_id = pd.DataFrame(analyser.fit_predict(dfvector), columns = ['그룹 id'])
cluster_data = pd.concat((cluster_id,comdata), axis = 1).sort_values('그룹 id')
cluster_data

##각 클러스터에서 주제 찾기
cluster_id_1_data = cluster_data.groupby('그룹 id').get_group(0)
vectorizer = CountVectorizer(min_df = 1)
clu_df = vectorizer.fit_transform(np.array(cluster_id_1_data['comments'].to_list()))
vectorizer.fit_transform(np.array(cluster_id_1_data['comments'].to_list()))
clu_df_matrix = pd.DataFrame(np.array(clu_df.todense()), columns=vectorizer.vocabulary_.keys())

print(clu_df_matrix.std().sort_values(ascending=False).head(5).index)
print(cluster_id_1_data['그룹 id'].values) # 항목 입력하면 그거에 맞는 데이터가 나오는 듯 합니다 .comments ㅎ하면 다른 값 나와요!

#키워드 횟수로 주제 찾기
#실전에서는 이게 편할 듯 - 샘플 데이터를 통해 만든 프레임이 작기에 여기선 그렇게 큰 효용 x
## 수정중 ..
'''
for name, comdata in cluster_data.groupby('그룹 id') :
    vectorizer = CountVectorizer(min_df = 1)
    vectorizer.fit_transform(np.array(comdata['comments'].to_list()))
    clu_df_matrix = pd.DataFrame(np.array(clu_df.todense()), columns=vectorizer.vocabulary_.keys())
    clu_topic = clu_df_matrix.std().sort_values(ascending=False).head(10).index.to_list()
    print(f"클러스터 id : {name} / 핵심키워드 : {clu_topic}")

'''











