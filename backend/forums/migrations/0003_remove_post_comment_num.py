# Generated by Django 3.1.5 on 2021-02-12 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_auto_20210212_0728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_num',
        ),
    ]