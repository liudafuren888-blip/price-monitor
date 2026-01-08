import yfinance as yf
from requests import Session
from requests_cache import CachedSession
from requests_ratelimiter import LimiterSession

session = CachedSession('yfinance.cache')
session.headers['User-agent'] = 'my-program/1.0'

print("Downloading 600519.SS with session...")
ticker = yf.Ticker("600519.SS", session=session)
data = ticker.history(period="1mo")
print("Data shape:", data.shape)
print(data.head())
