# Generated by Django 5.1.1 on 2024-10-22 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='imagen',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
