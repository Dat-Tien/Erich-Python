# Generated by Django 4.2.1 on 2023-05-14 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='interest',
            new_name='interests',
        ),
    ]
