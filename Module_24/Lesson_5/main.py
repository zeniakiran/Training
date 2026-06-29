import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv('titanic.csv')

print(titanic.head())

# 80 + 81 + 82 + 82 + 86 = sum them all / total values = 82
sb.barplot(x='Pclass', y='Fare', data=titanic)
plt.show()

sb.pointplot(x='Pclass', y='Fare', data=titanic)
plt.show()

sb.jointplot(x='Pclass',y='Fare',data=titanic)
plt.show()

sb.stripplot(x="Pclass", y="Fare", data=titanic)
plt.show()

sb.swarmplot(x="Pclass", y="Fare", data=titanic)
plt.show()

sb.countplot(x='Sex',data=titanic)
plt.show()


# data = {
#     'Class': ['A', 'A', 'A', 'B', 'B', 'B'],
#     'Marks': [80, 85, 90, 70, 75, 78]
# }

# sb.pointplot(x='Class', y='Marks', data=data)
# plt.show()



