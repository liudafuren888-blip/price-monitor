import requests
import json
import time

def fetch_jin10_flash_news():
    url = "https://flash-api.jin10.com/get_flash_list"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "x-app-id": "bVBF4FyRTn5NJF5n",
        "x-version": "1.0.0",
        "Origin": "https://www.jin10.com",
        "Referer": "https://www.jin10.com/"
    }
    
    params = {
        "channel": 1, 
        "vip": "1",
        "t": int(time.time() * 1000)
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        
        if response.status_code == 200:
            json_data = response.json()
            if json_data.get("status") == 200:
                data = json_data.get("data", [])
                print(f"Got {len(data)} news items")
                if len(data) > 0:
                    print(json.dumps(data[0], indent=2, ensure_ascii=False))
                return data
            else:
                print(f"API Error: {json_data}")
        else:
            print(f"HTTP Error: {response.status_code}")
            
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    fetch_jin10_flash_news()
