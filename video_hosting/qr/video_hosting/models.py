from django.core.validators import FileExtensionValidator
from django.db import models


class Video(models.Model):
    title = models.CharField('Название', max_length=100)
    anons = models.TextField('Анонс статьи')
    image = models.ImageField('Фотография', upload_to='image/')
    file = models.FileField('Видео',
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    create_at = models.DateTimeField('Дата', auto_now_add=True)
    is_published = models. BooleanField('Публикация', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'