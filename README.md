# YouTube Playlist's Length Calculator Based on Days

This is a simple Python script that calculates the length of a YouTube playlist based on the number of days you want to watch it.
There are two modes for displaying the loading status: `tqdm` and `itertools with threading`.

## Author

> [Asmaa Hamid](https://linktr.ee/asmaahamid02)

## Technologies

- Python 3
- pytube (for retrieving playlist information)
- tdqm (for progress bar)

## Pre-requisites

- Python 3
- pip

## How to use

1. Install the required libraries:

   ```bash
   pip -r requirements.txt
   ```

2. Run the script:

   ```bash
   python script.py
   # or
   python script_with_spinner.py
   ```

3. Enter the URL of the YouTube playlist and the number of days you want to watch it.

4. Enter the number of days you want to watch the playlist.

5. The script will calculate the total length of the playlist and the number of videos you need to watch per day.
