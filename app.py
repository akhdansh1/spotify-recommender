# app.py
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv("SpotifyFeatures.csv")

# Pilih kolom fitur
feature_cols = ['danceability', 'energy', 'valence', 'tempo', 'loudness',
                'acousticness', 'instrumentalness', 'liveness', 'speechiness']

# Ambil subset
df_subset = df.sample(n=5000, random_state=42).reset_index(drop=True)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df_subset[feature_cols])
similarity_matrix = cosine_similarity(scaled_features)
track_refs = df_subset[['track_name', 'artist_name']].reset_index(drop=True)

# Fungsi rekomendasi
def recommend_similar_songs(track_name, artist_name, refs, similarity_matrix, top_n=5):
    match = refs[
        (refs['track_name'].str.lower() == track_name.lower()) &
        (refs['artist_name'].str.lower() == artist_name.lower())
    ]
    if match.empty:
        return None

    idx = match.index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    recommendations = refs.iloc[[i[0] for i in sim_scores]].copy()
    recommendations['similarity_score'] = [i[1] for i in sim_scores]
    return recommendations

# Streamlit UI
st.title("🎵 Sistem Rekomendasi Lagu - Spotify")

st.markdown("Masukkan judul dan artis lagu yang kamu suka:")

track_input = st.text_input("Judul Lagu", "Shape of You")
artist_input = st.text_input("Nama Artis", "Ed Sheeran")

genre_list = df_subset['genre'].dropna().unique()
selected_genre = st.selectbox("Filter Genre", genre_list)


if st.button("Rekomendasikan 🎶"):
    result = recommend_similar_songs(track_input, artist_input, track_refs, similarity_matrix)
    if result is None:
        st.error("Lagu tidak ditemukan dalam subset.")
    else:
        st.success("Lagu mirip ditemukan!")
        st.dataframe(result)
