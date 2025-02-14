# Generated by Django 4.2.7 on 2023-11-23 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lapblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='web',
            name='category',
            field=models.CharField(choices=[('Vlog', 'Vlog'), ('Photoblog', 'Photoblog'), ('Blognews', 'Blognews'), ('Personal blog', 'Personal Blog')], default='Vlog', max_length=64),
        ),
        migrations.AddField(
            model_name='web',
            name='poster',
            field=models.ImageField(default='images/r5.jpg', upload_to='images/'),
        ),
    ]
