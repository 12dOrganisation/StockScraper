import pandas as pd
from scraper import scraperFunction

url = "https://raw.githubusercontent.com/nmapx/revolut-stocks-list/master/list.csv"
df_stocks = pd.read_csv(url)
df_stocks.loc[-1] = [df_stocks.columns[0], df_stocks.columns[1]]  # adding a row
df_stocks.index = df_stocks.index + 1  # shifting index
df_stocks.sort_index(inplace=True)
df_stocks = df_stocks.rename(columns={'A': 'stock_index', 'Agilent Technologies': 'stock_name'})

df_scraped = pd.DataFrame(scraperFunction(1000))

ser = pd.Series(data=0, index=df_stocks.index)

for index, row in df_stocks.iterrows():
    for index1, row1 in df_scraped.iterrows():
        temp = row1['title'].split(" ")
        temp1 = row1['body'].split(" ")
        dollar_sign = "$"
        dollar_sign += row['stock_index']
        if (row['stock_index'] in (*temp, *temp1)) \
                or (row['stock_name'] in (*row1['title'], *row1['body']))\
                or (dollar_sign in (*temp, *temp1)):
            # print(row['stock_index'])
            # print(row1['title'])

            ser[index] = ser[index] + row1["comms_num"]
            # print(ser[index], index)

df_stocks["nr_comments"] = ser

to_export = df_stocks[df_stocks["nr_comments"]>0].sort_values("nr_comments", ascending=False)
exported = to_export.to_csv('hot_stocks.csv')
