from django.db import models

class Calls(models.Model):
    name = models.CharField(u'Имя', max_length=255)
    phone = models.CharField(u'Телефон', max_length=255)
    duration = models.CharField(u'Продолжительность', max_length=255)
    text = models.TextField(u'Текст')
    link_audio = models.CharField(u'Ссылка аудио', max_length=255)
    link_text = models.CharField(u'Ссылка текст', max_length=255)
    date_created = models.DateTimeField(u'Дата создания')

    def __str__(self):
        return u'%s' % self.name

    class Meta:
        db_table='calls_calls'
        verbose_name='Вызовы'
        verbose_name_plural='Вызовы'
