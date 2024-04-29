from rest_framework.serializers import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        youtube_url = 'https://www.youtube.com/'
        data_url = dict(value).get(self.field)
        if youtube_url not in data_url:
            raise ValidationError('Сторонняя ссылка')
