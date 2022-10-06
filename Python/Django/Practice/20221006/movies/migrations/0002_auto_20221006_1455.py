# Generated by Django 3.2.13 on 2022-10-06 05:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='files/covers'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
