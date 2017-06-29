import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

web_stats= {'Day':[1,2,3,4,5,6],
            'visitors':[45,56,66,33,22,33],
            'Bounce_rate':[56,56,678,756,43,32]}

# df= pd.DataFrame(web_stats)

#print(df)
#print(df.head())
# print(df.tail())

# print(df.tail(2))

# df.set_index('Day', inplace=True)
# print(df.head())


# df.set_index('visitors', inplace= True)
# print(df.head())

# print(df['Bounce_rate'])



# df= pd.DataFrame(web_stats)

# print(df['Day'].tolist())

# print(np.array(df[['visitors','Day','Bounce_rate']]))



df= pd.read_csv('ZILL_Z77006_3B.csv')

print(df.head())
df.set_index('Date',inplace = True)
df.to_csv('newcsvfile.csv')
