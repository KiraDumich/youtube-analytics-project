import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()


class Video:

    api_key: str = os.getenv('YI-API-KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        video_response = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                     id=video_id).execute()
        self.video_id = video_id
        self.url = f'https://youtu.be/{self.video_id}'
        self.video_title = video_response['items'][0]['snippet']['title']
        self.view_count = video_response['items'][0]['statistics']['viewCount']
        self.like_count = video_response['items'][0]['statistics']['likeCount']

    def __repr__(self):
        return f'{self.video_title}'

    def __str__(self):
        return self.video_title


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
