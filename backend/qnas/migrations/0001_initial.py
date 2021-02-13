# Generated by Django 3.1.5 on 2021-02-13 15:45

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
            name='Ans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('assisted', models.BooleanField(default='False')),
                ('like_ans_num', models.PositiveIntegerField(default=0)),
                ('liked_ans', models.BooleanField(default='False')),
                ('written_time', models.DateTimeField(auto_now_add=True)),
                ('assist_ans_users', models.ManyToManyField(related_name='assist_anss', to=settings.AUTH_USER_MODEL)),
                ('like_ans_users', models.ManyToManyField(related_name='like_anss', to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ans_profile', to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Qna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('ref_tags', multiselectfield.db.fields.MultiSelectField(choices=[('Python3', 'Python3'), ('Django', 'Django'), ('Java', 'Java'), ('Spring', 'Spring'), ('HTML5', 'HTML5'), ('CSS3', 'CSS3'), ('JavaScript', 'JavaScript'), ('TypeScript', 'TypeScript'), ('Vue.js', 'Vue.js'), ('React', 'React'), ('Angular', 'Angular'), ('Node.js', 'Node.js'), ('Swift', 'Swift'), ('Ruby', 'Ruby'), ('Ruby on Rails', 'Ruby on Rails'), ('MySQL', 'MySQL'), ('MariaDB', 'MariaDB'), ('MongoDB', 'MongoDB'), ('Docker', 'Docker'), ('Kubernetes', 'Kubernetes'), ('Frontend', 'Frontend'), ('Backend', 'Backend'), ('DevOps', 'DevOps'), ('Artificial Intelligence', 'Artificial Intelligence'), ('BigData', 'BigData'), ('Blockchain', 'Blockchain'), ('Internet of Things', 'Internet of Things'), ('Augmented Reality', 'Augmented Reality'), ('Virtual Reality', 'Virtual Reality')], max_length=273)),
                ('like_num', models.PositiveIntegerField(default=0)),
                ('comment_num', models.PositiveIntegerField(default=0)),
                ('liked', models.BooleanField(default='False')),
                ('bookmark_num', models.PositiveIntegerField(default=0)),
                ('bookmarked', models.BooleanField(default='False')),
                ('solved', models.BooleanField(default='False')),
                ('viewed_num', models.PositiveIntegerField(default=0)),
                ('written_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('bookmark_users', models.ManyToManyField(related_name='bookmark_qnas', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(related_name='like_qnas', to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qna_profile', to='profiles.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qna_userinfo', to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Qnasmall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('written_time', models.DateTimeField(auto_now_add=True)),
                ('qna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qnas.qna')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Anssmall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('written_time', models.DateTimeField(auto_now_add=True)),
                ('ans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qnas.ans')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ans',
            name='qna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qnas.qna'),
        ),
        migrations.AddField(
            model_name='ans',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ans',
            name='user_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ans_userinfo', to='profiles.profile'),
        ),
    ]
