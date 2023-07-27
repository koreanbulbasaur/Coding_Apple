from papago import trans

import pandas as pd

data = pd.read_excel(r'part3\papago\english-1.xlsx', engine='openpyxl')

for i, row in data.iterrows():
    data.loc[i, 'korean'] = trans(row['english'])

print(data)

data.to_excel(r'part3\papago\output.xlsx')
data.to_csv(r'part3\papago\output.csv')