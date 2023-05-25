# Generated by Django 4.2.1 on 2023-05-15 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic1', '0001_initial'),
        ('blog', '0003_alter_blog_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='topics',
        ),
        migrations.AddField(
            model_name='blog',
            name='topics',
            field=models.ManyToManyField(to='topic1.topics'),
        ),
    ]
