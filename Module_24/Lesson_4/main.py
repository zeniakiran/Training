import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris #iris -> flower
import numpy as np


# iris_df = sb.load_dataset('iris')
# print(iris_df.head())

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(df.head(4))

# histogram - frequency of the values

sb.histplot(df['petal length (cm)'], kde = False)

#plt.show()

sb.kdeplot(df['petal length (cm)'])
#plt.show()

sb.jointplot(x='petal length (cm)', y='petal width (cm)', data=df)
plt.show()

data = pd.DataFrame({
    'Math' : [90, 65, 70],
    'Science' : [80, 67, 88]
}, index=['Ali', "Hamza", 'Hania'])

sb.heatmap(data, annot=True, cmap="coolwarm")
plt.show()
