# Generated by Django 3.1.1 on 2020-09-29 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid
import youtubeApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('channnel_art', models.ImageField(default='default_art.jpg', upload_to='channel/')),
                ('channel_icon', models.ImageField(default='default_icon.png', upload_to='profile/')),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('catrgory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtubeApp.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VideoFiles',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('video', models.FileField(upload_to=youtubeApp.models.channel_directory_path)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtubeApp.channel')),
            ],
        ),
        migrations.CreateModel(
            name='VideoDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('visibility', models.BooleanField(choices=[(False, 'private'), (True, 'public')])),
                ('thumbnail', models.ImageField(upload_to='')),
                ('videofile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='youtubeApp.videofiles')),
            ],
        ),
    ]
