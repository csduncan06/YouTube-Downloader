import requests
import shutil
import pytube
import time
import json
import os


def convert_resolution(resolution):
    resolution_map = {
        "low": 18,
        "medium": 22,
        "high": 137,
        "very high": 313
    }

    return resolution_map.get(resolution.lower(), 18)


def generate_video_url(video_id):
    url = 'https://www.youtube.com/watch?v=' + video_id
    return url

def store_recent_video(channel_name, video_title):
    data = {channel_name: video_title}
    file_path = 'RecentVids.json'

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                json_data = json.load(file)
            except json.decoder.JSONDecodeError:
                json_data = {}
    else:
        json_data = {}

    json_data.update(data)

    with open(file_path, 'w') as file:
        json.dump(json_data, file)

def download_video(resolution, url, directory):
    start = time.time()
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(resolution)

    stream.download()
    end = time.time()
    download_time = end - start
    
    channels_dir = "Uploads"
    
    if not os.path.exists(channels_dir):
        os.makedirs(channels_dir)
    
    source_path = stream.default_filename
    destination_path = os.path.join(channels_dir, directory, stream.default_filename)
    
    if not os.path.exists(os.path.join(channels_dir, directory)):
        os.makedirs(os.path.join(channels_dir, directory))

    shutil.move(source_path, destination_path)
    
    return stream.default_filename, download_time
