# Generated by Django 4.0.6 on 2022-08-01 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='Default1.jpg', upload_to='profile_pics'),
        ),
    ]
