from app import fetch_news
import json

news = fetch_news()
print(json.dumps(news, ensure_ascii=False, indent=2))
print(f"Total news items found: {len(news)}")
