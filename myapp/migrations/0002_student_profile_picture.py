# Generated by Django 5.1.1 on 2024-09-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(default='profile/default.jpg', upload_to='profile/'),
        ),
    ]
