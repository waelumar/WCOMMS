import requests
from bs4 import BeautifulSoup

def search_disboard(keyword):
    url = f"https://disboard.org/en/search?keyword={keyword}"
    headers = {"User-Agent": "Mozilla/5.0"}
    results = []
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        for card in soup.select(".server-card")[:5]:
            name = card.select_one(".name").get_text(strip=True)
            link = "https://disboard.org" + card.select_one("a")["href"]
            desc = card.select_one(".description").get_text(strip=True)
            results.append({
                "platform": "Discord",
                "name": name,
                "url": link,
                "description": desc
            })
    except Exception as e:
        print("[Disboard ERROR]", e)
    return results
