# Generated by Django 3.1.5 on 2021-02-14 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qnas', '0005_auto_20210214_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagefile',
            old_name='post_file',
            new_name='img_file',
        ),
        migrations.RenameField(
            model_name='imagefile',
            old_name='file_url',
            new_name='img_url',
        ),
    ]
