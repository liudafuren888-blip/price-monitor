import requests
import re

url = "http://stock2.finance.sina.com.cn/futures/api/jsonp.php/var%20_GC=/GlobalFuturesService.getGlobalFuturesDailyKLine?symbol=GC"
r = requests.get(url)
content = r.text
print("Content length:", len(content))
print("Sample content:", content[:200])

start = content.find('([') + 1
end = content.rfind('])') + 1
if start > 0 and end > 0:
    json_str = content[start:end]
    print("JSON str sample:", json_str[:100])
    
    # Current Regex
    matches = re.findall(r'd:"(\d{4}-\d{2}-\d{2})".*?c:"([\d\.]+)"', json_str)
    print("Matches found:", len(matches))
    if matches:
        print("Last match:", matches[-1])
    else:
        # Check actual format if regex fails
        # It seems the keys might not be quoted in some responses or format is different
        pass
else:
    print("Could not find start/end")
