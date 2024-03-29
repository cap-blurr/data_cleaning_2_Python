# -*- coding: utf-8 -*-
"""Moringa_Data_Science_Prep_W3_Independent_Project_2019_07_Wambugu_Gichuki_Python_Notebook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sFDyNyozETSYQv48ze_uoZ5F413QrL1D
"""

import pandas as pd

import numpy as np

ds1 = pd.read_csv('cells_geo.csv',sep=';',index_col=False)
df1 = pd.DataFrame(ds1)

ds2 = pd.read_csv('Telcom_dataset.csv')
df2 = pd.DataFrame(ds2)

ds3 = pd.read_csv('Telcom_dataset2.csv')
df3 = pd.DataFrame(ds3)

ds4 = pd.read_csv('Telcom_dataset3.csv')
df4 = pd.DataFrame(ds4)

df1.head(3)

df3.head(3)

df1.info()

df1.describe()

df1.shape

df2.info()

df2.describe()

df2.shape

df3.info()

df3.describe()

df3.shape

df4.info()

df4.describe()

df4.shape

df1.notnull()

df2.notnull()

df3.notnull()

df4.notnull()

"""# DATA CLEANING"""

df1.columns = ['Index','City','In service','In Abidjan','Geographical Area','Name of zone','Longitude','Latitude','Region','Area','CELL_ID','SITE_ID']

df1.head(1)

df2.columns = ['Product','Value','Datetime','CELL_ON_SITE','DW_A_NUMBER','DW_B_NUMBER','COUNTRY_A','COUNTRY_B','CELL_ID','SITE_ID']

df3.columns = ['Product','Value','Datetime','CELL_ON_SITE','DW_A_NUMBER','DW_B_NUMBER','COUNTRY_A','COUNTRY_B','CELL_ID','SITE_ID']

df4.columns = ['Product','Value','Datetime','CELL_ON_SITE','DW_A_NUMBER','DW_B_NUMBER','COUNTRY_A','COUNTRY_B','CELL_ID','SITE_ID']

df1 = df1.drop(['Index','In service','In Abidjan','Geographical Area','Name of zone','Latitude','Longitude','Region','Area','CELL_ID'],axis = 1)

df2 = df2.drop(['Value','CELL_ON_SITE','COUNTRY_A','DW_A_NUMBER','DW_B_NUMBER','COUNTRY_B','CELL_ID'], axis = 1)

df3 = df3.drop(['Value','CELL_ON_SITE','COUNTRY_A','DW_A_NUMBER','DW_B_NUMBER','COUNTRY_B','CELL_ID'],axis = 1)

df4 = df4.drop(['Value','CELL_ON_SITE','COUNTRY_A','DW_A_NUMBER','DW_B_NUMBER','COUNTRY_B','CELL_ID'],axis = 1)

df1.head()

df3.head()

df2.head()

new_datetime = df2['Datetime'].str.split(" ",n = 1,expand = True)
df2['Date'] = new_datetime[0]
df2['Time'] = new_datetime[1]
df2 = df2.drop('Datetime',axis = 1)

new_datetime2 = df3['Datetime'].str.split(" ",n = 1,expand = True)
df3['Date'] = new_datetime2[0]
df3['Time'] = new_datetime2[1]
df3 = df3.drop('Datetime',axis = 1)

new_datetime3 = df4['Datetime'].str.split(" ",n = 1,expand = True)
df4['Date'] = new_datetime3[0]
df4['Time'] = new_datetime3[1]
df4 = df4.drop('Datetime',axis = 1)

df2and3 = pd.merge(df2,df3,on = ['SITE_ID','Date','Product'],how='inner')
df2and3

df5 = pd.merge(df4,df2and3,on = 'SITE_ID',how = 'inner')
df5

df5 = df5.drop(['Product_x','Product_y','Date_y','Time_y','Date_x','Time_x'],axis = 1)
df5

df6 = pd.merge(df5,df1,on = 'SITE_ID',how = 'inner')
df6