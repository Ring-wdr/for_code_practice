#작업형 1

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('data/mtcars.csv', index_col = 0)

sc = MinMaxScaler()
sc.fit(df)
scaled_df = sc.transform(df)

print(sum(scaled_df[:,6] > 0.5))