from django.db import models

class Calls(models.Model):
    transcribed_text = models.TextField(u'Текст')
    synopsis_text = models.TextField(u'Краткое описание')
    caller_name = models.CharField(u'Имя', max_length=255)
    caller_number = models.CharField(u'Номер с', max_length=20)
    caller_adr = models.CharField(u'Номер', max_length=150)
    called_number = models.CharField(u'На номер', max_length=20)
    link_inp_aud = models.TextField(u'Ссылка аудио', max_length=255)
    link_out_text = models.TextField(u'Ссылка текст', max_length=255)
    date_of_call = models.DateTimeField(u'Дата звонка')
    date_of_transcribe = models.DateTimeField(u'Дата преобразования')
    call_lenght_s = models.IntegerField(u'Продолжительность', max_length=11)

    def __str__(self):
        return u'%i' % self.pk

    class Meta:
        db_table='transcribed_audio'
        #verbose_name='Вызовы'
        #verbose_name_plural='Вызовы'
