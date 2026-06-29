import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

df = pd.read_csv('USA_Housing.csv')

df.head(10)

df.info() 

df.describe() 

df.columns

sb.pairplot(df)

plt.show()

numeric_df = df.select_dtypes(include='number')

corr = numeric_df.corr()
sb.heatmap(corr, cmap="coolwarm", annot=True)

plt.show()
