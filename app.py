from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from recommender.gemini_helper import generate_keywords_and_categories
from recommender.reddit_api import search_reddit
from recommender.discord_scraper import search_disboard
from recommender.telegram_scraper import search_telegram

import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/domain',methods=['post'])
def domain():
        domain = request.form.get('domain')
        return redirect(url_for(domain))

@app.route('/music', methods=['GET', 'POST'])
def music():
    if request.method == 'POST':
        data = {
            'domain': "music",
            'title': request.form['genre'],
            'artist': request.form['artist'],
            'album': request.form['album']
        }
        return save_response(data)  # Shows result immediately
    return render_template('music.html')


@app.route('/movies', methods=['GET', 'POST'])
def movies():
    if request.method == 'POST':
        data = {
            'domain':"movies",
            'title': request.form['genre'],
            'director': request.form['director']
        }
        return save_response(data)
    return render_template('movies.html')

@app.route('/games', methods=['GET', 'POST'])
def games():
    if request.method == 'POST':
        data = {
            'domain':"games",
            'type': request.form['type'],
            'game': request.form['game']
        }
        return save_response(data)
    return render_template('games.html')

@app.route('/art', methods=['GET', 'POST'])
def art():
    if request.method == 'POST':
        data = {
            "domain": "art",
            "Art Type": request.form.get('type'),
            "Style": request.form.get('style')
        }
        return save_response(data)
    return render_template('art.html')


def save_response(data):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    folder = os.path.join(app.instance_path, 'responses')
    os.makedirs(folder, exist_ok=True)

    # Save user input
    filename = f"{data['domain']}_{timestamp}.txt"
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w') as f:
        for k, v in data.items():
            f.write(f"{k}: {v}\n")

    # Use Gemini to generate keywords
    result = generate_keywords_and_categories(data)
    try:
        parsed = json.loads(result)
        keywords = parsed['keywords']
    except:
        keywords = list(data.values())  # fallback

    # Scrape communities
    reddit = search_reddit(keywords)
    discord = []
    telegram = []
    for kw in keywords:
        discord += search_disboard(kw)
        telegram += search_telegram(kw)

    all_results = reddit + discord + telegram

    # Save result file
    result_file = os.path.join(folder, f"{data['domain']}_{timestamp}_communities.json")
    with open(result_file, 'w') as f:
        json.dump(all_results, f, indent=2)

    # Return results page
    return render_template("results.html", communities=all_results)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
app.run(debug=True)