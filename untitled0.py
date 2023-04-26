# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:30:59 2023

@author: CPS
"""

#TD_IDF 통한 추천 알고리즘
import pandas as pd
pd.options.display.float_format = '{:.6f}'.format
import numpy as np
import os
import logging

# 로그 생성
logger = logging.getLogger()

# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

# log 출력 형식
formatter = logging.Formatter("%(message)s")

# Start defining and assigning your handlers here
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# visualization
import seaborn as sns
import matplotlib.pyplot as plt

merge = pd.read_csv('result.csv')
# 문자열 결측값 전처리
merge.replace('[]', np.nan, inplace=True)

# 결측값 비율이 높은 컬럼 (homepage, tagline) 제거
merge.drop([컬럼명, 컬럼명], axis=1, inplace=True)

