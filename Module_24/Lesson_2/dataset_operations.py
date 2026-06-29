import pandas as pd
import numpy as np

scores = pd.Series([80, 88, np.nan, 95, 50], index =["Sara", "Ali", "Ahmad", "Nimra", "Humza"])

# dataframe

stds = {
    'name' : ['Ali', 'Ahmad', 'Sara', 'Humza'],
    'age' : [16, 16, 17, 15],
    'grade' : [8, 8, 7, 5]
}

dataset = pd.read_csv('people-100.csv')
print(dataset.head(10))