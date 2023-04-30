import pandas as pd

df1 = pd.read_excel('claims-2002-2006_0.xls')
df2 = pd.read_excel('claims-2007-2009_0.xls')
df3 = pd.read_excel('claims-2010-2013_0.xls')
df4 = pd.read_excel('claims-2014.xls')

df = pd.concat([df1, df2, df3, df4])


df = df.reset_index(drop=True)

df.to_excel('combined_dataset.xls', index=False)