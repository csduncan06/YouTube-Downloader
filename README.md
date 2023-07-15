# 📽️ YouTube-Downloader

Automated YouTube video downloader for specified YouTubers + support for automatic download of new uploads
![Screenshot](https://media.discordapp.net/attachments/780911810311618591/1129580378475212930/image.png?width=918&height=499)


# Usage
To run the AutoDownloader.<br>
`$ python main.py` <br>
This will download all videos currently posted on channels in the config.<br>

To automatically download newly uploaded videos<br>
`$ python GetRecentVideos.py`<br>
It is recommended to have this script run automatically after a set period of time. This can be achieved with [TaskScheduler.](https://www.jcchouinard.com/python-automation-using-task-scheduler/)

## Installation

You can install by cloning the Git repository :

    $ git clone https://github.com/csduncan06/YouTube-Downloader


*__Note:__ **[Python](http://www.python.org/download/)** (**3.x**) is required for running.*

## Config 
<i>Found in Config.py</i>

```py
youtube_api_key = 'YouTube Data API v3 key'
monitor_yt_ids = ['@Youtube', 'SpaceX']
max_downloads = 5
download_resolution = 'medium' # very high, high, medium, low

```
You can obtain a YouTube Data API v3 key from [Google Cloud.](https://console.cloud.google.com/)<br>
Create a new project, enable use of YouTube Data API v3 and get your API key.

## Note
It is possible your API key will die. Google has "fairly" strict quotas on their API's so you may need to frequently change it or apply for more usage.
