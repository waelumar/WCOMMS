import requests
from bs4 import BeautifulSoup

def search_telegram(keyword):
    url = f"https://tdirectory.me/search?query={keyword}"
    headers = {"User-Agent": "Mozilla/5.0"}
    results = []
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        for item in soup.select(".channel")[:5]:
            name = item.select_one(".title").get_text(strip=True)
            link = item.select_one("a")["href"]
            desc = item.select_one(".description").get_text(strip=True)
            results.append({
                "platform": "Telegram",
                "name": name,
                "url": link,
                "description": desc
            })
    except Exception as e:
        print("[Telegram ERROR]", e)
    return results
