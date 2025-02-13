import requests
import yt_dlp
import time 

#Spotify Creds
CLIENT_ID = "Your Client ID"
CLIENT_SECRET = "Your Client Secret"


#Fetching Access Token
auth_url = "https://accounts.spotify.com/api/token"
auth_response = requests.post(auth_url, {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
})

access_token = auth_response.json()["access_token"]

#Fetching Playlist Details 
def GetTracks(playlist_id):
    track_names = []
    headers = {"Authorization": f"Bearer {access_token}"}
    playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    
    #Playlist Data
    playlist_response = requests.get(playlist_url, headers=headers)
    playlist_data = playlist_response.json()

    playlist_name = playlist_data.get("name", "Unknown Playlist")

    # Fetching Tracks with 100>songs Consideration
    tracks_url = playlist_data["tracks"]["href"]
    while tracks_url:
        response = requests.get(tracks_url, headers=headers)
        
        # Handle rate limits
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 5))
            time.sleep(retry_after)
            continue
        
        tracks_response = response.json()
        for item in tracks_response.get("items", []):
            track = item["track"]
            artist_names = ", ".join(artist["name"] for artist in track["artists"])
            track_names.append(f"{track['name']} by {artist_names}")
        
        # Get next page
        tracks_url = tracks_response.get("next")

    return playlist_name, track_names


#Fetch Track Links
def GetLinks(tracklist):
    links = {}
    
    for track in tracklist:
        query = f"{track} official audio"
        ydl_opts = {"quiet": True, "default_search": "ytsearch", "noplaylist": True}
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            search_results = ydl.extract_info(query, download=False)
            
            if "entries" in search_results and len(search_results["entries"]) > 0:
                video_url = search_results["entries"][0]["webpage_url"]
                links[track] = video_url
    return links


#Converting & Downloading MP3 Files
def DownloadMP3(playlist_name, links):
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{playlist_name}/%(title)s.%(ext)s',  # Saves in 'downloads' folder
    'quiet': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for track, url in links.items():
            print(f"Downloading {track}..")
            ydl.download([url])  

    print(f"Download Complete!")
        


playlist_id = input("Playlist ID: ")
playlist_name, tracks = GetTracks(playlist_id)
print(f"Playlist: {playlist_name}\nTracks: {len(tracks)}")
for track in tracks:
    print(track)
print("Fetching Links...")
links = GetLinks(tracks)
print(links)
print(f"Downloading {playlist_name} playlist...")
DownloadMP3(playlist_name, links)
