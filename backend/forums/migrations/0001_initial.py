# Generated by Django 3.1.5 on 2021-02-14 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('ref_tags', multiselectfield.db.fields.MultiSelectField(choices=[('Python3', 'Python3'), ('Django', 'Django'), ('Java', 'Java'), ('Spring', 'Spring'), ('HTML5', 'HTML5'), ('CSS3', 'CSS3'), ('JavaScript', 'JavaScript'), ('TypeScript', 'TypeScript'), ('Vue.js', 'Vue.js'), ('React', 'React'), ('Angular', 'Angular'), ('Node.js', 'Node.js'), ('Swift', 'Swift'), ('Ruby', 'Ruby'), ('Ruby on Rails', 'Ruby on Rails'), ('MySQL', 'MySQL'), ('MariaDB', 'MariaDB'), ('MongoDB', 'MongoDB'), ('Docker', 'Docker'), ('Kubernetes', 'Kubernetes')], max_length=153)),
                ('like_num', models.PositiveIntegerField(default=0)),
                ('liked', models.BooleanField(default='False')),
                ('bookmark_num', models.PositiveIntegerField(default=0)),
                ('bookmarked', models.BooleanField(default='False')),
                ('viewed_num', models.PositiveIntegerField(default=0)),
                ('written_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('bookmark_users', models.ManyToManyField(related_name='bookmark_posts', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_userinfo', to='profiles.profile')),
                ('writer_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_profile', to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('assisted', models.BooleanField(default='False')),
                ('like_comment_num', models.PositiveIntegerField(default=0)),
                ('liked_comment', models.BooleanField(default='False')),
                ('written_time', models.DateTimeField(auto_now_add=True)),
                ('like_comment_users', models.ManyToManyField(related_name='like_comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.post')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_profile', to='profiles.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_userinfo', to='profiles.profile')),
            ],
        ),
    ]
