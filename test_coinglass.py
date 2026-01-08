import requests
import json

def test_coinglass_api():
    url = "https://fapi.coinglass.com/api/futures/home/statistics"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Origin": "https://www.coinglass.com",
        "Referer": "https://www.coinglass.com/"
    }
    
    try:
        print(f"Fetching from {url}...")
        response = requests.get(url, headers=headers, timeout=10)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            # Save raw data to inspect structure
            with open("coinglass_data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print("Data saved to coinglass_data.json")
            
            if data.get('success'):
                stats = data['data']
                print(f"24h Liquidation: {stats.get('liquidation24h')}")
                print(f"24h Rekt Users: {stats.get('liquidationBox', {}).get('num')}")
            else:
                print("API Success is False")
        else:
            print("Request failed")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_coinglass_api()
