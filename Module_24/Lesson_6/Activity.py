import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("penguins.csv")

print(df.head(10)) # FIRST 10 ROWS
print(df.shape) # rows and columns
print(df.tail()) # last rows
print(df.isnull().sum()) # count of null columns -> body mass = 3, flipper_length : 10
print(df.dtypes) 
print(df.info())
print(df.describe()) # numerical
print(df.describe(include='all')) # categorical
# print(df.corr())

# sns.heatmap(df.corr(), cmap= 'Wistia', annot=True)

df.hist(figsize=(12,8)) # 12 rows and 8 columns
plt.show()

df.plot(kind= 'box', subplots=True, layout=(3,2), figsize=(8,12))
plt.show()

print("COUNT", df.sex.value_counts())

# df.island.value_counts()

# df.species.value_counts()

sns.countplot(data=df, x='sex')
plt.show()

sns.countplot(data=df, x='island')
plt.show()

sns.countplot(data=df, x='species')
plt.show()

sns.countplot(data= df, x='sex', palette='rocket', hue='species')
plt.show()

sns.countplot(data= df, x= 'island', hue='species', palette='husl')
plt.show()

sns.countplot(data= df, x= 'island', hue='sex', palette='spring')
plt.show()

sns.pairplot(data=df, hue='species',palette='mako')
plt.show()