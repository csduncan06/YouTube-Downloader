import GetRecentVideos
import requests
import Config
import Util
import json

# Config
api_key = Config.youtube_api_key
channels_to_monitor = Config.monitor_yt_ids
resolution = Config.download_resolution

# Constants
API_URL = 'https://www.googleapis.com/youtube/v3'

class YouTube:

    @staticmethod
    def get_channel_id(channel_search):
        params = {
            "part": "snippet",
            "type": "channel",
            "q": channel_search,
            "maxResults": 1,
            "key": Config.youtube_api_key
        }

        response = requests.get(API_URL + '/search', params=params)
        data = response.json()
        try:
            channel_id = data['items'][0]['id']['channelId']
        except: 
            print('API key likely dead')
            input()
        return channel_id

    @staticmethod
    def get_channel_name(channel_id):
        params = {
            "part": "snippet",
            "id": channel_id,
            "key": Config.youtube_api_key
        }

        response = requests.get(API_URL + '/channels', params=params)
        data = response.json()
        title = data['items'][0]['snippet']['title']
        return title

    @staticmethod
    def get_latest_videos(channel_id):
        params = {
            "part": "snippet",
            "channelId": channel_id,
            "maxResults": max_downloads,
            "order": "date",
            "key": Config.youtube_api_key
        }

        response = requests.get(API_URL + '/search', params=params)
        data = response.json()
        videos = []

        for item in data['items']:
            if item['id']['kind'] == 'youtube#video':
                vid_title = item['snippet']['title']
                vid_id = item['id']['videoId']
                videos.append((vid_title, vid_id))

        return videos



def main():
    resolution = Util.convert_resolution(Config.download_resolution)

    data = {}

    for display_channel_id in Config.monitor_yt_ids:
        backend_channel_id = YouTube.get_channel_id(display_channel_id)
        channel_display_name = YouTube.get_channel_name(backend_channel_id)
        recent_videos = YouTube.get_latest_videos(backend_channel_id)

        print(f'\nActive Channel: {channel_display_name}')

        for video_title, video_id in recent_videos:
            try:
                print(f'\t[~] Downloading... {video_title}')
                url = Util.generate_video_url(video_id)
                video_info = Util.download_video(resolution, url, channel_display_name)
                filename = video_info[0]
                download_speed = video_info[1]
                print(f'\t[!] Filename: {filename}')
                print(f'\t[!] Download time: {download_speed}\n')

                if channel_display_name not in data:
                    data[channel_display_name] = []

                data[channel_display_name].append(video_title)
            except Exception as e:
                print(f'{e}')

    with open('DownloadList.json', 'a') as file:
        json.dump(data, file)





if __name__ == "__main__":
    max_downloads = Config.max_downloads

    main()
    GetRecentVideos.UpdateRecentUploads()

else: 
    max_downloads = 1


