# Generated by Django 4.2.1 on 2023-05-14 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_rename_interests_person_interest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='interest',
            new_name='interests',
        ),
    ]
