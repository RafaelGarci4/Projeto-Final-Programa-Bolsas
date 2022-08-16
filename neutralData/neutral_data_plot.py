import pandas as pd
import matplotlib.pyplot as plt





dfr = pd.read_csv('tweetsEmotion.csv')

neutral_filt = dfr['Feeling'] == 'Neutral'

dfr = dfr[neutral_filt]



subString = 'http'

http_filt = dfr['tweet'].str.contains('http',na=False)

dfr = dfr[http_filt]


df_plot = pd.DataFrame(http_filt.value_counts())

#print(df_plot.keys)

#df_plot.to_csv('teste2.csv')
plt.pie( df_plot['tweet'], labels=['Contem', 'Nao contem'], autopct='%1.1f%%')
plt.show()

