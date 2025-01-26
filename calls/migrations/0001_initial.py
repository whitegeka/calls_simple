# Generated by Django 5.1.5 on 2025-01-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('duration', models.CharField(max_length=255, verbose_name='Продолжительность')),
                ('text', models.TextField(verbose_name='Текст')),
                ('link_audio', models.CharField(max_length=255, verbose_name='Ссылка аудио')),
                ('link_text', models.CharField(max_length=255, verbose_name='Ссылка текст')),
                ('date_created', models.DateTimeField(verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Вызовы',
                'verbose_name_plural': 'Вызовы',
                'db_table': 'calls_calls',
            },
        ),
    ]
