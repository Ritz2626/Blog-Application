# Generated by Django 4.0.6 on 2022-11-10 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
    ]