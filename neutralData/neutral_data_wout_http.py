import pandas as pd
import matplotlib.pyplot as plt





dfr = pd.read_csv('tweetsEmotion.csv')



subString = 'http'

http_filt = ((dfr['tweet'].str.contains('http',na=False)) & (dfr['Feeling'] == 'Neutral'))

dfr = dfr[~http_filt]



df_plot = pd.DataFrame(dfr['Feeling'].value_counts())




plt.pie(df_plot['Feeling'],colors=['green','yellow','red'], labels=df_plot.index, autopct='%1.1f%%')

plt.title('Without Http in Neutral result')

plt.show()

