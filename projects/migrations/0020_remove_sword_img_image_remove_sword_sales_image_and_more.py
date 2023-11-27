# Generated by Django 4.2 on 2023-11-27 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_blogimages_blog_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sword_img',
            name='image',
        ),
        migrations.RemoveField(
            model_name='sword_sales',
            name='image',
        ),
        migrations.AddField(
            model_name='sword_img',
            name='images',
            field=models.CharField(default='null'),
        ),
        migrations.AddField(
            model_name='sword_sales',
            name='images',
            field=models.CharField(default='null'),
        ),
        migrations.RemoveField(
            model_name='blog',
            name='images',
        ),
        migrations.DeleteModel(
            name='BlogImages',
        ),
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.CharField(default='null'),
        ),
    ]
