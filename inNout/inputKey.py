import pandas as pd
import numpy as np

dirname = 'sourc/youtuber_cluster_key.csv'
key_docs = pd.read_csv(dirname, encoding='utf-8')

inputKey=input().split()
outputCluster=key_docs[key_docs['keyword'].str.contains(inputKey)]