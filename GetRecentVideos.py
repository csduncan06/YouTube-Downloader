import json
import Main
import Config

data = {}

def UpdateRecentUploads(): 
    data = {}
    
    with open('RecentVids.json') as stored:
        stored_data = json.load(stored)

    for display_channel_id in Config.monitor_yt_ids:
        backend_channel_id = Main.YouTube.get_channel_id(display_channel_id)
        channel_display_name = Main.YouTube.get_channel_name(backend_channel_id)
        recent_videos = Main.YouTube.get_latest_videos(backend_channel_id)

        if recent_videos:
            video_title = recent_videos[0][0]  # Extract only the video title
            data[channel_display_name] = video_title

            if video_title in stored_data.values():
                pass
            else:
                Main.main()
                with open('RecentVids.json', 'w') as file:
                    json.dump(data, file)

    with open('RecentVids.json', 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    UpdateRecentUploads()
else: 
    pass
