# Generated by Django 4.1.3 on 2023-02-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_speakers_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsers',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]