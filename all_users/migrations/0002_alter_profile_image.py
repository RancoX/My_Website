# Generated by Django 4.0.6 on 2022-07-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='Default.jpg', upload_to='profile_pics'),
        ),
    ]
