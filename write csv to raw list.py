import pandas as pd

data = pd.read_csv('data.csv')

df = pd.DataFrame(data=data).T
df = df.to_csv('data_write.csv')
df



