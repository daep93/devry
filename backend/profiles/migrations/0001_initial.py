# Generated by Django 3.1.5 on 2021-02-05 01:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0005_auto_20210205_0730'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=80)),
                ('follower_num', models.PositiveIntegerField(default=0)),
                ('followee_num', models.PositiveIntegerField(default=0)),
                ('profile_img', imagekit.models.fields.ProcessedImageField(blank=True, default='', upload_to='accounts/images')),
                ('region', models.CharField(blank=True, choices=[('서울', '서울'), ('부산', '부산'), ('대구', '대구'), ('인천', '인천'), ('광주', '광주'), ('대전', '대전'), ('울산', '울산'), ('경기', '경기'), ('강원', '강원'), ('충북', '충북'), ('충남', '충남'), ('전북', '전북'), ('전남', '전남'), ('경북', '경북'), ('경남', '경남'), ('제주', '제주')], max_length=4)),
                ('group', models.CharField(blank=True, default='', max_length=40)),
                ('bio', models.TextField(blank=True, default='')),
                ('sns_name1', models.TextField(blank=True, default='')),
                ('sns_name2', models.TextField(blank=True, default='')),
                ('sns_name3', models.TextField(blank=True, default='')),
                ('sns_url1', models.URLField(blank=True, default='', max_length=100)),
                ('sns_url2', models.URLField(blank=True, default='', max_length=100)),
                ('sns_url3', models.URLField(blank=True, default='', max_length=100)),
                ('tech_stack', multiselectfield.db.fields.MultiSelectField(choices=[('Python3', 'Python3'), ('Django', 'Django'), ('Java', 'Java'), ('Spring', 'Spring'), ('HTML5', 'HTML5'), ('CSS3', 'CSS3'), ('JavaScript', 'JavaScript'), ('TypeScript', 'TypeScript'), ('Vue.js', 'Vue.js'), ('React', 'React'), ('Angular', 'Angular'), ('Node.js', 'Node.js'), ('Swift', 'Swift'), ('Ruby', 'Ruby'), ('Ruby on Rails', 'Ruby on Rails'), ('MySQL', 'MySQL'), ('MariaDB', 'MariaDB'), ('MongoDB', 'MongoDB'), ('Docker', 'Docker'), ('Kubernetes', 'Kubernetes')], max_length=153)),
                ('project_name1', models.CharField(blank=True, default='', max_length=100)),
                ('project_name2', models.CharField(blank=True, default='', max_length=100)),
                ('project_name3', models.CharField(blank=True, default='', max_length=100)),
                ('project_url1', models.URLField(blank=True, default='', max_length=100)),
                ('project_url2', models.URLField(blank=True, default='', max_length=100)),
                ('project_url3', models.URLField(blank=True, default='', max_length=100)),
                ('tag', multiselectfield.db.fields.MultiSelectField(choices=[('Python3', 'Python3'), ('Django', 'Django'), ('Java', 'Java'), ('Spring', 'Spring'), ('HTML5', 'HTML5'), ('CSS3', 'CSS3'), ('JavaScript', 'JavaScript'), ('TypeScript', 'TypeScript'), ('Vue.js', 'Vue.js'), ('React', 'React'), ('Angular', 'Angular'), ('Node.js', 'Node.js'), ('Swift', 'Swift'), ('Ruby', 'Ruby'), ('Ruby on Rails', 'Ruby on Rails'), ('MySQL', 'MySQL'), ('MariaDB', 'MariaDB'), ('MongoDB', 'MongoDB'), ('Docker', 'Docker'), ('Kubernetes', 'Kubernetes'), ('FrontEnd', 'FrontEnd'), ('BackEnd', 'BackEnd'), ('DevOps', 'DevOps'), ('Artificial Intelligence', 'Artificial Intelligence'), ('BigData', 'BigData'), ('Blockchain', 'Blockchain'), ('Internet of Things', 'Internet of Things'), ('Augmented Reality', 'Augmented Reality'), ('Virtual Reality', 'Virtual Reality')], max_length=273)),
                ('joined', models.DateTimeField(blank=True)),
                ('tags', models.TextField(blank=True)),
                ('comments', models.ManyToManyField(related_name='profile_comments', to='articles.Comment')),
                ('links', models.ManyToManyField(blank=True, default=0, related_name='_profile_links_+', to='profiles.Profile')),
                ('pinned_posts', models.ManyToManyField(related_name='profile_pinned_posts', to='articles.Article')),
                ('posts', models.ManyToManyField(related_name='profile_posts', to='articles.Article')),
                ('projects', models.ManyToManyField(blank=True, default=0, related_name='_profile_projects_+', to='profiles.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
