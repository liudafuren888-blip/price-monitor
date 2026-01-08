import yfinance as yf
print("Downloading 600519.SS...")
data = yf.download("600519.SS", period="1mo", progress=False)
print("Data shape:", data.shape)
print(data.head())
