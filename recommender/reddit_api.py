import praw

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent=""
)

def search_reddit(keywords):
    return [{
        "platform": "Reddit",
        "name": f"Reddit: {kw}",
        "url": f"https://www.reddit.com/search/?q={kw.replace(' ', '+')}+community",
        "description": "Search results for community"
    } for kw in keywords]
