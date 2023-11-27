# Generated by Django 4.2 on 2023-11-27 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_remove_sword_img_image_remove_sword_sales_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(default='null')),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='images',
        ),
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.ManyToManyField(blank=True, to='projects.blogimages'),
        ),
    ]
