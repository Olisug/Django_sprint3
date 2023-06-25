from django.db import models


class PublishedCreatedModel(models.Model):
    """Абстрактная модель. Добавляет флаг is_published и crated_at."""
    is_published = models.BooleanField('Опубликовано', default=True,
                                       help_text='Снимите галочку, чтобы '
                                                 'скрыть публикацию.')
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        abstract = True
