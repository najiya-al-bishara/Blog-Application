# Generated by Django 4.2 on 2023-06-05 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_alter_blog_list_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloglist',
            fields=[
                ('Blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('Author_name', models.CharField(max_length=200)),
                ('Publish_date', models.DateTimeField()),
                ('Blog_category', models.CharField(blank=True, max_length=300, null=True)),
                ('Blog_title', models.CharField(max_length=400)),
                ('Blog_caption', models.CharField(max_length=500)),
                ('Blog_image', models.ImageField(blank=True, null=True, upload_to='blogs')),
            ],
        ),
        migrations.DeleteModel(
            name='Blog_list',
        ),
    ]