import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_coinglass_data():
    url = "https://www.coinglass.com/LiquidationData"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            script_tag = soup.find('script', id='__NEXT_DATA__')
            
            if script_tag:
                data = json.loads(script_tag.string)
                # Traverse the JSON to find liquidation data
                # Typically in props -> pageProps -> initialState or something similar
                print("Found __NEXT_DATA__")
                
                # Save to file for inspection
                with open("coinglass_next_data.json", "w") as f:
                    json.dump(data, f, indent=2)
                
                # Try to find specific keys
                # We are looking for "liquidation24h" or similar
                # Let's search recursively or just dump the structure
                
                # Check pageProps
                page_props = data.get('props', {}).get('pageProps', {})
                print(f"Page Props Keys: {page_props.keys()}")
                
                # Check if there is data directly
                if 'data' in page_props:
                    print("Found data in pageProps")
                    # print(json.dumps(page_props['data'], indent=2)[:500])
                
            else:
                print("Could not find __NEXT_DATA__ script tag")
        else:
            print(f"Failed to fetch page: {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scrape_coinglass_data()
