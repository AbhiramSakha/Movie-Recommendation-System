import pickle
import streamlit as st
import requests
import os
import gdown

# 🎥 Set Streamlit Page Config
st.set_page_config(page_title="Movie Recommender", layout="wide")

# 🎬 Fetch movie poster and IMDb link from OMDb API
OMDB_API_KEY = "f2134ec5"

def fetch_movie_details(movie_title):
    try:
        url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("Response") == "True":
            poster_url = data.get("Poster", "https://via.placeholder.com/150?text=No+Image")
            imdb_id = data.get("imdbID")
            imdb_url = f"https://www.imdb.com/title/{imdb_id}" if imdb_id else "#"
            return poster_url, imdb_url
        else:
            return "https://via.placeholder.com/150?text=No+Image", "#"

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error fetching movie details: {e}")
        return "https://via.placeholder.com/150?text=No+Image", "#"

# 🎬 Recommend movies based on similarity
def recommend(movie):
    try:
        st.write(f"✅ Selected Movie: {movie}")  # Debugging log

        if movie not in movies["title"].values:
            st.error("⚠️ Movie not found in dataset. Try another movie.")
            return [], []

        index = movies[movies["title"] == movie].index[0]
        distances = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)

        recommended_movie_names = []
        recommended_movie_posters = []
        recommended_movie_links = []

        for i in distances[1:6]:  # Get top 5 recommendations
            movie_title = movies.iloc[i[0]].title
            poster_url, imdb_url = fetch_movie_details(movie_title)
            
            recommended_movie_names.append(movie_title)
            recommended_movie_posters.append(poster_url)
            recommended_movie_links.append(imdb_url)

        return recommended_movie_names, recommended_movie_posters, recommended_movie_links
    except Exception as e:
        st.error(f"Error generating recommendations: {e}")
        return [], [], []

# 🎥 Title and description
st.title("🎥 Movie Recommender System")
st.markdown("<p style='font-size:18px;'>Find the best movies personalized just for you! 🍿</p>", unsafe_allow_html=True)

# 📦 Google Drive URLs for Pickle Files
movie_list_url = "https://drive.google.com/uc?id=1QRwSbKMMprtvmhDBitVKtX4XETKcULTz"
similarity_url = "https://drive.google.com/uc?id=1OuiCbt31Zv99y9lLPDkOK2rBjhT1YXks"

# 📝 File names
movie_list_file = "movie_list.pkl"
similarity_file = "similarity.pkl"

# ⬇️ Function to Download Pickle Files
def download_file(url, output):
    if not os.path.exists(output):
        with st.spinner(f"Downloading {output}... ⏳"):
            gdown.download(url, output, quiet=True)
    else:
        st.success(f"{output} already exists. ✅")

# 🔽 Download Pickle Files if Not Found
download_file(movie_list_url, movie_list_file)
download_file(similarity_url, similarity_file)

# 📂 Load Data
try:
    movies = pickle.load(open(movie_list_file, "rb"))
    similarity = pickle.load(open(similarity_file, "rb"))

    # ✅ Debugging: Check if data is loaded properly
    if "title" not in movies.columns or "movie_id" not in movies.columns:
        st.error("⚠️ Error: 'title' or 'movie_id' column missing in dataset. Check 'movie_list.pkl'.")
        st.stop()
    
    st.success("✅ Data Loaded Successfully!")
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# 🔽 Movie Selection
movie_list = movies["title"].values
selected_movie = st.selectbox("🔎 Select a Movie:", movie_list)

# 🎬 Show Recommendations
if st.button("🎥 Get Recommendations"):
    recommended_movie_names, recommended_movie_posters, recommended_movie_links = recommend(selected_movie)

    if recommended_movie_names:
        st.markdown("### 🍿 Recommended Movies for You:")
        cols = st.columns(5)  # Display in a single row with 5 columns
        for i, col in enumerate(cols):
            with col:
                st.image(recommended_movie_posters[i], width=150)
                st.markdown(f"[{recommended_movie_names[i]}]({recommended_movie_links[i]})", unsafe_allow_html=True)
    else:
        st.warning("⚠️ No recommendations found. Try another movie.")

# 📌 Footer / Watermark
st.markdown("""
<div style='text-align: center; font-size: 14px; padding-top: 20px;'>
    Made by <b>Team-06</b> | 
    <a href="https://github.com/AbhiramSakha" target="_blank">GitHub</a> |
    <a href="https://www.linkedin.com/in/sakha-abhiram-60b138289/" target="_blank">LinkedIn</a>
</div>
""", unsafe_allow_html=True)
