import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

weather = pd.read_csv('weather dataset.csv')

print(weather.head())

print(weather.info())

sb.barplot(x="weather_type", y="temperature", data=weather)
plt.show()

sb.pointplot(x='weather_type', y='temperature', data=weather)
plt.show()


sb.jointplot(x='weather_type',y='temperature',data=weather)
plt.show()

sb.jointplot(x='humidity',y='temperature',data=weather, kind='hex')
plt.show()

sb.jointplot(x='humidity',y='temperature',data=weather, kind='kde')
plt.show()

sb.stripplot(x="weather_type", y="temperature", data=weather)
plt.show()

sb.swarmplot(x="weather_type", y="temperature", data=weather)
plt.show()

sb.countplot(x="weather_type", data=weather)
plt.show()







