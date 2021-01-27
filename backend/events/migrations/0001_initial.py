# Generated by Django 3.1.5 on 2021-01-27 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='%Y/%m/%d')),
                ('title', models.CharField(max_length=30)),
                ('sdata', models.DateField()),
                ('stime', models.TimeField()),
                ('edata', models.DateField()),
                ('etime', models.TimeField()),
                ('location', models.CharField(max_length=30)),
                ('like', models.PositiveIntegerField(default=0)),
                ('view', models.PositiveIntegerField(default=0)),
                ('cost', models.CharField(default='', max_length=30)),
                ('target', models.CharField(default='', max_length=30)),
                ('introduction', models.TextField(default='')),
                ('schedule', models.TextField(default='')),
                ('hostinfo', models.TextField(default='')),
                ('tag', models.CharField(default='', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
