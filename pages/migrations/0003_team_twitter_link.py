# Generated by Django 3.0.7 on 2022-11-29 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20221129_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='twitter_link',
            field=models.URLField(default='1', max_length=100),
            preserve_default=False,
        ),
    ]
