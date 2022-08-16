
import pandas as pd
import matplotlib.pyplot as plt



dfr = pd.read_csv('tweetsEmotion.csv')

df_plot = pd.DataFrame(dfr['Feeling'].value_counts())


plt.pie(df_plot['Feeling'], labels=df_plot.index, autopct='%1.1f%%')

plt.show()
