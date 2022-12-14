# Generated by Django 4.0.6 on 2022-11-10 13:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_photo',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
