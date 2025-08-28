🌐 AI-Powered Community Recommender

An AI-driven web application that recommends online communities (Reddit, Discord, Telegram) based on user preferences and interests. Users select a domain (e.g., music, games, movies, art), answer short domain-specific questions, and instantly receive personalized community recommendations.

🚀 Features

Preference-based input – Users pick a domain and answer simple questions.

AI keyword extraction – Uses Gemini AI to analyze user responses and generate meaningful keywords.

Community scraping & APIs – Fetches matching communities from:

🔺 Reddit

🎮 Discord (via Disboard.org scraper)

📲 Telegram groups/channels

Immediate recommendations – Results are shown instantly after submission on a results page.

Data logging – User inputs are stored for later analysis and improving recommendations.

🛠️ Tech Stack

Backend: Flask (Python)

AI/NLP: Gemini API for keyword extraction & classification

Scraping: Reddit API, Disboard scraper, Telegram parser

Frontend: HTML + Bootstrap (simple UI)

Storage: SQLite / CSV logging

📌 Workflow

User selects a domain of interest.

Answers short domain-specific questions.

Gemini generates keywords from the responses.

System scrapes & queries APIs to find matching communities.

Recommended communities with links are displayed on the results page.

🎯 Use Cases

Discover new communities based on hobbies/interests.

Personalized recommendations instead of manual searching.

AI-assisted community exploration across multiple platforms.
