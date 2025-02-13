SpotiSync: No Limits

OVERVIEW
SpotiSync is a Python-based tool that allows users to fetch tracks from a Spotify playlist and download them as MP3 files using YouTube audio sources. 
The program automates fetching Spotify playlist details, searching for corresponding YouTube videos, and converting them into high-quality MP3 files.

FEAUTRES
1. Fetches tracks from any public Spotify playlist.
2. Retrieves YouTube links for each track.
3. Downloads and converts tracks to MP3 format.
4. Saves tracks in a folder named after the playlist.

PRE REQUISITES 
Ensure you have the following installed:

1. Python 3.x
2. requests module
3. yt-dlp
4. ffmpeg (for audio conversion)


INSTALLATION
Clone the repository:

git clone https://github.com/yourusername/SpotiSync.git
cd SpotiSync

DEPENDENCIES
pip install requests yt-dlp

Install ffmpeg (if not installed):

1. Windows: Download from FFmpeg official site and add it to system PATH.
2. Mac: Install via Homebrew:
3. brew install ffmpeg
4. Linux: sudo apt install ffmpeg


USAGE
Run the script:

python spotisync.py

Enter the Spotify playlist ID when prompted. Playlist ID can be extracted from a playlist link (Share Link)
The program will fetch track details, retrieve YouTube links, and download them as MP3 files into a folder named after the playlist.


CONFIGURATION
Replace CLIENT_ID and CLIENT_SECRET in the script with your Spotify API credentials.
Modify yt_dlp search queries for better results if needed.

Disclaimer
This tool is for personal use only. Ensure compliance with Spotify and YouTube’s terms of service when using this software.

License
This project is licensed under the MIT License.

Contributing
Pull requests and suggestions are welcome! Feel free to improve functionality or optimize the script.
