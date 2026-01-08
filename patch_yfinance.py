import os

file_path = '/Users/liuqimeng/Library/Python/3.9/lib/python/site-packages/yfinance/calendars.py'

with open(file_path, 'r') as f:
    content = f.read()

# Add Union to imports
content = content.replace('from typing import Any, Optional', 'from typing import Any, Optional, Union')

# Replace specific type hints
content = content.replace('list[Any] | list["CalendarQuery"]', 'Union[list[Any], list["CalendarQuery"]]')
content = content.replace('str | datetime | date', 'Union[str, datetime, date]')
content = content.replace('str | datetime | date | int', 'Union[str, datetime, date, int]')

with open(file_path, 'w') as f:
    f.write(content)

print("Patched calendars.py")
with open(file_path, 'r') as f:
    content = f.read()

content = content.replace('Optional[Union[str, datetime, date] | int]', 'Optional[Union[str, datetime, date, int]]')

with open(file_path, 'w') as f:
    f.write(content)

print("Patched calendars.py again")
