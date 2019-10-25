# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:40:27 2019

@author: Administrator
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

plt.style.use('fivethirtyeight')
sns.set_style({'font.sans-serif':['simhei','Arial']})

house_data = pd.read_csv('lianjia.csv')
pd.set_option('display.max_columns',1000)
pd.set_option('display.width',1000)  # 解决显示省略号的问题
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)   # 解决不能对齐的问题
# display(house_data.head(n=2))
# house_data.info()   数据的整体信息
# print(house_data.describe()) 数据的统计信息

# 删除无用信息id并对信息的分布进行调整
df = house_data.copy()
df['PerPrice'] = house_data['Price'] / house_data['Size']
columns = ['Region','District','Garden','Layout','Floor','Year','Size','Elevator','Direction','Renovation',\
           'PerPrice','Price']
df = pd.DataFrame(df,columns=columns)

df_house_count = df.groupby('Region')['Layout'].count().sort_values(ascending=False).to_frame().reset_index() 
'''各地区二手房的数量,通过对Region进行分组然后用其中一列数据的数量来代表房子的数量'''
df_house_mean = df.groupby('Region')['PerPrice'].mean().sort_values(ascending=False).to_frame().reset_index()
'''各地区二手房的每平米均价'''
'''
下面的是Region特征分析
f,[ax1,ax2,ax3] = plt.subplots(3,1,figsize=(20,15))
plt.subplots_adjust(hspace=0.5,top=0.8,bottom=0) 
上一行的方法用来调整子图间的纵向间距，wspace可以调整横向间距，另外四个参数是left，right，top，bottom
sns.barplot(x='Region',y='PerPrice',palette='Blues_d',data=df_house_mean,ax=ax1)
ax1.set_title('北京各地区二手房每平米单价对比',fontsize=15)
ax1.set_xlabel('地区')
ax1.set_ylabel('每平米单价(万元)')

sns.barplot(x='Region',y='Layout',palette='Greens_d',data=df_house_count,ax=ax2)
ax2.set_title('北京各地区二手房数量对比',fontsize=15)
ax2.set_xlabel('地区')
ax2.set_ylabel('数量')

sns.boxplot(x='Region',y='Price',data=df,ax=ax3)
ax3.set_title('北京各地区二手房房屋总价',fontsize=15)
ax3.set_xlabel('地区')
ax3.set_ylabel('房屋总价(万元)')
'''

'''下面的是Size特征分析
df = df[(df['Layout']!='叠拼别墅')&(df['Size']<1000)]  # 删除明显不符的数据
f,[ax1,ax2] = plt.subplots(1,2,figsize=(15,5))
sns.distplot(df['Size'],bins=20,color='r',ax=ax1)  # bins控制直方图的划分，20表示划分20个区间
sns.kdeplot(df['Size'],shade=False,ax=ax1)  #核密度估计图，shade则对曲线下方的区域进行阴影处理
sns.regplot(x='Size',y='Price',data=df,ax=ax2) # 散点图
'''

'''下面的是Layout特征分析
f,ax1 = plt.subplots(figsize=(20,20))
sns.countplot(y='Layout',data=df,ax=ax1)
ax1.set_title('房屋户型')
ax1.set_xlabel('数量')
ax1.set_ylabel('户型')
display(df.loc[df['Layout']=='11房间3卫'])
'''

'''下面的是Renovation特征分析
df = df[df['Renovation']!='南北']
print(df['Renovation'].value_counts())
f,[ax1,ax2] = plt.subplots(2,1,figsize=(15,5))
plt.subplots_adjust(top=2,bottom=0,hspace=0.5)
sns.barplot(x='Renovation',y='Price',data=df,ax=ax1)
sns.countplot('Renovation',data=df,ax=ax2)
'''
# display(len(df.loc[df['Elevator'].isnull()]))  有8237条数据的Elevator一项是Null
'''df[]和df.loc[]选取数据的区别:
    前者一次只能选取行或者列，即一次选取中，只能为行或者列设置筛选条件
    后者可以从多个维度（行和列）对数据进行筛选,方括号内必须有两个参数\
    第一个参数是对行的筛选条件，第二个参数是对列的筛选条件，两个参数用逗号隔开
'''
df['Elevator'] = df.loc[(df['Elevator']=='有电梯')|(df['Elevator']=='无电梯'),'Elevator'] # 去除错位的数据
df.loc[(df['Floor']>6) & (df['Elevator'].isnull()),'Elevator']=='有电梯'
df.loc[(df['Floor']<6) & (df['Elevator'].isnull()),'Elevator']=='无电梯'
display(df.head(n=2))    






