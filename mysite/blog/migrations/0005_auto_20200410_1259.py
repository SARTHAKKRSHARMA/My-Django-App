# Generated by Django 2.2 on 2020-04-10 07:29

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20200410_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_detail',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 7, 29, 45, 848934, tzinfo=utc)),
        ),
        migrations.RemoveField(
            model_name='blog_detail',
            name='user_reaction',
        ),
        migrations.AddField(
            model_name='blog_detail',
            name='user_reaction',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
