import pandas as pd
from scraper import scraperFunction

url = "https://raw.githubusercontent.com/nmapx/revolut-stocks-list/master/list.csv"
df_stocks = pd.read_csv(url)
df_stocks.loc[-1] = [df_stocks.columns[0], df_stocks.columns[1]]  # adding a row
df_stocks.index = df_stocks.index + 1  # shifting index
df_stocks.sort_index(inplace=True)
df_stocks = df_stocks.rename(columns={'A': 'stock_index', 'Agilent Technologies': 'stock_name'})

df_scraped = pd.DataFrame(scraperFunction(100))


for index, row in df_stocks.iterrows():
    for index1, row1 in df_scraped.iterrows():
        temp = " "
        temp = temp + row['stock_index']
        temp = temp + " "
        if temp in row1['title']:
            print(row['stock_index'])
            print(row1['title'])

df_stocks['comments'] = 0
df_stocks['comments'] = df_stocks[(df_stocks['comments'])]