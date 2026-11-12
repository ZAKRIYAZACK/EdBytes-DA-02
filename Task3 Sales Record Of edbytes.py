import pandas as pd
from numpy.ma.extras import row_stack

from script3 import avg
#Sales Dataset
data=pd.read_csv("sales Edbytes.csv")
print(data.head())
print('Dimentions :',data.ndim)
print(data.isnull().sum())  # NO Null Values
#No Column Has Missing Value.
data["Revenue"]=data["Quantity"]*data["UnitPrice"]
print('Each Product Total:\n',data["Revenue"])
print('Total Revenue :',sum(data["Revenue"]))
print("Average :",sum(data["Revenue"])/len(data["Revenue"]))
  # ihave skip the chart preparation i did'nt learn yet seaborn
print(data.groupby("Category")["Category"].count())
print(data.groupby("Category")["Revenue"].sum())
#Right now I don't, I didn't learn the visualization tool yet.
# But I can give the insight about overall view of product category.
# Basically the category have of three type of product we have, bags, books, pens.
# Bag represent three times orders are placed. And books represent three orders are placed.
# And pens represent two orders are placed. And also comparatively bags are generated high income of overall product category.
# The bag product is actually performing well for this month

#Sales_dirty Dataset;
data2=pd.read_csv("sales-dirty edbytes.csv")
print(data2.head())
print(data2.tail())
print('Dimentions :',data2.shape)
print(data2.isnull().sum())
print(data2.duplicated().sum()) # 8th row have dulicated
data2=data2.drop_duplicates()
print(data2)
data2=data2.dropna()
#here only have 9 record inlcuding duplicate i have droped all values are nan
print("Cleaned Data Set :")
print(data2)
print("After Cleaning Dimention :",data2.shape)
print('Null Values After Cleaning :',data2.isnull().sum())
#In this data set, I have verified that the data has totally nine records including duplicates.
# And I have calculated the each column-wise null values and and I have found out the null value of last record, that is last record.
# It produces all the rows and columns are null values. So I dropped that, dropped that particular row. And also here it has no duplicate records.
# The duplicate records have been removed on the basis of the same records repeating the again even every rows and columns: date, sale amount, value, quantity sold. Everything has been matched.
# So the same records already I have. So I deleted the duplicate record of last one. That is order ID S03


