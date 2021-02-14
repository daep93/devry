# Generated by Django 3.1.5 on 2021-02-14 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


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
                ('state', multiselectfield.db.fields.MultiSelectField(choices=[('Ready', 'Ready'), ('Start', 'Start'), ('End', 'End')], max_length=20)),
                ('thumnail', models.ImageField(default='', upload_to='%Y/%m/%d')),
                ('title', models.CharField(max_length=70)),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[('Conference', 'Conference'), ('Workshop', 'Workshop'), ('Hackathon', 'Hackathon'), ('competition', 'competition'), ('Meeting', 'Meeting')], max_length=49)),
                ('place', models.CharField(default='', max_length=70)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('cost', models.CharField(default='', max_length=50)),
                ('participation', models.CharField(default='', max_length=50)),
                ('introduction', models.TextField(default='')),
                ('schedule', models.TextField(default='')),
                ('host_name', models.CharField(max_length=70)),
                ('profile_img', models.ImageField(default='', upload_to='%Y/%m/%d')),
                ('register_url', models.URLField(default='')),
                ('ref_tags', multiselectfield.db.fields.MultiSelectField(choices=[('Python3', 'Python3'), ('Django', 'Django'), ('Java', 'Java'), ('Spring', 'Spring'), ('HTML5', 'HTML5'), ('CSS3', 'CSS3'), ('JavaScript', 'JavaScript'), ('TypeScript', 'TypeScript'), ('Vue.js', 'Vue.js'), ('React', 'React'), ('Angular', 'Angular'), ('Node.js', 'Node.js'), ('Swift', 'Swift'), ('Ruby', 'Ruby'), ('Ruby on Rails', 'Ruby on Rails'), ('MySQL', 'MySQL'), ('MariaDB', 'MariaDB'), ('MongoDB', 'MongoDB'), ('Docker', 'Docker'), ('Kubernetes', 'Kubernetes'), ('Frontend', 'Frontend'), ('Backend', 'Backend'), ('DevOps', 'DevOps'), ('Artificial Intelligence', 'Artificial Intelligence'), ('BigData', 'BigData'), ('Blockchain', 'Blockchain'), ('Internet of Things', 'Internet of Things'), ('Augmented Reality', 'Augmented Reality'), ('Virtual Reality', 'Virtual Reality')], max_length=273)),
                ('bookmark_num', models.PositiveIntegerField(default=0)),
                ('bookmarked', models.BooleanField(default='False')),
                ('viewed_num', models.PositiveIntegerField(default=0)),
                ('bookmark_users', models.ManyToManyField(related_name='bookmark_evnets', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
