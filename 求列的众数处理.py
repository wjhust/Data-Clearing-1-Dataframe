# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 09:55:50 2018

@author: admin
"""

import pandas as pd
import numpy as np
from scipy import stats
#f1 = open(r'C:\Users\admin\Desktop\test_data.csv')
df=pd.read_csv("C:/Users/admin/Desktop/test.csv",index_col=0)
#print(df)
#df.groupby('member_id').agg(lambda x:np.mean(pd.Series.mode(x))).reset_index()
#df = pd.DataFrame({'a':['A','A','A','A','B','B','B','B','B'],'b':[1,1,2,3,1,2,2,3,3],'c':['a','a','b','b','c','b','b','c','a']})
#print(df.groupby('a').agg(lambda x: np.mean(pd.Series.mode(x))).reset_index())
#print(df.groupby('member_id').agg(stats.mode(df['two_category_name'])))

df1=df.groupby('member_id').agg(lambda x: stats.mode(x)[0][0]).reset_index()
df1.to_csv('C:\\Users\\admin\\Desktop\\df3.csv',encoding='gb2312', index=False)
