# Generated by Django 3.2.13 on 2022-05-08 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EntregaIntermedia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genadmin',
            name='adminavatar',
            field=models.ImageField(blank=True, null=True, upload_to='admins'),
        ),
        migrations.AddField(
            model_name='genadmin',
            name='creationdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genadmin',
            name='modificationdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genitem',
            name='creationdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genitem',
            name='itemicon',
            field=models.ImageField(blank=True, null=True, upload_to='items'),
        ),
        migrations.AddField(
            model_name='genitem',
            name='modificationdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genuser',
            name='creationdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genuser',
            name='modificationdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genuser',
            name='playericon',
            field=models.ImageField(blank=True, null=True, upload_to='players'),
        ),
        migrations.AddField(
            model_name='genvehicle',
            name='creationdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genvehicle',
            name='modificationdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genvehicle',
            name='vehicleicon',
            field=models.ImageField(blank=True, null=True, upload_to='vehicles'),
        ),
    ]
