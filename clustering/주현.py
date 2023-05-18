import matplotlib as plt
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import CountVectorizer


dirname = 'sourc/comments_vector_data.csv'
dfvector = pd.read_csv(dirname, encoding='utf-8')

dirname2 = 'sourc/comments_clean_data.csv'
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

#20230518, 유튜버 52개에 대한 군집 개수 ==20개

analyser = AgglomerativeClustering(linkage= method, n_clusters=20)
cluster_id = pd.DataFrame(analyser.fit_predict(dfvector), columns = ['group_id'])
cluster_data = pd.concat((cluster_id,comdata), axis = 1).sort_values('group_id')
cluster_data.info()

##각 클러스터에서 주제 찾기

cluster_id_4_data = cluster_data.groupby('group_id').get_group(0)
vectorizer = CountVectorizer(min_df = 1)
clu_df = vectorizer.fit_transform(np.array(cluster_id_4_data['comments'].to_list()))
vectorizer.fit_transform(np.array(cluster_id_4_data['comments'].to_list()))
clu_df_matrix = pd.DataFrame(np.array(clu_df.todense()), columns=vectorizer.vocabulary_.keys())

print(clu_df_matrix.std().sort_values(ascending=False).head(5).index)
print(cluster_id_4_data['youtuber'].values) # 항목 입력하면 그거에 맞는 데이터가 나오는 듯 합니다 .comments ㅎ하면 다른 값 나와요!

#키워드 횟수로 주제 찾기
#실전에서는 이게 편할 듯 - 샘플 데이터를 통해 만든 프레임이 작기에 여기선 그렇게 큰 효용 x
## 수정중 ..

for name, comdata in cluster_data.groupby('group_id') :
    vectorizer = CountVectorizer(min_df = 1)
    clu_tf = vectorizer.fit_transform(np.array(comdata['comments'].to_list()))
    clu_tf_matrix = pd.DataFrame(np.array(clu_tf.todense()), columns=vectorizer.get_feature_names_out())
    clu_topic = clu_df_matrix.std().sort_values(ascending=False).head(10).index.to_list()
    print(f"클러스터 id : {name} / 핵심키워드 : {clu_topic}")
    
