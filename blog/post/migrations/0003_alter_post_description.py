# Generated by Django 4.0.6 on 2022-11-10 11:46

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
