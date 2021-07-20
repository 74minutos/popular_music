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

def make_track(release_date:str, id:str, album_name:str, artist_name:str, year:str) -> Dict:
    return {
        'release_date': release_date,
        'id': id,
        'album_name': album_name,
        'artist_name': artist_name,
        'year': year
    }

def get_albums(spotify_api:Any) -> List:
    tracks = []
    for i in range(0,1000, 50):
        for year in range(1940, 2021):
            track_results = spotify_api.search(q='year:{}'.format(year), type='album', limit=50, offset=i)
            for i, t in enumerate(track_results['albums']['items']):
                track = make_track(
                    release_date =t['release_date'],
                    id = t['id'],
                    album_name = t['name'],
                    artist_name = t['artists'][0]['name'],
                    year = year)
                tracks.append(track)
    return tracks

def songs_with_audio_features(credentials_path: str) -> None:
    credentials = load_json(credentials_path)
    SP = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials(client_id=credentials['client_id'],
                                                                                client_secret=credentials['client_secret']))
    tracks = get_albums(SP)
    df_with_songs = pd.DataFrame.from_records(tracks)

    genres = {}
    for track in tracks:
        first_call_genres = SP.search(q="artist:{}".format(track['artist_name']), type='artist')
        for genre in first_call_genres['artists']['items']:
            genres[genre['name']] = genre['genres']
    df_with_songs['genre'] = df_with_songs['artist_name'].map(genres)


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
