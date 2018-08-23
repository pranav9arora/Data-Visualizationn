import numpy as np
import pandas as pd
from pandas import DataFrame
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#df = pd.read_csv('f2m_ratios.csv',engine='python',sep='/t')
#print(list(df))
df = pd.read_csv('prac.csv')
print(list(df))
#print(df.isnull())
#print(df.isnull().sum())
df = df.fillna(" ")
print(df.isnull().sum())
#df2 = df.pivot('Area,Year,Age,Ratio')
#print(df2.head())
#sns.heatmap(df,annot=True,fmt='d',linewidth=0.5).get_figure().savefig('heatmap.png')

