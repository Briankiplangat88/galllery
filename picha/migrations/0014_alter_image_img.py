# Generated by Django 4.0.3 on 2022-03-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picha', '0013_rename_image_link_image_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(default='1', upload_to='images/'),
        ),
    ]
