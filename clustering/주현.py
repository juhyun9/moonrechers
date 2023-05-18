import matplotlib as plt
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import CountVectorizer
import re

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

clu_n=20

analyser = AgglomerativeClustering(linkage= method, n_clusters=clu_n)
cluster_id = pd.DataFrame(analyser.fit_predict(dfvector), columns = ['group_id'])
cluster_data = pd.concat((cluster_id,comdata), axis = 1).sort_values('group_id')
cluster_data.info()

##각 클러스터에서 주제 찾기
key_data = []
group=[]
youtu=[]
for i in range(clu_n):
    cluster_id_data = cluster_data.groupby('group_id').get_group(i)
    vectorizer = CountVectorizer(min_df = 1)
    clu_df = vectorizer.fit_transform(np.array(cluster_id_data['comments'].to_list()))
    vectorizer.fit_transform(np.array(cluster_id_data['comments'].to_list()))
    clu_df_matrix = pd.DataFrame(np.array(clu_df.todense()), columns=vectorizer.vocabulary_.keys())

    group.append(i)
    youtu.append(cluster_id_data['youtuber'])
    key=clu_df_matrix.std().sort_values(ascending=False).index
    key=re.sub('0-9+','', str(key))
    key=key.strip('Index(')
    #key=key.strip(",\n      dtype='object', length=69043") 왜 안됨?
    key=key.strip(")")
    key_data.append(key)

youtuber_cluster_key=pd.DataFrame({'group_id':group, 'youtuber':youtu,'keyword':key_data})
key.strip("\n      dtype='object', length=")
youtuber_cluster_key.to_csv('sourc/youtuber_cluster_key.csv', index=False)
