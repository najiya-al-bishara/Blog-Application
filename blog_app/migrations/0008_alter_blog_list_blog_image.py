# Generated by Django 4.2 on 2023-06-05 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_alter_blog_list_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_list',
            name='Blog_image',
            field=models.ImageField(default=0, upload_to='images'),
        ),
    ]
