# Generated by Django 3.2.15 on 2023-11-30 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to='uploadimg/'),
        ),
    ]
