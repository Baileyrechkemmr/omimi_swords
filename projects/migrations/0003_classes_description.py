# Generated by Django 4.2 on 2023-05-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_classes_sword_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='description',
            field=models.TextField(default='null'),
        ),
    ]
