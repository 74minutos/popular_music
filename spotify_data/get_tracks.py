import spotipy
import argparse
import json
import pandas as pd
from typing import Dict, List, Any
from spotipy.oauth2 import SpotifyClientCredentials

def load_json(file_path: str) -> Dict:
    with open(file_path) as read_from_file:
        data = json.load(read_from_file)
        return data

def make_track(popularity:int, id:str, track_name:str, artist_name:str, artist_id: str, year:int) -> Dict:
    return {
        'popularity': popularity,
        'id': id,
        'track_name': track_name,
        'artist_name': artist_name,
        'artist_id': artist_id,
        'year': year
    }

def get_tracks(spotify_api:Any) -> List:
    tracks = []
    for year in range(1940, 2021):
        for i in range(0,1000, 50):
            track_results = spotify_api.search(q='year:{}'.format(year), type='track', limit=50, offset=i)
            for i, t in enumerate(track_results['tracks']['items']):
                track = make_track(
                    popularity =t['popularity'],
                    id = t['id'],
                    track_name = t['name'],
                    artist_name = t['artists'][0]['name'],
                    artist_id = t['artists'][0]['id'],
                    year = year)
                tracks.append(track)
    return tracks

def songs_with_audio_features(credentials_path: str) -> None:
    credentials = load_json(credentials_path)
    SP = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials(client_id=credentials['client_id'],
                                                                                client_secret=credentials['client_secret']), requests_timeout=20, retries=10)
    tracks = get_tracks(SP)
    df_with_songs = pd.DataFrame.from_records(tracks)

    genres = {}
    artists_id = set(df_with_songs['artist_id'])
    for artist in artists_id:
        artist_data = SP.artist(artist)
        genres[artist_data['name']] = artist_data['genres']
    df_with_songs['genre'] = df_with_songs['artist_name'].map(genres)
    df_with_songs['genre'] = df_with_songs['genre'].astype(str).str.replace("[", "").str.replace("]", "").str.replace("'", "")
    df_with_songs['genre'] = df_with_songs['genre'].str.split(',')
    df_with_songs = df_with_songs.explode('genre', ignore_index=True)

    df_with_songs.to_csv("popular_music.csv", sep=";", index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Create a file with all tracks."
    )

    parser.add_argument(
        "--credentials_path",
        required=True,
        type=str,
        help="path to credentials")

    args = parser.parse_args()

    songs_with_audio_features(args.credentials_path)
