import pandas as pd

url = "https://raw.githubusercontent.com/nmapx/revolut-stocks-list/master/list.csv"
df_stocks = pd.read_csv(url)
