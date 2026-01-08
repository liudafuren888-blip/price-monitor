import requests
import json

url = "https://api-mainnet.magiceden.dev/v3/rtp/polygon/collections/v5?slug=liberty-cats"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}
try:
    r = requests.get(url, headers=headers, timeout=10)
    if r.status_code == 200:
        data = r.json()
        print(json.dumps(data, indent=2))
    else:
        print(f"Error: {r.status_code}")
except Exception as e:
    print(f"Exception: {e}")
