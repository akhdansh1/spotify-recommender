# 🎵 Spotify Song Recommender

A simple **music recommendation system** built using **cosine similarity** on Spotify audio features. The app is deployed on **Streamlit Cloud** and allows users to get similar song suggestions based on a selected track and artist.

## 🌐 Live App

👉 Try the app here (https://spotify-recommender-p3fcmwg9vqs38b4iidprgq.streamlit.app/)

## 🧠 How It Works

This recommender system uses Spotify's audio features (e.g., danceability, energy, valence) and compares them using **cosine similarity** to find similar songs.

### Features used for similarity:
- `danceability`
- `energy`
- `valence`
- `tempo`
- `loudness`
- `acousticness`
- `instrumentalness`
- `liveness`
- `speechiness`

The system takes a random subset of 5000 songs to ensure fast processing and minimal memory usage.

## 📁 Dataset

We use the **[Spotify Songs Dataset](https://www.kaggle.com/datasets/leonardopena/spotify-2023) from Kaggle** with audio features of thousands of tracks.

Upload `SpotifyFeatures.csv` to your project directory.

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/akhdansh1/spotify-recommender.git
cd spotify-recommender

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py

## 📦 Dependencies

pandas
scikit-learn
streamlit

## Install with:

pip install pandas scikit-learn streamlit

## 🚀 Deployment (Streamlit Cloud)
Push your code to GitHub

Go to streamlit.io/cloud

Connect to your GitHub repo

Set main file path to app.py

Add secrets (optional, if using Spotify API)

Deploy!
