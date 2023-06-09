# Generated by Django 4.2 on 2023-06-19 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_year_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sword_sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(default='null')),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]
