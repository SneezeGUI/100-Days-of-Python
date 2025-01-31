import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#Load environment variables from .env file
load_dotenv() #loads the environment variables from a `.env` file, if it exists

#Initialize Spotipy with Spotify OAuth manager
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",  #needed scope
        redirect_uri="http://localhost:4304/auth/spotify/callback", #Redirect URI where the access token is sent after authorization
        client_id=os.getenv('SPOTIPY_CLIENT_ID'), #Client ID from your Spotify App
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),  #Client Secret from your Spotify App
        show_dialog=True,
        cache_path='token.txt',   #Token caching to avoid unnecessary calls to the authorization server.
        username=os.getenv('USERNAME') #Spotify username of the account to be used
    )
)
user_id = sp.current_user()['id']  #get current user id

## Scrape Billboard 100 songs by requesting a specific date input from user and use this date to scrape data
date = input('Welcome to the Musical Time Machine!\nPlease input a Year (XXXX-XX-XX):') #User input for date of scraping
header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0" } #Header for the HTTP request
URL = f'https://www.billboard.com/charts/hot-100/{date}/' #Billboard URL with specific date to scrape
response = requests.get(url=URL, headers=header)  #Send a GET request
soup = BeautifulSoup(response.text, 'html.parser') ## Make soup object from response content
raw_song_data = soup.find_all(name='div', class_="o-chart-results-list-row-container") #Find all songs in the scraped data
song_names_spans = [entry.find(name='h3', id='title-of-a-story') for entry in raw_song_data] #Get song name spans from entries
song_names = [song.getText().strip() for song in song_names_spans] ##Strip special characters from the song names

#Loop through all songs and get their spotify URIs
song_uris = []  ##Empty list to store song uris
for song in song_names:
    result = sp.search(q=f'{song}', type='track') ##Search for song
    try:
        uri = result["tracks"]["items"][0]["uri"]  ##get the URI of first matching item
        song_uris.append(uri) #Add it to our list of URIs
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.") ##Print if song not found on spotify and continue with next song
#Ask user to create a playlist or not
create = input('Press Any Key to Create Playlist... (N to cancel)')
if create == 'N': #If user entered "N", don't create the playlist and exit program.
    exit(0)
else: ##Create private playlist in spotify account of used with song URIs
    playlist = sp.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public=False)
    sp.user_playlist_add_tracks(user=user_id ,playlist_id=playlist['id'], tracks=song_uris)
