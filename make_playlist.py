import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI")
))

def create_playlist(name, description="AI-generated playlist"):
    user_id = os.getenv("SPOTIFY_USER_ID")
    playlist = sp.user_playlist_create(user=user_id, name=name, public=True, description=description)
    print(f"Created playlist: {playlist['external_urls']['spotify']}")
    return playlist["id"]

if __name__ == "__main__":
    playlist_id = create_playlist("AI Test Playlist", "Playlist made by AI bot")
