# Generated by Django 4.2 on 2023-05-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_blog_hotel_sword_img_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='phone',
            field=models.CharField(default=-5595, max_length=100),
        ),
    ]
