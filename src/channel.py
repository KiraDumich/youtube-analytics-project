import json
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YI-API-KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        channel = Channel.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        custom_url = channel['items'][0]['snippet']['customUrl']
        self.url = f'https://www.youtube.com/{custom_url}'
        self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']

    def print_info(self) -> None:
        channel = Channel.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        dict_channel = json.dumps(channel, indent=2, ensure_ascii=False)
        print(dict_channel)

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Класс-метод, возвращающий объект для работы с YouTube API."""
        return Channel.youtube

    def to_json(self, file):
        """Метод, сохраняющий в файл значения атрибутов экземпляра `Channel`"""
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': f'{self.description}',
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
        }
        with open(file, 'a', encoding='utf-8') as file_in:
            json.dump(data, file_in, indent=2, ensure_ascii=False)
