import google.generativeai as genai

genai.configure(api_key="#insert gemini api key")
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_keywords_and_categories(user_data):
    prompt = f"""
    User interests:
    Domain: {user_data.get('domain')}
    Genre: {user_data.get('genre', '')}
    Artist/Game/Director: {user_data.get('artist', user_data.get('director', user_data.get('game', '')))}
    Album/Style: {user_data.get('album', user_data.get('style', ''))}

    Give 5 keywords for searching communities.
    Also return 3 categories/tags that summarize this user's interests.
    Output as JSON.
    """

    response = model.generate_content(prompt)
    return response.text  
