from sklearn.cluster import AgglomerativeClustering
import numpy as np

# 데이터 생성
X = np.array([[1,2], [1,4], [1,0],
              [4,2], [4,4], [4,0]])

# 병합 군집 분석 객체 생성
agg_clustering = AgglomerativeClustering(n_clusters=2)

# 모델 학습
agg_clustering.fit(X)

# 결과 출력
print(agg_clustering.labels_)
