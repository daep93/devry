# Generated by Django 3.1.5 on 2021-02-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210205_0223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followee_num',
        ),
        migrations.RemoveField(
            model_name='user',
            name='follower_num',
        ),
        migrations.AddField(
            model_name='userfollowing',
            name='followee_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userfollowing',
            name='follower_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
