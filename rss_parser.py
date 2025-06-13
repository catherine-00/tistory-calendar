# rss_parser.py

import feedparser
from collections import defaultdict
from datetime import datetime
import json

rss_url = "https://catherine-record.tistory.com/rss"

feed = feedparser.parse(rss_url)
post_counts = defaultdict(int)

for entry in feed.entries:
    published = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z')
    date_str = published.strftime('%Y-%m-%d')
    post_counts[date_str] += 1

# JSON 저장
with open("tistory_post_counts.json", "w", encoding="utf-8") as f:
    json.dump(post_counts, f, ensure_ascii=False, indent=2)
