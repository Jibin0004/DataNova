import streamlit as st
import pickle
import pandas as pd
import requests
import time
import re

st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")

#  Clean movie title to improve TMDb search match
def clean_title(title):
    title = re.sub(r'\(.*?\)', '', title)  # remove (2020), (Part II), etc.
    title = re.sub(r'[^a-zA-Z0-9 ]', '', title)  # remove special characters
    return title.strip()

#  Fetch movie poster using TMDb API
def fetch_poster_by_title(title):
    try:
        cleaned_title = clean_title(title)
        url = f"https://api.themoviedb.org/3/search/movie?api_key=8265bd1679663a7ea12ac168da84d2e8&query={cleaned_title}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        results = data.get("results", [])
        for result in results:
            poster_path = result.get("poster_path")
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path

        # No poster found
        return "https://via.placeholder.com/300x450.png?text=No+Poster"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for '{title}': {e}")
        return "https://via.placeholder.com/300x450.png?text=Error"

#  Recommend top 5 similar movies
def recommender(movie_title):
    movie_index = movie_df[movie_df["title"] == movie_title].index[0]
    distances = similarity[movie_index]
    similar_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_titles = []
    recommended_posters = []

    for i in similar_movies:
        title = movie_df.iloc[i[0]]["title"]
        recommended_titles.append(title)
        time.sleep(0.5)  # Prevent TMDb rate limiting
        poster_url = fetch_poster_by_title(title)
        recommended_posters.append(poster_url)

    return recommended_titles, recommended_posters

#  Load data
movie_dict = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movie_df = pd.DataFrame(movie_dict)
movie_titles = movie_df["title"].values

#  User input
selected_movie = st.selectbox("Search for a movie", movie_titles)

if st.button("Recommend"):
    names, posters = recommender(selected_movie)

    st.subheader("Top 5 Recommendations")
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
