import pandas as pd
from scraper import scaperFunction

url = "https://raw.githubusercontent.com/nmapx/revolut-stocks-list/master/list.csv"
df_stocks = pd.read_csv(url)

data = scaperFunction(5)
print(data)