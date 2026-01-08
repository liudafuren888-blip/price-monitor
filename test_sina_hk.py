import requests
import json

# Try Sina HK Stock API again with different parameters or endpoint
# Sometimes referer is needed
headers = {
    "Referer": "https://finance.sina.com.cn/"
}
url = "http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/HK_Stock.getKLineData?symbol=hk03690&scale=240&ma=no&datalen=30"
print(f"Testing URL: {url}")
try:
    r = requests.get(url, headers=headers)
    print(f"Status: {r.status_code}")
    print(f"Content: {r.text[:200]}")
except Exception as e:
    print(f"Error: {e}")

# Try fetching via yfinance as fallback if Sina fails
import yfinance as yf
print("\nTesting yfinance for 3690.HK...")
try:
    data = yf.download("3690.HK", period="1mo", progress=False)
    print(data.head())
except Exception as e:
    print(f"yfinance error: {e}")
