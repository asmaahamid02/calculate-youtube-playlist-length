from pytube import Playlist
from datetime import timedelta
import sys
import itertools
import time
from threading import Thread

def spinner(msg:str, delay:float = 0.1):
    spinner_cycle = itertools.cycle(['-', '/', '|', '\\'])
    while True:
        sys.stdout.write(f'\r{msg} {next(spinner_cycle)}')
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write("\r")
        
def get_playlist_info(playlist_url:str, days:int) -> tuple:
    # Initialize the playlist object

    playlist = Playlist(playlist_url)
  
    # count the number of videos in the playlist
    video_count = playlist.length

    # calculate the total duration of the playlist
    total_seconds = 0
    for index, video in enumerate(playlist.videos):
        # get video length in seconds
        print(index)
        if video.length is None:
            continue
        total_seconds += video.length

    # convert total seconds to hours, minutes and seconds
    total_duration = str(timedelta(seconds=total_seconds))

    # calculate the estimated daily watch time
    estimated_daily_watch_time = round(total_seconds / days)
    estimated_daily_watch_time_str = str(timedelta(seconds=estimated_daily_watch_time))  

    # calculate the estimated daily watch videos
    estimated_daily_watch_videos = round(video_count / days)

    return video_count, total_duration, estimated_daily_watch_time_str, estimated_daily_watch_videos

def run_with_spinner(playlist_url:str, days:int) -> tuple:
    spinner_thread = Thread(target=spinner, args=("Fetching playlist information",), daemon=True)
    spinner_thread.start()

    result = get_playlist_info(playlist_url, days)
    
    sys.stdout.write("\n")
    sys.stdout.flush()

    return result

if __name__ == "__main__":
    playlist_url = input("Enter the playlist URL: ").strip()

    if not playlist_url:
            print("Please enter a valid playlist URL.")
            sys.exit(1)
    try:
        days = int(input("Enter the number of days to complete the playlist: "))    
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        sys.exit(1)

    try:
        video_count, total_duration, estimated_daily_watch_time, estimated_daily_watch_videos = run_with_spinner(playlist_url, days)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    print(f"Total number of videos in the playlist: {video_count}")
    print(f"Total duration of the playlist: {total_duration}")
    print(f"Estimated daily watch time: {estimated_daily_watch_time}")
    print(f"Estimated daily watch videos: {estimated_daily_watch_videos}")