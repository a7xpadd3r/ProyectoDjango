# Generated by Django 3.2.13 on 2022-05-08 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EntregaFinal', '0007_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]
