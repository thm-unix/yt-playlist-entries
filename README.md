# yt-playlist-entries
Script for getting titles of all videos from YT playlist

## Attention
This project does not use YouTube API and just parses HTML page, therefore it might stop working at any time. If it no longer works, let me know about that via Issues.

## Guide
1. `git clone https://github.com/thm-unix/yt-playlist-entries`
2. `cd yt-playlist-entries`
3. `pip3 install -r requirements.txt`
4. `python3 main.py https://youtube.com/playlist?list=...`

At this point list of videos should be available at result.txt in the current directory.
