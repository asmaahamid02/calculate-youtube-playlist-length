from pytube import Playlist
from datetime import timedelta
import sys
from tqdm import tqdm
      
def get_playlist_info(playlist_url:str, days:int) -> tuple:
    # Initialize the playlist object

    playlist = Playlist(playlist_url)
  
    # count the number of videos in the playlist
    video_count = playlist.length

    # calculate the total duration of the playlist
    total_seconds = 0
    for video in tqdm(playlist.videos,desc="Calculating total duration",unit="video"):
        # get video length in seconds
        try:
            total_seconds += video.length
        except:
            print(f"Could not fetch video length for {video}")
            continue

    # convert total seconds to hours, minutes and seconds
    total_duration = str(timedelta(seconds=total_seconds))

    # calculate the estimated daily watch time
    estimated_daily_watch_time = round(total_seconds / days)
    estimated_daily_watch_time_str = str(timedelta(seconds=estimated_daily_watch_time))  

    # calculate the estimated daily watch videos
    estimated_daily_watch_videos = round(video_count / days)

    return video_count, total_duration, estimated_daily_watch_time_str, estimated_daily_watch_videos

if __name__ == "__main__":
    playlist_url = input("Enter the playlist URL: ")

    if not playlist_url:
            print("Please enter a valid playlist URL.")
            sys.exit(1)
    try:
        days = int(input("Enter the number of days to complete the playlist: "))  

        if days <= 0:
            raise ValueError("Number of days should be greater than 0.") 
    except ValueError as e:
        print(f"Invalid days input: {e}")
        sys.exit(1)

    try:
        video_count, total_duration, estimated_daily_watch_time, estimated_daily_watch_videos = get_playlist_info(playlist_url, days)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    print(f"Total number of videos in the playlist: {video_count}")
    print(f"Total duration of the playlist: {total_duration}")
    print(f"Estimated daily watch time: {estimated_daily_watch_time}")
    print(f"Estimated daily watch videos: {estimated_daily_watch_videos}")