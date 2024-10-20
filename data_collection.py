import pandas as pd
import yfinance as yf
import datetime as dt

# list of tickers of top 100 companies in SP500 by market cap
tickers = [
    "MSFT", "AAPL", "NVDA", "GOOG", "GOOGL", "AMZN", "META", "BRK-B", "LLY", "AVGO", 
    "TSLA", "JPM", "V", "WMT", "XOM", "MA", "PG", "UNH", "HD", "MRK", "CVX", 
    "ABBV", "KO", "PEP", "ORCL", "PFE", "COST", "TMO", "ADBE", "MCD", "CRM", 
    "NFLX", "ACN", "TXN", "NEE", "AMD", "ABT", "PM", "LIN", "UPS", "INTU", 
    "VZ", "QCOM", "HON", "MS", "GS", "AMT", "SBUX", "CAT", "LOW", "DE", 
    "MDLZ", "AMGN", "LMT", "BKNG", "DHR", "RTX", "SPGI", "BLK", "SCHW", "CI", 
    "SYK", "T", "ELV", "PLD", "TJX", "MMM", "MO", "GILD", "ADP", "ISRG", 
    "PNC", "ITW", "USB", "MRNA", "AXP", "FISV", "MU", "CB", "MDT", "MMC", 
    "SO", "ADI", "PGR", "C", "NKE", "ETN", "VRTX", "COP", "PANW", "CL", 
    "CHTR", "TGT", "DUK", "EQIX", "KMB", "ZTS", "SHW", "EOG", "REGN", "APD"
]

# get todays date
date_today = dt.datetime.today().date()

# Ask for user inputs
num_tickers = int(input(f"How many tickers would you like to download? (Max {len(tickers)}): "))
# start_date = input("Enter start date (YYYY-MM-DD): ")
# end_date = input("Enter end date (YYYY-MM-DD): ")

# Ensure valid number of tickers
if num_tickers > len(tickers):
    print(f"Max allowed tickers is {len(tickers)}. Setting number of tickers to {len(tickers)}.")
    num_tickers = len(tickers)

print("Downloading data...")
# Download historical data for all tickers since January 1, 2000
data = yf.download(tickers[:num_tickers], start="2005-01-01", end=date_today, group_by="ticker")

# leave only the closing price of each ticker
close_prices = pd.DataFrame()

for ticker in tickers[:10]:
    close_prices[ticker] = data[ticker]["Close"]

close_prices=close_prices.reset_index()
close_prices.dropna(inplace=True)

close_prices.to_csv("stock_prices.csv", index=False)