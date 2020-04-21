# Generated by Django 2.2 on 2020-04-12 11:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200412_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Blog_Detail'),
        ),
        migrations.AlterField(
            model_name='blog_detail',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 11, 14, 39, 479031, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='comments',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 12, 11, 14, 39, 482024, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='dislikes',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='comments',
            name='likes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]