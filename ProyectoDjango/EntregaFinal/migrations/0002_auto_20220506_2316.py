# Generated by Django 3.2.13 on 2022-05-07 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EntregaFinal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webuser',
            old_name='username',
            new_name='USERNAME_FIELD',
        ),
        migrations.RenameField(
            model_name='webuser',
            old_name='pw1',
            new_name='password1',
        ),
        migrations.RenameField(
            model_name='webuser',
            old_name='pw2',
            new_name='password2',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
