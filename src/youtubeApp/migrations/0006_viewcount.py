# Generated by Django 3.1.1 on 2020-12-10 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeApp', '0005_auto_20201025_0324'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=50)),
                ('session', models.CharField(max_length=50)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='view_count', to='youtubeApp.videofiles')),
            ],
        ),
    ]
