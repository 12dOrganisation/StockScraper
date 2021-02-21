import pandas as pd
from scraper import scaperFunction

url = "https://raw.githubusercontent.com/nmapx/revolut-stocks-list/master/list.csv"
df_stocks = pd.read_csv(url)
df_stocks.loc[-1] = [df_stocks.columns[0], df_stocks.columns[1]]  # adding a row
df_stocks.index = df_stocks.index + 1  # shifting index
df_stocks.sort_index(inplace=True)
df_stocks = df_stocks.rename(columns={'A':'stock_index', 'Agilent Technologies': 'stock_name'})
print(df_stocks)