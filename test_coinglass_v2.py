import requests
import json

def test_coinglass_endpoints():
    endpoints = [
        "https://fapi.coinglass.com/api/futures/home/statistics",
        "https://fapi.coinglass.com/api/futures/liquidation_chart?symbol=BTC&timeType=12", # 12 might be 1h or 1d
        "https://fapi.coinglass.com/api/futures/liquidation/info?symbol=BTC"
    ]
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://www.coinglass.com",
        "Referer": "https://www.coinglass.com/",
        "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }
    
    for url in endpoints:
        try:
            print(f"Testing {url}...")
            response = requests.get(url, headers=headers, timeout=5)
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"Response keys: {data.keys()}")
                if 'data' in data and data['data']:
                    print(f"Data found in {url}")
                    # Print first few chars of data
                    print(str(data['data'])[:200])
                else:
                    print("No 'data' field or empty")
            print("-" * 30)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_coinglass_endpoints()
